def main_list():
    numbers = []

    print("Enter five numbers:")
    for i in range(5):
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)
    
    return numbers

def main_list_calculations(numbers):
    lowest_number = min(numbers)
    highest_number = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Lowest number: {lowest_number}")
    print(f"Highest number: {highest_number}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")
