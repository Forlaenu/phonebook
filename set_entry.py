def set_entry(user_input_name,user_input_phonenumber, phonebook_dictionary):
    phonebook_dictionary[user_input_name] = user_input_phonenumber
    # Verify entry was indeed stored using the "in" condition
    if user_input_name in phonebook_dictionary:
        return f"--Entry stored for {user_input_name}--"
