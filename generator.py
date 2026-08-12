def generate_test_cases(requirement):
    return f"""
Generated Test Cases

Requirement:
{requirement}

Positive Test:
- Verify valid login succeeds

Negative Test:
- Verify invalid password fails

Boundary Test:
- Verify account locks after 5 attempts

Edge Test:
- Verify email is case insensitive
"""
