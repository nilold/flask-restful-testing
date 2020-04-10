from unittest import TestCase
from locker import *


class LockerTest(TestCase):

    def test_assert_one_right_at_wrong_pos(self):
        prof_num = "614"
        true_nums = ["042", "062", "102", "402", "601", "606", ]
        wrong_nums = ["042", "062", "102", "402", "601", "606", ]

        for n in true_nums:
            self.assertTrue(assert_one_right_at_wrong_pos(n, prof_num))
