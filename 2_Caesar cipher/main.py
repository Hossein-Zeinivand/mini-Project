alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encoded_message = ""
is_matched = False
is_running = True

while is_running:
    action = input("Do you want to encode or decode? ").lower()
    user_message = input("Enter your message: ").lower()
    shift_index = int(input("Enter the shift value: ")) % 26

    for letter in user_message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            if action == "encode":
                current_index += shift_index
            if action == "decode":
                current_index -= shift_index
            encoded_message += alphabet[current_index]
        else:
            encoded_message += letter
        is_matched = True
    
    if is_matched:
        print(f"Your processed message is: {encoded_message}")
        encoded_message = ""

    continue_prompt = input("Do you want to continue? (y/n): ")
    if continue_prompt == "n":
        is_running = False
