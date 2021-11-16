from lookup_entry import lookup_entry
from set_entry import set_entry
app_running = True
phonebook_dictionary = {}
#The phonebook dictionary
main_menu = """1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit""" 

while app_running:
    def delete_entry():
        print("\nDeleting entry")
        user_input_name = input("Name: ")
        #checking that the entry exists in the phonebook
        if user_input_name in phonebook_dictionary:
            #entry found, deleting
            del phonebook_dictionary[user_input_name]
            print(f"Deleted entry for {user_input_name}")    
        else:
            # In case no entry exists for that name
            print(f"No entry found for {user_input_name}")
        #printing line break
        print()

    def list_entries():
        print("\nListing Entries")
        #iterate thru the keys in phonebook
        for key,value in phonebook_dictionary.items():
            print(f"Found entry for {key}: {value}")
        #printing line break
        print()
    
        # MAIN LOOP MENU
    print("Electronic Phone Book")
    print("=====================")
    print(main_menu)
    #Get user input
    menu_input = input("What do you want to do (1-5)?: ")
    if menu_input == '1':
        print("\nLooking up phonebook entry")
        #Getting the info we need to pass to lookup_entry
        user_input_name = input("Name: ")
        #printing the RETURN of function lookup_entry
        print(lookup_entry(user_input_name,phonebook_dictionary))
        #printing line break
        print()
    if menu_input == '2':
        print("\nSetting an entry")
        #Getting the info we need to pass to setup_entry
        user_input_name = input("Name: ")
        user_input_phonenumber = input("Phone Number: ")
        #printing the RETURN of function set_entry
        print(set_entry(user_input_name,user_input_phonenumber,phonebook_dictionary))
        #printing line break
        print()
    if menu_input == '3':
        delete_entry()
    if menu_input == '4':
        list_entries()
    if menu_input.lower() == '5':
        app_running = False


    # REFACTORING
    # def lookup_entry():
    #     print("\nLooking up phonebook")
    #     user_input_name = input("Name: ")
    #     if user_input_name in phonebook_dictionary:
    #         phone_number_for_entry = phonebook_dictionary[user_input_name]
    #         print(f"Found entry for {user_input_name}: {phone_number_for_entry}")    
    #     else:
    #         # In case no entry exists for that name
    #         print(f"No entry found for {user_input_name}")
    #     #printing line break
    #     print()
    
    # REFACTORING
    # def set_entry():
    #     print("\nSetting an entry")
    #     user_input_name = input("Name: ")
    #     user_input_phonenumber = input("Phone Number: ")
    #     phonebook_dictionary[user_input_name] = user_input_phonenumber
    #     # Verify entry was indeed stored using the "in" condition
    #     if user_input_name in phonebook_dictionary:
    #         print(f"Entry stored for {user_input_name}")
    #     #printing line break
    #     print()