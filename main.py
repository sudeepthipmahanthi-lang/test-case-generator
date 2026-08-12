\from generator import generate_test_cases
from critic import review_test_cases

print("=== Test Case Generator ===")

requirement = input("Enter requirement: ")

tests = generate_test_cases(requirement)

print("\n=== GENERATED TEST CASES ===")
print(tests)

gaps = review_test_cases(tests)

print("\n=== CRITIQUE RESULT ===")

if gaps:
    print("Coverage gaps found:")
    for gap in gaps:
        print(f"- {gap}")
else:
    print("No coverage gaps found.")
