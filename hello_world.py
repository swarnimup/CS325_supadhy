name = input("Enter your name: ")

# Ensure age is a positive integer
while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 0:
            break
        else:
            print("Please enter a valid positive age.")
    except ValueError:
        print("Please enter a valid integer for age.")

current_year = 2024
birth_year = current_year - age

print(f"Hello, {name}! You were born in the year {birth_year}.")

# Additional lines
month_of_birth = input("Enter the month of your birth (e.g., January): ")
print(f"You were born in {month_of_birth}, {name}!")

if age < 18:
    print(f"{name}, you are a minor.")
elif 18 <= age < 65:
    print(f"{name}, you are an adult.")
else:
    print(f"{name}, you are a senior citizen.")
