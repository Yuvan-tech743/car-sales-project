# Car Sales System (Simple Grade Version)

# Step 1: Show car models
print("BMW Car Models:")
print("1. BMW X1 - $35000")
print("2. BMW X3 - $45000")
print("3. BMW X5 - $60000")
print("4. BMW 3 Series - $42000")
print("5. BMW 7 Series - $90000")

# Step 2: Ask user to choose a car
car_choice = int(input("Enter the car number (1-5): "))

# Set car name and price based on choice
if car_choice == 1:
    car_name = "BMW X1"
    price = 35000
elif car_choice == 2:
    car_name = "BMW X3"
    price = 45000
elif car_choice == 3:
    car_name = "BMW X5"
    price = 60000
elif car_choice == 4:
    car_name = "BMW 3 Series"
    price = 42000
elif car_choice == 5:
    car_name = "BMW 7 Series"
    price = 90000
else:
    car_name = "Invalid Choice"
    price = 0

print("You selected:", car_name)
print("Price: $", price)

# Step 3: Payment option
print("\nPayment Options:")
print("1. Cash")
print("2. Credit Card")
print("3. Loan")

pay = int(input("Choose your payment method (1-3): "))

if pay == 1:
    payment_method = "Cash"
elif pay == 2:
    payment_method = "Credit Card"
elif pay == 3:
    payment_method = "Loan"
else:
    payment_method = "Invalid Option"

# Step 4: Refreshments
print("\nRefreshments:")
print("1. Tea")
print("2. Coffee")
print("3. Cold Drink")
print("4. None")

ref = int(input("Choose your refreshment (1-4): "))

if ref == 1 or ref == 2 or ref == 3:
    print("Your refreshment will be here in 5 minutes.")
else:
    print("No refreshment selected.")

# Step 5: Customer details
print("\nEnter your details:")
name = input("Name: ")
phone = input("Phone Number: ")
address = input("Address: ")

# Step 6: Final Bill
print("\n----- FINAL BILL -----")
print("Customer Name:", name)
print("Phone Number:", phone)
print("Address:", address)
print("Car Purchased:", car_name)
print("Price: $", price)
print("Payment Method:", payment_method)
print("-----------------------------")
print("Your car will be delivered in 48 hours. Thank you!")
