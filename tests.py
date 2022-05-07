import unittest
from logics import get_number_from_index, get_emty_list,\
    get_index_from_number, is_zero_in_mas, move_left, move_up, \
    can_move



class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_emty_list(mas), a)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_emty_list(mas), a)

    def test_4(self):
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_5(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_6(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_7(self):
        mas = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_8(self):
        mas = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0]
        ]
        rez = [
            [4, 0, 0, 0],
            [0, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 12))


    def test_9(self):
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 24))


    def test_10(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 32))

    def test_11(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rez = [
            [2, 4, 8, 4],
            [4, 8, 0, 4],
            [8, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), (rez, 12))

    def test_12(self):
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]

        self.assertEqual(can_move(mas), True)

    def test_13(self):
        mas = [
            [2, 4, 8, 2],
            [4, 8, 2, 4],
            [2, 4, 8, 16],
            [8, 8, 4, 4]
        ]

        self.assertEqual(can_move(mas), False)