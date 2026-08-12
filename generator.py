def generate_test_cases(requirement):
    if "login" in requirement.lower():
        return """
Positive Test:
- Verify successful login with valid credentials

Negative Test:
- Verify login fails with invalid password

Boundary Test:
- Verify account locks after exactly 5 failed attempts

Edge Test:
- Verify email case insensitivity
"""
    
    return """
Positive Test:
- Verify valid input is accepted
"""
