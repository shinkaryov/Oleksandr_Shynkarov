from behave import *

@when('press button "{sphere}"')
def step_impl(context, sphere):
    pass

@then('site readress  to "https://www.epam.com/services/{sphere}"')
def step_impl(context, sphere):
    pass