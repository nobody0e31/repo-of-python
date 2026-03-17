def check_numbers():
    """
    Continuously inputs numbers from the user and prints 
    if they are positive or negative until the user enters "Quit".
    """
    print("Enter a number to check if it's positive or negative.")
    print("Type 'Quit' (case-insensitive) to exit the program.")
    
    while True:
        user_input = input("Enter a number or 'Quit': ")
        
        if user_input.lower() == 'quit':
            print("Exiting program. Goodbye!")
            break  # Exit the while loop
            
        try:
            # Attempt to convert the input to a floating-point number
            number = float(user_input)
            
            if number > 0:
                print(f"{number} is positive.")
            elif number < 0:
                print(f"{number} is negative.")
            else:
                # Handle the case where the number is zero
                print(f"{number} is neither positive nor negative (it is zero).")
                
        except ValueError:
            # Handle cases where the input is not a valid number
            print(f"Invalid input: '{user_input}'. Please enter a valid number or 'Quit'.")

# To run the program, call the function:
# check_numbers()
