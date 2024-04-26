
def perform_union(set1, set2):
    return set1.union(set2)

def perform_intersection(set1, set2):
    return set1.intersection(set2)

def perform_difference(set1, set2):
    return set1.difference(set2)

def display_sets():
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Set 3:", set3)

def display_result(operation, result):
    print(f"\nThe {operation} result is: {result}\n")

if __name__ == "__main__":
    set1 = {"red", "blue", "green", "yellow"}
    set2 = {"blue", "orange", "purple", "yellow"}
    set3 = {"green", "purple", "pink", "orange"}

    option = 0
    while option != 4:
        print("\nOptions:")
        print("1 - Perform union between two sets of colors")
        print("2 - Perform intersection between two sets of colors")
        print("3 - Perform difference between two sets of colors")
        print("4 - Exit the program")

        option = int(input("Enter the number of the desired option: "))

        if option == 1:
            display_sets()
            set_choice1 = int(input("Enter the number of the first set (1, 2, or 3): "))
            set_choice2 = int(input("Enter the number of the second set (1, 2, or 3): "))
            result = perform_union(globals()[f"set{set_choice1}"], globals()[f"set{set_choice2}"])
            display_result("union", result)
        elif option == 2:
            display_sets()
            set_choice1 = int(input("Enter the number of the first set (1, 2, or 3): "))
            set_choice2 = int(input("Enter the number of the second set (1, 2, or 3): "))
            result = perform_intersection(globals()[f"set{set_choice1}"], globals()[f"set{set_choice2}"])
            display_result("intersection", result)
        elif option == 3:
            display_sets()
            set_choice1 = int(input("Enter the number of the first set (1, 2, or 3): "))
            set_choice2 = int(input("Enter the number of the second set (1, 2, or 3): "))
            result = perform_difference(globals()[f"set{set_choice1}"], globals()[f"set{set_choice2}"])
            display_result("difference", result)
        elif option == 4:
            print("Exiting the program....")
        else:
            print("\nInvalid option. Please choose a valid option.")
