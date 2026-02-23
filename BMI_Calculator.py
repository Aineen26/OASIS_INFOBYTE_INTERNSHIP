def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight in kilograms: "))

        # Take height input in feet and inches
        feet = int(input("Enter your height (feet): "))
        inches = int(input("Enter your height (inches): "))

        # Convert feet + inches to meters
        total_inches = feet * 12 + inches
        height = total_inches * 0.0254

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()