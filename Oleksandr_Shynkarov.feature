Feature: Testing EPAM website

  Scenario: epam_is_on
    Given browser is opened
    When go to "https://www.epam.com/"
    Then "https://www.epam.com/" will open in browser

  Scenario:  fullscreen_test
    Given "https://www.epam.com/" is opened
    When push "F11" on keybord
    Then site will open in fullscreen

  Scenario:  Inspecting_button_find_your_dream_job
    Given "https://www.epam.com/" is opened
    When push button named "Find your dream job"
    Then page readresses to "https://www.epam.com/careers"

  Scenario:  reloading_of_website
    Given "https://www.epam.com/" is opened
    When push "Ctrl+R" on keybord
    Then site will reload

  Scenario:  scaling_change
    Given "https://www.epam.com/" is opened
    When reduce browser scale
    Then site will reduce its scale

  Scenario Outline: entering_any_adress_in_domain
    Given "https://www.epam.com/" is opened
    When go to site "https://www.epam.com/{domain}"
    Then site will open error 404 in EPAM domain
    Examples:
    |          domain          |
    |           dsds           |
    |          asdasd          |
    |          asdadw          |

  Scenario Outline: readress_to_sphere_is_working_om
    Given "https://www.epam.com/" is opened
    When press button "{sphere}"
    Then site readress  to "https://www.epam.com/services/{sphere}"
    Examples:
    |          sphere          |
    |         engineer         |
    |         operate          |
    |         optimize         |

  Scenario Outline: country_check
    Given "https://www.epam.com/" is opened
    When place cursor on "{country}"
    Then image of {"country} will change"
    Examples:
    |          country         |
    |          Canada          |
    |          Columbia        |
    |          Mexico          |
