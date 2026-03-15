# --- MAIN PROGRAM ---

while True: # 1. Tady začíná nekonečná smyčka
    # Data collection
    user_name = input("\nEnter your name: ")
    goal = input("What is your main goal? ")
    target_date = input("When do you want to achieve it? ")
    steps_input = input("Enter steps separated by commas: ")

    step_list = [s.strip() for s in steps_input.split(",") if s.strip() != ""]

    if len(step_list) == 0:
        print("\n❌ Error: You must enter at least one step.")
    else:
        created_file = create_action_plan(user_name, goal, step_list, target_date)
        os.startfile(created_file)

    # 2. Tady se zeptáme, jestli chce uživatel pokračovat
    again = input("\nDo you want to create another plan? (yes/no): ").lower().strip()
    
    if again != "yes": # Pokud napíše cokoliv jiného než 'yes'
        print("Thank you for using Global Task Architect. Goodbye!")
        break # 3. Tímto příkazem smyčku 'rozbijeme' a program skončí
