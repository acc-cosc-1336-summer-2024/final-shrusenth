from question_b import stock_purchase_history

def main():
    while True:
        print("\nMenu:")
        print("1. Display stock purchase history")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
