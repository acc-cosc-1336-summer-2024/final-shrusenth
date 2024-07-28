def create_multiplication_table():
    table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(' '.join(map(str, row)))

def user_menu():
    while True:
        choice = input("Would you like to create a multiplication table? (type 'yes' or no')").strip().lower()
        if choice == 'yes':
            table = create_multiplication_table()
            display_multiplication_table(table)
        elif choice == 'no':
            break
        else:
            print("Invalid input.")
