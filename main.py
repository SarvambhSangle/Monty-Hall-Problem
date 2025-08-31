import random

def monty_hall_simulation(num_doors, num_simulations):
    """
    Simulates the Monty Hall problem.

    Args:
        num_doors (int): The total number of doors.
        num_simulations (int): The number of times to run the simulation.

    Returns:
        A tuple containing the win percentage for switching and staying.
    """
    if num_doors < 3:
        raise ValueError("Number of doors must be 3 or more.")

    wins_staying = 0
    wins_switching = 0

    for _ in range(num_simulations):
        # Place the prize behind a random door
        prize_door = random.randint(1, num_doors)

        # Contestant makes an initial choice
        initial_choice = random.randint(1, num_doors)

        # The host opens one door without the prize and not the contestant's choice.
        # This is the tricky part, especially with more than 3 doors.
        
        # All doors except the prize door and the contestant's choice
        doors_to_open = [d for d in range(1, num_doors + 1) if d != prize_door and d != initial_choice]
        
        # For the 3-door case, the host only has one choice.
        # For more than 3 doors, the host opens one of the empty doors.
        # This logic assumes the host only opens ONE door, as per the prompt.
        if num_doors > 3:
            door_opened_by_host = random.choice(doors_to_open)
        else:
            door_opened_by_host = doors_to_open[0]

        # Scenario 1: Stay with the initial choice
        if initial_choice == prize_door:
            wins_staying += 1

        # Scenario 2: Switch to the other unopened door
        # The new choice is the door that is not the initial choice and not the door the host opened.
        all_doors = set(range(1, num_doors + 1))
        unopened_doors = list(all_doors - {initial_choice, door_opened_by_host})
        
        # If there are multiple unopened doors to switch to (e.g., 4+ doors),
        # the contestant picks one at random.
        if unopened_doors:
            switched_choice = random.choice(unopened_doors)
            if switched_choice == prize_door:
                wins_switching += 1

    percent_staying = (wins_staying / num_simulations) * 100
    percent_switching = (wins_switching / num_simulations) * 100

    return percent_staying, percent_switching

# --- User input section ---
try:
    num_doors = int(input("Enter the number of doors (3 or more): "))
    num_simulations = int(input("Enter the number of simulations to run (e.g., 10000): "))

    stay_percent, switch_percent = monty_hall_simulation(num_doors, num_simulations)

    print(f"\nResults based on {num_simulations} simulations with {num_doors} doors:")
    print(f"Percentage of wins by staying with the initial choice: {stay_percent:.2f}%")
    print(f"Percentage of wins by switching doors: {switch_percent:.2f}%")
    
    # Simple check to see which strategy is better
    if switch_percent > stay_percent:
        print("\nConclusion: It is better to switch doors. ")
    else:
        print("\nConclusion: It is better to stay with your initial choice. ")

except ValueError as e:
    print(f"Error: {e}. Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")