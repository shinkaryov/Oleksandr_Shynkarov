import unittest
from common.helper import TestGrades

global tester


def init_driver():
    global tester
    tester = TestGrades()


def login():
    tester.login()


def add():
    tester.main_page()


def check_row():
    tester.check_row()


def remove_and_check():
    tester.remove_and_check()


if __name__ == '__main__':
    unittest.main()