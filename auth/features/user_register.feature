Feature: User Management

  Scenario Outline: Register a new user
    Given I am a new user
    When I register with the following details
      | email                   | username   | password    | phone_number    |
      | <email>                 | <username> | <password>  | <phone_number>  |
    Then I should receive a confirmation with status 201
    And the response should contain the following details
      | username   | email          | phone_number    |
      | <username> | <email>        | <phone_number>  |

    Examples:
      | email                   | username   | password    | phone_number    |
      | amin@son.ir             | aminhzdev  | adminpassword | +989331109442 |
      | john@example.com        | johnsmith  | password123  | +989123456789 |

  Scenario Outline: Create a new user
    Given I am authenticated
    When I create a user with the following details
      | email                   | username   | password    | phone_number    |
      | <email>                 | <username> | <password>  | <phone_number>  |
    Then I should receive a confirmation with status 201
    And the response should contain the following details
      | username   | email          |
      | <username> | <email>        |

    Examples:
      | email                   | username   | password    | phone_number    |
      | newuser@example.com     | newuser    | newpassword | +989335692244 |
      | anotheruser@example.com | anotheruser| anotherpass | +989877654321 |

  Scenario Outline: Retrieve a user
    Given I am authenticated
    And I have created a user with the following details
      | username    | email                | password    |
      | <username> | <email>              | <password> |
    When I retrieve the user with username "<username>"
    Then I should receive the user's details with status 200
    And the details should contain the following information
      | username    | email                |
      | <username> | <email>              |

    Examples:
      | username    | email                | password    |
      | retrieveuser | retrieveuser@example.com | password |
      | testuser     | testuser@example.com     | testpass  |

  Scenario Outline: Update a user's details
    Given I am authenticated
    And I have created a user with the following details
      | username    | email                | password    |
      | <username> | <email>              | <password> |
    When I update the user's email with the following details
      | email                   | phone_number    |
      | <new_email>             | <phone_number>  |
    Then I should receive a confirmation with status 200
    And the response should contain the updated details
      | email                   | phone_number    |
      | <new_email>             | <phone_number>  |

    Examples:
      | username    | email                | password    | new_email               | phone_number    |
      | updateuser  | updateuser@example.com | password | updateduser@example.com | +989446558552 |
      | anotheruser | anotheruser@example.com| anotherpass | newanotheruser@example.com | +989123456789 |

  Scenario Outline: Delete a user
    Given I am authenticated
    And I have created a user with the following details
      | username    | email                | password    |
      | <username> | <email>              | <password> |
    When I delete the user with username "<username>"
    Then I should receive a confirmation with status 204
    And the user should no longer exist

    Examples:
      | username    | email                | password    |
      | deleteuser  | deleteuser@example.com | password |
      | removeme    | removeme@example.com   | removepass |