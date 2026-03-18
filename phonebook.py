phonebook = [

]

while True:
    command = input("Enter command (add/delete/search/show/exit):")
    if command == "exit":
        break
    elif command == "add":
        name = input("Enter name:")
        phone = input("Enter phone number:")
        phonebook.append({"name":name, "phone":phone})
