

class TowersOfHanoi():

    def __init__(self, stack_height):
        """ Set up tower initial state with rings placed on first tower

        param stack_height: Number of rings
        type  stack_height: int
        """

        self.stack_height = stack_height
        self.moves = 0

        self.towers = [[], [], []]
        self.towers[0] = [i for i in range(self.stack_height, 0, -1)]

    def __str__(self):
        """ Output the state of the towers
        """

        return '{}\n{}\n{}\n{}'.format(*self.towers, '-' * 10)

    def move_ring(self, origin, destination):
        """ Move a ring from the origin tower to the destination tower

        param origin: Index of tower from which the ring is moved from
        type  origin: int
        param destination: Index of tower from which the ring is moved to
        type  destination: int
        """

        if not self.towers[origin]:
            raise ValueError('No ring on origin tower')

        ring = self.towers[origin].pop()

        if len(self.towers[destination]) > 0 and self.towers[destination][-1] < ring:
            raise ValueError('Invalid move')

        self.towers[destination].append(ring)
        print(self)

        self.moves += 1

    def move_rings(self, n, origin, destination, spare):
        """ sMove all rings from the origin to tower to the destination tower

        param n: Index of tower from which the stack of rings is moved from
        type  n: int
        param origin: Index of tower from which ring is moved from
        type  origin: int
        param destination: Index of tower from which the stack of rings ring is moved to
        type  destination: int
        param spare: Index of tower that is neiter the origin or destination of the stack
        type  spare: int
        """

        if n > 0:
            self.move_rings(n - 1, origin, spare, destination)
            self.move_ring(origin, destination)
            self.move_rings(n - 1, spare, destination, origin)


if __name__ == '__main__':
    stack = 6

    towers = TowersOfHanoi(stack)
    towers.move_rings(stack, 0, 2, 1)

    print(towers.moves)
