# Servo Controller for Project Caesar
# by Tyler Korte
# 2019/06/17

from gpiozero import AngularServo
from time import sleep


class Dispenser:

    # raspberry pi pin to attach the servo to
    SERVO_PIN = 12

    # operating range of the servo in degrees (gamma)
    OPERATING_RANGE = 180

    # number of holes around the perimeter of the revolver (n)
    NUM_HOLES = 12

    # angle change for each hole (omega)
    MOVEMENT_AMOUNT = 360. / float(NUM_HOLES)

    # ID number of the furthest position before the direction needs to switch (beta)
    NUM_POSITIONS = 4  # int(OPERATING_RANGE / MOVEMENT_AMOUNT)

    def __init__(self):
        # servo object to control
        self.revolver = AngularServo(self.SERVO_PIN, min_angle=0, max_angle=180)

        # array of discrete possible positions
        self.positions = list()

        # boolean variable to tell if the direction is increasing or not
        self.increasing = True

        # current state of the IR sensor
        self.sensor_state = 0

        # last state of the IR sensor
        self.last_state = 0

        # cycle counter for the state change of the breakbeam sensor
        self.cycle = 0

        # balance of pellets to dispense
        self.pellet_balance = 0

        # TODO: implement empty detection
        # boolean variable to tell if the dispenser is empty
        self.empty = False

        self.closest = 0

        # todo: fix automatic angle piking
        # takes the number of the furthest position, angle change per movement in degrees,
        #    and a pointer to an array to returns the positions in
        # returns a modified version of the positions array populated with the discrete possible positions
        # def find_positions():  # This used to be a function, but it was only ever used once
        # self.positions.append(0.)
        # counter = 1
        # while (counter * self.MOVEMENT_AMOUNT) < self.OPERATING_RANGE:
        #     self.positions.append((self.positions[counter-1] + self.MOVEMENT_AMOUNT))
        #     counter += 1

        # optimal positions: 15, 65, 115, 165
        self.positions = (15., 65., 115., 165.)

        # self.closest = self.find_closest(self.revolver.angle)
        print(self.positions)

        # current discrete position of the revolver set to the center position
        self.pos = int(len(self.positions)/2.)  # self.find_closest(self.revolver.angle)

        # adjust to the closest acceptable angle
        self.revolver.angle = self.positions[self.pos]

    # takes current position in degrees
    # returns the closest position in the set to that position
    def find_closest(self, position):
        #     if position == 0:
        #         return 0
        #     elif position >= operating_range - 1:
        #         return num_positions - 1
        #     else:
        #         # //    byte closestpos = 1
        #         #     for (int i = 2; i < numpositions - 1; i++)
        #         for i in range(2, num_positions - 1):
        #             # //      Serial.println(closestpos)
        #             if positions[i] > position:
        #                 return i
        # # //      if (abs(pos - positions[i]) < abs(pos - positions[closestpos])) {
        # # //        closestpos = i;
        # # //      }
        #     # return closestpos

        closest = 0
        for i in range(self.NUM_POSITIONS):
            if abs(self.positions[i] - position) < abs(self.positions[closest] - position):
                closest = i
        return closest

    def dispense(self, num_pellets):
        num_pellets = int(num_pellets)
        while num_pellets > 0:
            print('Pellet dispensed')
            print(self.pos)
            if self.increasing:
                if self.pos >= self.NUM_POSITIONS - 1:
                    self.pos -= 1
                    self.increasing = False
                else:
                    self.pos += 1
            else:
                if self.pos <= 0:
                    self.pos += 1
                    self.increasing = True
                else:
                    self.pos -= 1
            self.revolver.angle = self.positions[self.pos]
            num_pellets -= 1
            sleep(0.7)

    # dispenser setup for multiprocessing
    # def dispense_queue(self, q):
    #     while True:
    #         if q.empty():
    #             pass  # I might want to sleep instead of passing
    #         else:
    #             item = q.get()
    #             if item is
    #             :
    #                 break
    #             else:
    #                 self.dispense(int(item))


def thread_dispenser(q):
    d = Dispenser()

    while True:
        if q.empty():
            pass  # I might want to sleep instead of passing
        else:
            item = q.get()
            if item == 'poison pill':
                break
            else:
                d.dispense(int(item))


# For running tests
def main():
    print('Hi world')
    dispenser = Dispenser()
    print('positions', dispenser.NUM_POSITIONS)
    print(dispenser.positions)

    while True:
        n = int(input('insert number of pellets to dispense: '))
        dispenser.dispense(n)
        # dispenser.q.put(n)


if __name__ == '__main__':
    main()
