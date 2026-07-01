back_stack = []
forward_stack = []
current = "Home"

while True:
    print("\nCurrent Location:", current)
    print("1. Visit New Place")
    print("2. Back")
    print("3. Forward")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        place = input("Enter new place: ")
        back_stack.append(current)
        current = place
        forward_stack.clear()
        print("Moved to", current)

    elif choice == "2":
        if len(back_stack) == 0:
            print("No previous location.")
        else:
            forward_stack.append(current)
            current = back_stack.pop()
            print("Moved Back to", current)

    elif choice == "3":
        if len(forward_stack) == 0:
            print("No forward location.")
        else:
            back_stack.append(current)
            current = forward_stack.pop()
            print("Moved Forward to", current)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")