# Test Case Generator Design

## Problem Statement

The goal is to generate requirement-traceable test cases from requirements and acceptance criteria.

## Agent Architecture

Requirement Input
↓
Test Generator
↓
Generated Tests
↓
Critic
↓
Coverage Gap Detection
↓
Additional Tests
↓
Final Test Suite

## Agentic Behaviour

The solution follows a generate-then-critique loop.

Step 1:
Generate positive, negative, boundary, and edge test cases.

Step 2:
Review generated tests.

Step 3:
Identify missing coverage.

Step 4:
Add missing tests.

Step 5:
Produce final output.

## Components

### generator.py

Creates initial test cases.

### critic.py

Reviews generated tests for coverage gaps.

### main.py

Combines generation and review.

## Output Formats

- Gherkin
- Feature files
- Coverage review

## Challenges

- Ensuring AC coverage
- Avoiding duplicate tests
- Identifying edge cases

## Improvements

- Integration with OpenAI
- CSV export
- TestRail export
- Traceability matrix generation
