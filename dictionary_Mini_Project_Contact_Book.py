# 1. Project features
# - Add a new contact
# - View all contacts
# - Search for a contact
# - Update a phone number
# - Delete a contact
# - Exit the program
# We'll store each person's name as a dictionary key and their details in a nested dictionary.



contacts = {}

while True:
    print('\n========== Contact App ==========')
    print('1. Add New Contact')
    print('2. Search Contact')
    print('3. Delete Contact')
    print('4. Update Contact')
    print('5. View All Contacts')
    print('6. Exit')

    choice = int(input('Enter your Choice: '))

    if choice == 1:
        mobno = int(input('Enter New Mobno: '))

        if mobno in contacts:
            print('Contact Already Exists!')
        else:
            name = input('Enter Username: ')
            contacts[mobno] = name
            print('Contact Added Successfully!')
            print(contacts)

    elif choice == 2:
        mobno = int(input('Enter Mobile Number to Search: '))

        if mobno in contacts:
            print('Username:', contacts[mobno])
        else:
            print('Contact Not Found!')

    elif choice == 3:
        mobno = int(input('Enter Mobile Number to Delete: '))

        if mobno in contacts:
            contacts.pop(mobno)
            print('Contact Deleted Successfully!')
        else:
            print('Contact Not Found!')

    elif choice == 4:
        mobno = int(input('Enter Mobile Number to Update: '))

        if mobno in contacts:
            name = input('Enter New Username: ')
            contacts[mobno] = name
            print('Contact Updated Successfully!')
        else:
            print('Contact Not Found!')

    elif choice == 5:
        if contacts:
            print('\nAll Contacts:')
            for mobno, name in contacts.items():
                print('Mobile Number:', mobno, '| Username:', name)
        else:
            print('No Contacts Available!')

    elif choice == 6:
        print('Thank You for Using Contact App!')
        break

    else:
        print('Invalid Choice! Please Select 1 to 6.')
