import Assignment4

def menu():
    print('--------Programmes Menu--------')
    print("1. Check Armstrong Number")
    print("2. Find GCD of Two Numbers")
    print("3. Custom Sort List")
    print("4. Reverse a Number")
    print("5. Sum of Digits")
    print("6. Count Words in Sentence")
    print("7. Convert to Title Case")
    print("0. Exit")

    print("-------------------------------")

def main():
    while True:
        menu()
       
        choice = int(input("Enter your choice: "))
       
        if choice == 0:
            print("Thank You")
            break
        elif choice == 1:
            print("Armstrong:", Assignment4.armstrong())   
        elif choice == 2:
            print("GCD:", Assignment4.gcd())
        elif choice == 3:
            print("Sorted list:", Assignment4.custom_sort())

        elif choice == 4:
            print("Reversed:", Assignment4.reverse_number())
        elif choice == 5:
            print("Sum of digits:", Assignment4.sum_of_digit())
        elif choice == 6:
            print("Word count:", Assignment4.count_word())
        elif choice == 7:
            print("Title case:", Assignment4.title_case())      
        else:
            print("Invalid choice! Please try again.\n")


main()