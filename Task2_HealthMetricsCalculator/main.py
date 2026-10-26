
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m * height_m)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("=" * 40)
    print("       HEALTH METRICS CALCULATOR")
    print("          BMI CALCULATOR")
    print("=" * 40)

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive.")
            return

        bmi = calculate_bmi(weight, height)

        print("\n---------- BMI RESULT ----------")
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {get_category(bmi)}")
        print("--------------------------------")
        print("Note: BMI is a general screening measure,")
        print("not a medical diagnosis.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()
