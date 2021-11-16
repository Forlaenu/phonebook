def lookup_entry(user_input_name, phonebook_dictionary):
        if user_input_name in phonebook_dictionary:
            phone_number_for_entry = phonebook_dictionary[user_input_name]
            return f"--Found entry for {user_input_name}: {phone_number_for_entry}--"   
        else:
            # In case no entry exists for that name
            return f"--No entry found for {user_input_name}--"