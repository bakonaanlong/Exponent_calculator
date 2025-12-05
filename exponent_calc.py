import math

def calculate_exponent(base, result):
    if base <= 0:
        return "Error: Base must be positive"
    if result <= 0:
        return "Error: Result must be positive"
    if base == 1:
        if result == 1:
            return "Any exponent works (1^x = 1 for any x)"
        else:
            return "No solution (1 raised to any power equals 1)"
    
    # Using logarithms: if base^exponent = result, then exponent = log(result)/log(base)
    exponent = math.log(result) / math.log(base)
    return exponent

# Main program
print("=== Exponent Calculator ===")
print("This calculator finds x in the equation: base^x = result\n")

try:
    base = float(input("Enter the base number: "))
    result = float(input("Enter the result: "))
    
    exponent = calculate_exponent(base, result)
    
    if isinstance(exponent, str):
        print(f"\n{exponent}")
    else:
        print(f"\n{base}^{exponent:.6f} = {result}")
        print(f"The exponent is: {exponent:.6f}")
        
        # Verify the answer
        verification = base ** exponent
        print(f"\nVerification: {base}^{exponent:.6f} = {verification:.6f}")
        
except ValueError:
    print("\nError: Please enter valid numbers")
except Exception as e:
    print(f"\nAn error occurred: {e}")