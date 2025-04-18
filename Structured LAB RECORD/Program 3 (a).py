def display_menu():
    print("\nChoose an operation:")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Find element")
    print("4. Sort the list")
    print("5. Reverse the list")
    print("6. Display the list")
    print("7. Exit")

def insert_element(lst):
    element = input("Enter the element to insert: ")
    lst.append(element)
    print(f"{element} has been added to the list.")

def delete_element(lst):
    element = input("Enter the element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"{element} has been removed from the list.")
    else:
        print(f"{element} not found in the list.")

def find_element(lst):
    element = input("Enter the element to find: ")
    if element in lst:
        print(f"{element} is present in the list.")
    else:
        print(f"{element} is not in the list.")

def sort_list(lst):
    lst.sort()
    print("The list has been sorted.")

def reverse_list(lst):
    lst.reverse()
    print("The list has been reversed.")

def main():
    lst = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            insert_element(lst)
        elif choice == "2":
            delete_element(lst)
        elif choice == "3":
            find_element(lst)
        elif choice == "4":
            sort_list(lst)
        elif choice == "5":
            reverse_list(lst)
        elif choice == "6":
            print("Current list:", lst)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
