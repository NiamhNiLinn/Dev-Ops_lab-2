# Basic program to compute the average of a set of numbers
numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

average = sum(numbers) / count

print(f"The average of the numbers is: {average}")
