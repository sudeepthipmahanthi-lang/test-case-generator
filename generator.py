def generate_test_cases(requirement):
    if "login" in requirement.lower():
        return """
LOGIN-001 (AC1)
Positive Test:
- Verify successful login with valid credentials

LOGIN-002 (AC2)
Negative Test:
- Verify login fails with incorrect password

LOGIN-003 (AC3)
Negative Test:
- Verify login fails with unregistered email

LOGIN-004 (AC4)
Negative Test:
- Verify validation appears for blank fields

LOGIN-005 (AC5)
Negative Test:
- Verify invalid email format message

LOGIN-006 (AC6)
Boundary Test:
- Verify account locks after 5 failed attempts

LOGIN-007 (AC7)
Edge Test:
- Verify email is case insensitive

LOGIN-008 (AC8)
Positive Test:
- Verify session persists after refresh

LOGIN-009 (AC9)
Negative Test:
- Verify inactive account cannot login
"""
