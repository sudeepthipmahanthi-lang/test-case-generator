def generate_test_cases(requirement):

    if "login" in requirement.lower():
        return """
LOGIN-001 (AC1)
Positive Test:
- Verify successful login with valid credentials

LOGIN-002 (AC2)
Negative Test:
- Verify login fails with invalid password

LOGIN-003 (AC3)
Negative Test:
- Verify login fails with unregistered email

LOGIN-004 (AC4)
Negative Test:
- Verify validation appears when fields are blank

LOGIN-005 (AC5)
Negative Test:
- Verify invalid email format error message

LOGIN-006 (AC6)
Boundary Test:
- Verify account locks after exactly 5 failed attempts

LOGIN-007 (AC7)
Edge Test:
- Verify email is case insensitive

LOGIN-008 (AC8)
Positive Test:
- Verify session persists after browser refresh

LOGIN-009 (AC9)
Negative Test:
- Verify inactive account cannot log in
"""

    if "promo" in requirement.lower():
        return """
PROMO-001 (AC1)
Positive Test:
- Verify SAVE10 applies 10 percent discount

PROMO-002 (AC2)
Positive Test:
- Verify FLAT200 applies ₹200 discount

PROMO-003 (AC3)
Negative Test:
- Verify FLAT200 is rejected below minimum order value

PROMO-004 (AC4)
Negative Test:
- Verify expired code is rejected

PROMO-005 (AC5)
Negative Test:
- Verify invalid promo code is rejected

PROMO-006 (AC6)
Edge Test:
- Verify promo code is case insensitive

PROMO-007 (AC7)
Negative Test:
- Verify already used promo code is rejected

PROMO-008 (AC8)
Boundary Test:
- Verify discount never reduces subtotal below zero

PROMO-009 (AC9)
Edge Test:
- Verify existing promo code can be replaced

PROMO-010 (AC10)
Negative Test:
- Verify error appears for empty promo code

PROMO-011 (AC11)
Edge Test:
- Verify leading and trailing spaces are trimmed

PROMO-012 (AC12)
Boundary Test:
- Verify discount is removed when cart subtotal drops below eligibility
"""

    return """
Positive Test:
- Verify valid input is accepted

Negative Test:
- Verify invalid input is rejected

Boundary Test:
- Verify minimum and maximum limits

Edge Test:
- Verify unusual but valid scenarios
"""
