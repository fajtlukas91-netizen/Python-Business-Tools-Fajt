import os
from datetime import datetime

def create_action_plan(name, main_goal, steps, deadline):
    """
    This function takes the data and creates a professional output 
    both to the console and to a text file.
    """
    # 1. Console Output for immediate feedback
    current_time = datetime.now()
    created_at = current_time.strftime("%d.%m.%Y %H:%M")

    print(f"\n" + "="*40)
    print(f"ACTION PLAN FOR: {name.upper()}")
    print(f"CREATED AT: {created_at}")
    print(f"MAIN GOAL: {main_goal}")
    print(f"DEADLINE: {deadline}")
    print("="*40)
    
    # 2. File output
    file_name = f"plan_{name.lower()}.txt"
    
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"ACTION PLAN RESULT - {name.upper()}\n")
        file.write(f"Created on: {created_at}\n")
        file.write(f"Main Goal: {main_goal}\n")
        file.write(f"Deadline: {deadline}\n")
        file.write("-" * 40 + "\n")
        
        for i, step in enumerate(steps, 1):
            line = f"{i}. [ ] {step}"
            print(line)               # Display in console
            file.write(line + "\n")   # Save to file
            
    print("="*40)
    print(f"✅ DONE! Your plan is saved in: {file_name}")
    return file_name

# --- MAIN PROGRAM ---

# Data collection (Inputs)
user_name = input("Enter your name: ")
goal = input("What is your main goal? ")
target_date = input("When do you want to achieve it? (e.g., Dec 31st): ")
steps_input = input("Enter steps separated by commas (Step 1, Step 2...): ")

# Data cleaning
step_list = [s.strip() for s in steps_input.split(",") if s.strip() != ""]

# Validation
if len(step_list) == 0:
    print("\n❌ Error: You must enter at least one step to create a plan.")
else:
    # Run the function
    created_file = create_action_plan(user_name, goal, step_list, target_date)
    
    # Auto-open the file in Windows
    os.startfile(created_file)
