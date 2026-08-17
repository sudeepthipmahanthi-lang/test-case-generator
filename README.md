# Test Case Generator

## Overview

This project generates software test cases from requirements and acceptance criteria.

## Features

- Positive test generation
- Negative test generation
- Boundary test generation
- Edge case generation
- Coverage gap detection
- Requirement traceability

## Agentic Workflow

1. Generate test cases
2. Review generated test cases
3. Identify coverage gaps
4. Generate missing test cases
5. Produce final test suite

## Files

- generator.py
- critic.py
- main.py

## Sample Use Case

Input:
User Login requirement

Output:
Positive, Negative, Boundary, and Edge test cases with coverage review.

## How to Run

1. Run the application

python main.py

2. Enter one of the following requirements

- User Login
- Apply Promo Code

3. Review the generated test cases and coverage report

## Agent Flow

Requirement Input
↓
Test Case Generator
↓
Coverage Critic
↓
Coverage Report
↓
Final Test Suite

## Supported Features

### Feature A - User Login

- Valid Login
- Invalid Password
- Unregistered Email
- Empty Fields
- Email Format Validation
- Account Lockout
- Case Sensitivity
- Session Management
- Inactive Account

### Feature B - Apply Promo Code

- Valid Percentage Discount
- Valid Fixed Discount
- Minimum Order Validation
- Expired Code Validation
- Invalid Code Validation
- Case Insensitivity
- Single Use Enforcement
- Discount Cap
- Promo Replacement
- Empty Input Validation
- Whitespace Handling
- Cart Revalidation
