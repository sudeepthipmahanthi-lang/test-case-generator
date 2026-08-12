def generate_test_cases(requirement):
    return f"""
Positive Test:
- Verify valid scenario works

Negative Test:
- Verify invalid input fails

Boundary Test:
- Verify minimum and maximum values

Edge Test:
- Verify unusual but valid conditions

Requirement:
{requirement}
"""
