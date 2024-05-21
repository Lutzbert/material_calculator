from pprint import pprint

# Check if the input is not empty

def input_with_prompt(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Error: Input cannot be empty. Please enter a valid input.")

# Inputs ------------------------------------------------------------

while True:
    try:
        game = input_with_prompt("Which game do you want to farm for?\n")
        character = input_with_prompt("Which character do you want to farm for?\n")
        num_materials = int(input_with_prompt("How many different materials do you want to farm?\n"))

        if num_materials <= 0:
            raise ValueError("The number of materials must be greater than 0.")

        break  # If all inputs are successful, exit the loop

    except ValueError as e:
        print(f"Error: {e}. Please enter the information again.")

# Materials array inputs ---------------------------------------------------
materials_array = []

for i in range(num_materials):
    print(f"\nInput for Material {i+1}:\n")
    material_name = input_with_prompt("Enter the name of the material:\n")

    while True:
        try:
            material_amount_input = input_with_prompt("Enter the drop amount for the material:\n")
            material_amount = int(material_amount_input)
            if material_amount <= 0:
                raise ValueError("The amount of materials must be greater than 0.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")

    while True:
        drop_chance_input = input_with_prompt("What is the drop chance for the material (percentage as a number)?\n")
        try:
            drop_chance = float(drop_chance_input)
            if not (0 <= drop_chance <= 100):
                raise ValueError("The drop chance must be between 0 and 100.")
            break
        except ValueError:
            print("Invalid input. Please enter a decimal number between 0 and 100.")

    material_location = input_with_prompt("Enter the location for the material:\n")

    material_info = [material_name, material_amount, drop_chance, material_location]
    materials_array.append(material_info)

    correction = input(f"Do you want to change any of the inputs for Material {i+1}? (yes / no)\n")
    if correction.lower() != 'no':
        print(f"Correction for Material {i+1} executed.")

print("The materials you want to farm are: ", materials_array)

# Calculation -----------------------------------------------------------

# Write the entire array to a file
with open(f"{game}_{character}_data.txt", 'w') as file:
    
    file.write("\nMinimum and maximum repetitions:\n\n")

    # Calculation and writing for each material in the array
    for i, material in enumerate(materials_array):
        material_name = material[0]
        material_amount = material[1]
        drop_chance_percent = material[2]
        drop_chance = drop_chance_percent / 100
        material_location = material[3]
        
        target_amount = int(input(f"Please enter the target amount for Material {i+1} ({material_name}):\n"))

        min_repetitions = int(target_amount / material_amount)
        max_repetitions = int(target_amount / (material_amount * drop_chance))

        # if the result should be less than 1
        if min_repetitions < 1:
            min_repetitions = 1
        if max_repetitions < 1:
            max_repetitions = 1

        # Write to the file
        file.write(f"The material: {material_name}\n")
        file.write(f"with a target amount of: {target_amount},\n")
        file.write(f"a drop amount of: {material_amount} and a drop chance of: {drop_chance * 100}%\n")
        file.write(f"should be at the location {material_location}\n")
        file.write(f"Minimum repetitions: {min_repetitions}\n")
        file.write(f"Maximum repetitions: {max_repetitions}\n")
        file.write("required\n")
        file.write("---------\n")

print(f"Data has been saved in '{game}_{character}_data.txt'.")
