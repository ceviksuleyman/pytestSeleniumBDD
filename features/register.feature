Feature: Register Account functionality

  @register1
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      | first_name | last_name | telephone  | password |
      | Thomas     | Malthus   | 7988878978 | qwerty1  |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter below details into all fields
      | first_name | last_name | telephone  | password |
      | Maynard    | Keynes    | 7988878978 | qwerty1  |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created

  @register
  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter details into all fields except email field
      | first_name | last_name | telephone  | password |
      | Adam       | Smith     | 7988878978 | qwerty1  |
    And I enter existing accounts email into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed