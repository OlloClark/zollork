prompt = "..."
choice = 0
name = input(f"who are you? \n {prompt}")

if name:
	choice = 1

while choice == 1:
	if choice == 1:
		table_choice = input(f"Hello, {name}. Look at the table \n {prompt}")

	if table_choice.lower() == "look at table":
		choice = 2
	elif table_choice.lower() == "what?":
		print("What do you mean 'what'? I said look at the table")
	elif table_choice.lower() == "I refuse":
		print("you cannot refuse")
	else:
		print("..............")

while choice == 2:
	if choice == 2:
		weapon_choice = input(f"time to choose a weapon! \n {prompt}")
		print(f"you chose {weapon_choice}. Nice")