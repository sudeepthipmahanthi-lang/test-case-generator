from generator import generate_test_cases
from critic import review_test_cases

requirement = """
User Login
"""

tests = generate_test_cases(requirement)

print("Generated Tests:")
print(tests)

gaps = review_test_cases(tests)

print("\nCoverage Gaps:")
print(gaps)
