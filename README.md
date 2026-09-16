# Discount Calculator

A simple Python project created to demonstrate basic **Software Configuration Management (SCM)** concepts using **Git and GitHub**. The project demonstrates how a small application can evolve through version control, change tracking, commits, and branching.

## Project Structure

```text
SCM-Demo/
└── src/   
    ├── calculator.py
    └── test_calculator.py
```

## Features
```
- Calculates a standard discount
- Includes basic automated tests
- Tracks changes using Git
- Maintains a history of project versions
```
## Current Implementation

The `calculate_discount()` function applies a **10% standard discount** and **20% member-specific discount**.

```python
def calculate_discount(price, is_member):
    if is_member:
        return price*0.20

    return price*0.10
```

## Testing

The project includes a test file using Python assertions.

```python
def test_regular_customer():
    assert calculate_discount(100, False)==10

def test_member_customer():
    assert calculate_discount(100, True)==20
```

## Git Workflow

This project was used to demonstrate:

1. Repository initialization
2. Tracking files with Git
3. Staging changes
4. Creating commits
5. Viewing commit history
6. Tracking modifications with `git diff`
7. Creating feature branches

## Branches

### `main`

Contains the stable version of the project.

### `feature-member-discount`

Contains experimental development for **member-specific discounts** without immediately modifying the stable `main` branch.

## Purpose

The goal of this project is not complexity, but to provide a small and understandable example of how Git can support SCM practices such as **version control, traceability, change tracking, and controlled development**.
