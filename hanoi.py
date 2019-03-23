towers = {
    1: [],
    2: [],
    3: []
}

n = 3

towers[1] = [4, 3, 2, 1]

def print_state():
    print(towers[1])
    print(towers[2])
    print(towers[3])
    print('------')

def move_ring(origin, destination):
    ring = towers[origin].pop()
    
    if len(towers[destination]) > 0 and towers[destination][-1] < ring:
        raise Exception('Invalid move')
    
    towers[destination].append(ring)
    print_state()

def move_rings(n, origin, destination, spare):
    if n > 0:
        print(f'moving {n}')
        move_rings(n - 1, origin, destination, spare)
        move_ring(origin, spare)
        move_rings(n - 1, destination, origin, spare)
        move_ring(spare, destination)
        move_rings(n - 1, origin, destination, spare)

move_rings(4, 1, 3, 2)