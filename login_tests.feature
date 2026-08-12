Feature: User Login

Scenario: Successful login
Given an active registered user
When valid email and password are entered
Then user is redirected to dashboard

Scenario: Invalid password
Given a registered user
When correct email and incorrect password are entered
Then "Invalid email or password" is displayed

Scenario: Unregistered email
When an unregistered email is entered
Then "Invalid email or password" is displayed

Scenario: Empty fields
When login is clicked with blank fields
Then validation messages are shown

Scenario: Invalid email format
When email format is invalid
Then "Enter a valid email address" is displayed

Scenario: Account lockout
Given 5 failed attempts within 15 minutes
Then account is locked for 30 minutes

Scenario: Email case insensitive
When USER@X.COM is entered instead of user@x.com
Then login succeeds

Scenario: Password case sensitive
When password case differs
Then login fails

Scenario: Session persistence
Given successful login
When browser refreshes
Then user remains logged in

Scenario: Inactive account
Given account is inactive
When valid credentials are entered
Then "This account is inactive. Contact support."
