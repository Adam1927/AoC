code_counter = 0
current_dial_position = 50 
encrypted_file = open('2025/Dec1/dec1Input.txt', 'r')
file_lines = encrypted_file.readlines()
encrypted_file.close()

for line in file_lines:
    letter = ""
    number_string = ""
    for character in line.replace("\n", ""):
        if character.isdigit():
            number_string += character
        else:
            letter = character
    number = int(number_string)

    if letter == "R":
        code_counter += (number + current_dial_position)//100
        current_dial_position = (number + current_dial_position) % 100
    else:
        if current_dial_position - (number % 100) <= 0 and current_dial_position != 0:
            code_counter += 1
        code_counter += number//100
        current_dial_position = (current_dial_position - number) % 100
    
    print(code_counter)
    print(current_dial_position)
    print("----------")

print("----------")
print("The code is: " + str(code_counter))