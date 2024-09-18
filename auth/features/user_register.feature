Feature: User Management

  Scenario: Register a new user and obtain an access token
    Given I am a new user
    When I register with the following details
      | email                   | username   | password    | phone_number    |
      | amin@son.ir             | aminhzdev  | adminpassword | +989331109442 |
    Then I should receive a confirmation with status 201
    And the response should contain the following details after register
      | username   | email          | phone_number    |
      | aminhzdev  | amin@son.ir    | +989331109442  |

  Scenario: Obtain an access token using credentials
    Given I am authenticated with the following credentials
      | username   | password    | phone_number     | email |
      | aminhzdev  | adminpassword | +989331109442  | amin@son.ir             |
    When I request an access token
    Then I should receive a token with status 200
    And the token response should contain the following details
      | access_token                              | expires_in | token_type | scope               |
      | <access_token>                            | 3600       | Bearer     | read write groups   |
    And I should store the access token for subsequent requests


  Scenario: Retrieve users with the stored access token
    Given I am authenticated with the stored access token
      | email                   | username   | password    | phone_number    |
      | amin@son.ir             | aminhzdev  | adminpassword | +989331109442 |
    When I request the list of users
    Then I should receive a list of users with status 200
    And the response should contain the following details
      | username   | phone_number     | email            |
      | aminhzdev  | +989331109442    | amin@son.ir      |


