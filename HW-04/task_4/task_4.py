def parse_input(user_input):
    """
    Розбиває введений рядок на команду та аргументи.
    Повертає кортеж (command, args), де command – рядок команди (у нижньому регістрі),
    а args – список аргументів.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    """
    Додає контакт до словника contacts.
    args має містити ім'я та номер телефону.
    """
    if len(args) < 2:
        return "Invalid format for add. Usage: add <name> <phone>"
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    args має містити ім'я контакту та новий номер.
    """
    if len(args) < 2:
        return "Invalid format for change. Usage: change <name> <new_phone>"
    name, new_phone = args[0], args[1]
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone(args, contacts):
    """
    Повертає номер телефону для заданого контакту.
    """
    if len(args) < 1:
        return "Invalid format for phone. Usage: phone <name>"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."

def show_all(contacts):
    """
    Повертає рядок з усіма контактами та їх номерами, або повідомлення,
    якщо контактів немає.
    """
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
