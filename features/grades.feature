Feature: Grades test om OrangeHRM

  Scenario: Grades normal-flow
    Given we have driver initialized
    When we login successfully
     And we add new grade
    Then we have new row
     And we remove row