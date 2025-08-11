# Pythagorean Triples Finder

This Python program searches for Pythagorean triples up to a specified limit and identifies which of those triples are *primitive* (i.e., their greatest common divisor is 1).

## Features

- Finds all Pythagorean triples `(a, b, c)` such that \(a^2 + b^2 = c^2\) and \(a < b < c < \text{limit}\).
- Determines primitive triples by calculating the greatest common divisor (GCD) of each triple.
- Interactive command-line interface for user input.
- **Does not use Python's built-in `math` module**, as this is a learning exercise to implement key concepts manually.

## How It Works

- The program iterates through possible values of `c` and `a`.
- For each pair `(a, c)`, it calculates `b` and checks if `b` is an integer and satisfies \(a < b < c\).
- The program collects all valid triples.
- It factorizes the numbers in each triple to find common factors and thus determine if the triple is primitive.
- GCD calculation is done through factorization instead of using built-in functions from the `math` module.

## Usage

Run the script and enter a positive integer limit when prompted. Enter `0` to exit.

```bash
python pythagorean_triples.py
