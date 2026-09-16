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

The `calculate_discount()` function applies a **15% standard discount**.

```python
def calculate_discount(price):
    return price*0.15
```

## Testing

The project includes a test file using Python assertions.

```python
def test_discount():
    assert calculate_discount(100)==15
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
