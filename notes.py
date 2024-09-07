# TODO Save Password
"""
The buttons 'do' the command, with the command function. That means it's the function (do) we
need to code

When user clicks 'Add', the website, email/username and password is stored on a txt file as
website: {} Email: {} Password: {}
Each entry on a new line, appended to the existing file with the other account details.
Once the button is pressed, clear all information

To do this:

1. Create empty dictionary
2. Get information from each entry
3. Append information into a different key, and append into dictionary.
Website:
Email:
Password:






letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

letters_list = [char for char in password_list]
symbols_list = [char for char in password_list]
numbers_list = [char for char in password_list]

password_list += letters_list + symbols_list + numbers_list

random.shuffle(password_list)

final_password = ""
for char in password_list:
  final_password += char

print(f"Your password is: {final_password}")
"""
