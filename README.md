# Exponent Calculator

A simple Python calculator that finds the exponent when given a base number and result.

## Description

This calculator solves for **x** in the equation: `base^x = result`

For example:
- If base = 2 and result = 8, it calculates x = 3 (since 2³ = 8)
- If base = 10 and result = 1000, it calculates x = 3 (since 10³ = 1000)

## Features

-  Calculates exponents using logarithms
-  Handles decimal exponents
-  Input validation and error handling
-  Automatic result verification
-  Multiple calculations in one session
-  Precision error checking

## Requirements

- Python 3.x
- No external libraries required (uses built-in `math` module)

## Usage

1. Run the program:
```bash
python exponent_calc1.py
```

2. Enter the base number when prompted
3. Enter the result value
4. View the calculated exponent
5. Choose to perform another calculation or exit

### Example Session

```
========================================
       EXPONENT CALCULATOR
========================================
Finds x in the equation: base^x = result
========================================

Enter the base number (or 'q' to quit): 2
Enter the result: 16

────────────────────────────────────────
Solution: 2^4 = 16
The exponent is: 4

Verification: 2^4 = 16
────────────────────────────────────────

Calculate another? (y/n): n

Thank you for using the Exponent Calculator!
```

## How It Works

The calculator uses the logarithmic identity:

If `base^x = result`, then `x = log(result) / log(base)`

## Limitations

- Base must be a positive number (not 0 or 1)
- Result must be a positive number
- Very large or very small numbers may have floating-point precision limitations

