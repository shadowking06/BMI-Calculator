# bmi_calculator.py

def calculate_bmi(weight, height):
    """
    Calculate the BMI (Body Mass Index)
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)  

# Round the BMI to 2 decimal places

def categorize_bmi(bmi):
    """
    Categorize the BMI into health categories
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to prompt user input and display results
    """
    while True:
        try:
            weight = float(input("Enter your weight (in kilograms): "))
            height = float(input("Enter your height (in meters): "))

            # Validate user input
            if weight <= 0 or height <= 0:
                print("Invalid input. Please enter positive values.")
                continue

            bmi = calculate_bmi(weight, height)
            category = categorize_bmi(bmi)

            print(f"Your BMI is: {bmi}")
            print(f"Your category is: {category}")
            break

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()