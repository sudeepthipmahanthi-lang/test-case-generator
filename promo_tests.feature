Feature: Apply Promo Code at Checkout

Scenario: Valid percentage code
Given subtotal is ₹1000
When SAVE10 is applied
Then ₹100 discount is applied

Scenario: Valid fixed code
Given subtotal is ₹1500
When FLAT200 is applied
Then ₹200 discount is applied

Scenario: Fixed code below minimum
Given subtotal is ₹800
When FLAT200 is applied
Then "This code requires a minimum order of ₹1000."

Scenario: Expired promo code
When an expired code is entered
Then "This code has expired."

Scenario: Invalid promo code
When a non-existent code is entered
Then "Invalid promo code."

Scenario: Case insensitive promo
When save10 is entered
Then same discount as SAVE10 is applied

Scenario: Single-use code already redeemed
When customer reuses redeemed code
Then "This code has already been used."

Scenario: Discount cap
Given subtotal is ₹150
When FLAT200 is applied
Then subtotal becomes ₹0

Scenario: Replace existing code
Given SAVE10 is already applied
When FLAT200 is entered
Then user is asked to confirm replacement

Scenario: Empty promo input
When Apply is clicked with no code
Then "Enter a promo code."

Scenario: Trim whitespace
When " SAVE10 " is entered
Then spaces are removed before validation

Scenario: Revalidate on cart change
Given FLAT200 is applied
When cart subtotal falls below ₹1000
Then discount is removed
