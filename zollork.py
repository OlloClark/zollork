prompt = "..."

name = input(f"""
who are you?
{prompt}
""")

table_choice = input(f"""
Hello, {name}. Look at the table
{prompt}
""")

if table_choice.lower() === "what":
	input("I said look at the table")
elif table_choice.lower() === "look at table":
	print("there are three weapons")
else:
	input("no decision made")