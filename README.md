## My Pipeline Badge

[![amogh-w](https://circleci.com/gh/amogh-w/clean-code-ml.svg?style=svg)](https://circleci.com/gh/amogh-w/clean-code-ml)

---

# clean-code-ml

Now available as a free tutorial series: https://bit.ly/2yGDyqT 😎

## Table of Contents

- [Introduction](#introduction)
- [Dev Productivity](docs/dev-tools.md)
  - Use Docker and stop hearing "Works on my machine!"
  - Ensure reproducibility
  - VS Code productivity tips (or "Know Your IDE")
- [Variables](docs/variables.md)
  - Variable names should reveal intent
  - Use meaningful and pronounceable variable names
  - Use the same vocabulary for the same type of variable
  - Avoid magic numbers and magic strings
  - Use variables to keep code "DRY" ("Don't Repeat Yourself")
  - Use explanatory variables
  - Avoid mental mapping
  - Don't add unneeded context
- [Dispensables](docs/dispensables.md)
  - Avoid comments
  - Remove dead code
  - Avoid print statements (even glorified print statements such as df.head(), df.describe(), df.plot())
- [Functions](docs/functions.md)
  - Use functions to keep code "DRY"
  - Functions should do one thing
  - Functions should only be one level of abstraction
  - Function names should say what they do
  - Use type hints to improve readability
  - Avoid side effects
  - Avoid unexpected side effects on values passed as function parameters
  - Function arguments (2 or fewer ideally)
  - Use default arguments instead of short circuiting or conditionals
  - Don't use flags as function parameters
- [Design](docs/design.md)
  - Avoid exposing your internals (Keep implementation details hidden)

## Introduction

Clean code practices (from [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) and [Refactoring](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599)) adapted for machine learning / data science workflows in Python. This is not a style guide. It's a guide to producing
readable, reusable, and refactorable software.

If you’ve tried your hand at machine learning or data science, you would know that code can get messy, quickly.

Unclean code adds to complexity by making code difficult to read and modify. As a consequence, changing code to respond to business needs becomes increasingly difficult, and sometimes even impossible. This has been written about extensively in several languages, and even in Python (e.g. Clean Code, Refactoring, clean-code-python). In this repo, we have adapted these principles for data science / machine learning codebases.

Targets Python3.7+

Inspired by [clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript) and forked from [clean-code-python](https://github.com/zedr/clean-code-python).

## The 5 S's of Clean Code

By James O Coplien (Source: Foreword of Clean Code (Robert C. Martin))

In about 1951, a quality approach called Total Productive Maintenance (TPM) came on the Japanese scene. Its focus is on maintenance rather than on production. One of the major pillars of TPM is the set of so-called 5S principles:
- **Seiri**, or organization (think **sort** in English). Knowing where things are—using approaches such as suitable naming—is crucial.
- **Seiton**, or tidiness (think **systematize** in English). There is an old American saying: A place for everything, and everything in its place. A piece of code should be where you expect to find it—and, if not, you should re-factor to get it there.
- **Seiso**, or cleaning (think **shine** in English): Keep the workplace free of hanging wires, grease, scraps, and waste. What do the authors here say about littering your code with comments and commented-out code lines that capture history or wishes for the future? Get rid of them.
- **Seiketsu**, or **standardization**: The group agrees about how to keep the workplace clean. Have a consistent coding style and set of practices within the group.
- **Shutsuke**, or discipline (**self-discipline**). This means having the discipline to follow the practices and to frequently reflect on one’s work and be willing to change.

## Hands-on Exercise

If you'd like to try out these practices, we've created a [refactoring exercise](./docs/refactoring-exercise.md) which you can follow along. Starting with [a jupyter notebook with many code smells](notebooks/titanic-notebook-1.ipynb), you can apply these clean code principles and refactor it to be readable and maintainable. The sample final solution can be found in [`src/train.py`](src/train.py).

