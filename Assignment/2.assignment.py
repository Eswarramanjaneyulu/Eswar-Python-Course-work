#Assignment 2: WhatsApp Chat Data Analysis
def input_messages():
    num_messages = int(input("Enter the number of messages: "))
    messages = []
    for _ in range(num_messages):
        entry = input()
        name, message = entry.split(":", 1)
        messages.append((name.strip(), message.strip()))
    return messages

def count_messages(messages):
    count = {}
    for name, _ in messages:
        count[name] = count.get(name, 0) + 1
    print("\nMessage count by user:")
    for name in count:
        print(f"{name}: {count[name]} messages")

def display_messages(messages):
    print("\nAll messages:")
    for name, message in messages:
        print(f"{name}: {message}")

def most_active_user(messages):
    count = {}
    for name, _ in messages:
        count[name] = count.get(name, 0) + 1
    most_active = max(count, key=count.get)
    print(f"\nMost active user: {most_active} ({count[most_active]} messages)")

def word_count(messages):
    words = {}
    for name, message in messages:
        words[name] = words.get(name, 0) + len(message.split())
    print("\nWord count by user:")
    for name in words:
        print(f"{name}: {words[name]} words")

def show_menu():
    print("\nChoose an analysis option:")
    print("1. Count messages by each user")
    print("2. Display all messages")
    print("3. Find most active user")
    print("4. Count total words by each user")
    print("5. Exit")

def main():
    messages = input_messages()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            count_messages(messages)
        elif choice == "2":
            display_messages(messages)
        elif choice == "3":
            most_active_user(messages)
        elif choice == "4":
            word_count(messages)
        elif choice == "5":
            print("Exiting analysis. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
    