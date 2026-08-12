def review_test_cases(test_cases):
    gaps = []

    if "Positive Test" not in test_cases:
        gaps.append("Missing positive test coverage")

    if "Negative Test" not in test_cases:
        gaps.append("Missing negative test coverage")

    if "Boundary Test" not in test_cases:
        gaps.append("Missing boundary test coverage")

    if "Edge Test" not in test_cases:
        gaps.append("Missing edge test coverage")

    return gaps
