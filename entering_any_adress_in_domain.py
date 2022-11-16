from behave import *

@when('go to site "https://www.epam.com/{domain}"')
def step_impl(context, domain):
    pass

@then('site will open error 404 in EPAM domain')
def step_impl(context):
    pass