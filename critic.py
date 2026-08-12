def review_test_cases(test_cases):
    gaps = []

    required_sections = [
        "Positive Test",
        "Negative Test",
        "Boundary Test",
        "Edge Test"
    ]

    for section in required_sections:
        if section not in test_cases:
            gaps.append(f"Missing {section}")

    return gaps
