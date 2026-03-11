# Menu Driven BMI Calculator

def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("\nYour BMI is:", round(bmi, 2))
    print("BMI Category:", category)


def bmi_categories():
    print("\nBMI Categories:")
    print("Below 18.5   : Underweight")
    print("18.5 - 24.9  : Normal Weight")
    print("25 - 29.9    : Overweight")
    print("30 and above : Obese")


while True:
    print("\n===== BMI CALCULATOR MENU =====")
    print("1. Calculate BMI")
    print("2. View BMI Categories")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        calculate_bmi()

    elif choice == '2':
        bmi_categories()

    elif choice == '3':
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")