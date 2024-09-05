name : str = input("Enter your name: ")
count = ["first", "second", "third"]

numbers = []

for i in range(0,3): 
    number = int(input(f"Enter your {count[i]} favorite number: "))
    numbers.append(number)

print(f"\nHello, {name}! Let's explore your favorite numbers:")

even_odd_info = []
for num in numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even"))
    else:
        even_odd_info.append((num, "odd"))

for num, status in even_odd_info:
    print(f"The number {num} is {status}.")

print("\nHere are your numbers and their squares:")
for num in numbers:
    square_tuple = (num, num ** 2)
    print(f"The number {num} and its square: {square_tuple}")

total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

is_prime = True
if total_sum < 2:
    is_prime = False
else:
    for i in range(2, int(total_sum ** 0.5) + 1):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"The number {total_sum} is not a prime number.")
