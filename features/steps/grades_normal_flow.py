from behave import *
from common.helper import TestGrades
global tester


@given('we have driver initialized')
def init_driver(context):
    global tester
    tester = TestGrades()


@when('we login successfully')
def login(context):
    tester.login()


@when('we add new grade')
def add(context):
    tester.main_page()


@then('we have new row')
def check_row(context):
    tester.check_row()


@then('we remove row')
def remove_and_check(context):
    tester.remove_and_check()

