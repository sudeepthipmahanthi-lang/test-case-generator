def calculate_coverage(total_ac, covered_ac):
    if total_ac == 0:
        return "Coverage: 0%"

    percentage = (covered_ac / total_ac) * 100
    return f"Coverage: {percentage:.0f}%"
