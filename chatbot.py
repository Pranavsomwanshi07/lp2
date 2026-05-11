# # Simple Rule-Based Chatbot

# print("🤖 Chatbot: Hello! Welcome to our Customer Support System")
# print("Type 'exit' to end chat\n")

# while True:
#     user = input("You: ").lower()

#     if user == "hello" or user == "hi":
#         print("🤖 Chatbot: Hello! How can I help you?")

#     elif "order" in user:
#         print("🤖 Chatbot: Please provide your order ID.")

#     elif "status" in user:
#         print("🤖 Chatbot: Your order is being processed and will be delivered soon.")

#     elif "price" in user or "cost" in user:
#         print("🤖 Chatbot: Please tell me the product name.")

#     elif "complaint" in user:
#         print("🤖 Chatbot: We are sorry for the inconvenience. Please describe your issue.")

#     elif "bye" in user:
#         print("🤖 Chatbot: Thank you for contacting us. Have a nice day!")
#         break

#     elif user == "exit":
#         print("🤖 Chatbot: Session ended. Goodbye!")
#         break

#     else:
#         print("🤖 Chatbot: Sorry, I didn't understand that. Can you rephrase?")


# ==========================================
# FULL CUSTOMER SUPPORT CHATBOT IN PYTHON
# ==========================================

print("===================================")
print(" 🤖 WELCOME TO CUSTOMER CHATBOT ")
print("===================================")

name = input("Enter your name: ")

print("\nHello", name + "!")
print("How can I help you today?")
print("-----------------------------------")
print("You can ask about:")
print("1. Products")
print("2. Order Status")
print("3. Prices")
print("4. Complaint")
print("5. Delivery")
print("6. Payment")
print("7. Contact")
print("Type 'menu' to see options again")
print("Type 'exit' to close chatbot")
print("-----------------------------------")

while True:

    user = input("\nYou: ").lower()

    # Greeting
    if user == "hi" or user == "hello":
        print("🤖 Chatbot: Hello", name + "! Welcome back.")

    # Product Information
    elif "product" in user:
        print("🤖 Chatbot: We sell:")
        print("1. Mobile Phones")
        print("2. Laptops")
        print("3. Smart Watches")
        print("4. Earbuds")

    # Mobile Price
    elif "moMobile" in user:
        print("🤖 Chatbot: Mobile phones start from ₹10,000.")

    # Laptop Price
    elif "laptop" in user:
        print("🤖 Chatbot: Laptops start from ₹35,000.")

    # Smart Watch
    elif "watch" in user:
        print("🤖 Chatbot: Smart watches start from ₹2,000.")

    # Earbuds
    elif "earbuds" in user:
        print("🤖 Chatbot: Earbuds start from ₹1,500.")

    # Order Status
    elif "order" in user:
        order_id = input("🤖 Chatbot: Enter your Order ID: ")

        if order_id == "101":
            print("🤖 Chatbot: Your order has been shipped.")

        elif order_id == "102":
            print("🤖 Chatbot: Your order is out for delivery.")

        elif order_id == "103":
            print("🤖 Chatbot: Your order has been delivered.")

        else:
            print("🤖 Chatbot: Invalid Order ID.")

    # Delivery
    elif "delivery" in user:
        print("🤖 Chatbot: Delivery usually takes 3-5 business days.")

    # Payment
    elif "payment" in user:
        print("🤖 Chatbot: We accept:")
        print("- UPI")
        print("- Debit Card")
        print("- Credit Card")
        print("- Cash on Delivery")

    # Complaint
    elif "complaint" in user:
        complaint = input("🤖 Chatbot: Please describe your issue: ")
        print("🤖 Chatbot: Your complaint has been registered.")
        print("🤖 Chatbot: Complaint Details ->", complaint)

    # Contact Information
    elif "contact" in user:
        print("🤖 Chatbot: Customer Care Number: 9876543210")
        print("🤖 Chatbot: Email: support@gmail.com")

    # Help Menu
    elif user == "menu":
        print("-----------------------------------")
        print("Available Services:")
        print("1. Products")
        print("2. Order Status")
        print("3. Prices")
        print("4. Complaint")
        print("5. Delivery")
        print("6. Payment")
        print("7. Contact")
        print("-----------------------------------")

    # Thank You
    elif "thanks" in user or "thank you" in user:
        print("🤖 Chatbot: You're welcome", name + "!")

    # Exit
    elif user == "exit" or user == "bye":
        print("🤖 Chatbot: Thank you for visiting.")
        print("🤖 Chatbot: Have a great day", name + "!")
        break

    # Unknown Input
    else:
        print("🤖 Chatbot: Sorry! I did not understand.")
        print("🤖 Chatbot: Type 'menu' to see available options.")
