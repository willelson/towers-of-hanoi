import pytest
from hanoi import TowersOfHanoi


def test_tower_set_up():
    towers = TowersOfHanoi(5)

    assert len(towers.towers) == 3
    assert towers.towers[0] == [5, 4, 3, 2, 1]


def test_moving_one_ring():
    towers = TowersOfHanoi(3)

    towers.move_ring(0, 2)

    expected_state = [
        [3, 2],
        [],
        [1]
    ]

    assert towers.towers == expected_state


def test_moving_one_ring_invalid():
    towers = TowersOfHanoi(5)

    towers.move_ring(0, 2)

    with pytest.raises(ValueError):
        towers.move_ring(0, 2)


def test_moving_multiple_rings():
    stack_height = 5

    towers = TowersOfHanoi(stack_height)

    towers.move_rings(stack_height, 0, 2, 1)

    expected_state = [
        [],
        [],
        [5, 4, 3, 2, 1]
    ]

    assert towers.towers == expected_state


def test_moving_many_rings():
    stack_height = 9

    towers = TowersOfHanoi(stack_height)

    towers.move_rings(stack_height, 0, 1, 2)

    expected_state = [
        [],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [],
    ]

    assert towers.towers == expected_state
