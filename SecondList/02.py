def add_gps_point():
    latitude = float(input("Enter the latitude of the GPS point: "))
    longitude = float(input("Enter the longitude of the GPS point: "))
    gps_point = (latitude, longitude)
    route.append(gps_point)
    print(f"\nThe GPS point {gps_point} has been added to the route.\n")

def remove_gps_point():
    if len(route) == 0:
        print("\nThe route is empty. There are no GPS points to remove.\n")
        return

    print("\nCurrent route:")
    display_route()

    index = int(input("\nEnter the index of the GPS point to remove: "))
    if index < 0 or index >= len(route):
        print("\nInvalid index. Please enter a valid index.\n")
        return

    removed_point = route.pop(index)
    print(f"\nThe GPS point {removed_point} has been removed from the route.\n")

def display_route():
    for i, gps_point in enumerate(route):
        print(f"{i}: {gps_point}")

    
if __name__ == "__main__":
    route = []
    option = 0
    while option != 4:
        print("\nOptions:")
        print("1 - Add GPS point to the route")
        print("2 - Remove GPS point from the route")
        print("3 - Display current route")
        print("4 - Exit the program")

        option = int(input("Enter the number of the desired option: "))

        if option == 1:
            add_gps_point()
        elif option == 2:
            remove_gps_point()
        elif option == 3:
            print("Current route:")
            display_route()
        elif option == 4:
            print("Exiting the program...")
        else:
            print("\nInvalid option. Please choose a valid option.")

