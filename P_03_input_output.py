# ask user for name
username = input("What's your name? ")

# ask user for favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve a square the users favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f"\nHi {username}, your favourite number is {fav_num}")

# Output the results of doubling, halving and squaring their favourite integer
print(f"Double {fav_num} is {double}.")
print(f"Halve {fav_num} is {halve}.")
print(f"Square {fav_num} is {square}.")
print()
print("Have a nice day.")
