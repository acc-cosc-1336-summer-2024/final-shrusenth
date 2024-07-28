def main():
    numbers = []

    print("Enter five numbers:")
    for _ in range(5):
        number = float(input(f"Number {_ + 1}: "))
        numbers.append(number)

    lowest_number = min(numbers)
    highest_number = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Lowest number: {lowest_number}")
    print(f"Highest number: {highest_number}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

if __name__ == "__main__":
    main()
