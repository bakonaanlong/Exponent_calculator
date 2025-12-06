import math

def calculate_exponent(base, result):
    # Handle special cases
    if base <= 0:
        return None, "Error: Base must be positive (negative bases require complex numbers)"
    
    if base == 1:
        if result == 1:
            return None, "Indeterminate: 1 raised to any power equals 1"
        else:
            return None, "No solution: 1 raised to any power can only equal 1"
    
    # Handle negative results (requires odd integer exponents for negative bases)
    if result < 0:
        return None, "Error: Result must be positive for positive bases"
    
    if result == 0:
        return None, "Error: Result cannot be 0 (base^x = 0 has no solution for positive base)"
    
    # Calculate exponent using logarithms
    # if base^exponent = result, then exponent = log(result)/log(base)
    try:
        exponent = math.log(result) / math.log(base)
        return exponent, None
    except (ValueError, ZeroDivisionError) as e:
        return None, f"Calculation error: {e}"

def get_float_input(prompt):
    """Get and validate float input from user"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main program loop"""
    print("=" * 40)
    print("       EXPONENT CALCULATOR")
    print("=" * 40)
    print("Finds x in the equation: base^x = result")
    print("=" * 40)
    
    while True:
        print()
        base = get_float_input("Enter the base number (or 'q' to quit): ")
        result = get_float_input("Enter the result: ")
        
        exponent, error = calculate_exponent(base, result)
        
        if error:
            print(f"\n{error}")
        else:
            print(f"\n{'─' * 40}")
            print(f"Solution: {base}^{exponent:.8g} = {result}")
            print(f"The exponent is: {exponent:.8g}")
            
            # Verify the answer
            verification = base ** exponent
            print(f"\nVerification: {base}^{exponent:.8g} = {verification:.8g}")
            
            # Show percentage error (for floating point precision check)
            error_pct = abs((verification - result) / result * 100) if result != 0 else 0
            if error_pct > 0.0001:
                print(f"Precision error: {error_pct:.6f}%")
            print('─' * 40)
        
        # Ask if user wants to continue
        print()
        continue_calc = input("Calculate another? (y/n): ").lower()
        if continue_calc != 'y':
            print("\nThank you for using the Exponent Calculator!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")