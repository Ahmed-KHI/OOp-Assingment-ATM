class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"✅ Your current balance is Rs{self.balance}")

    def deposit(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("❌ Incorrect PIN.")
            return
        if amount <= 0:
            print("❌ Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print(f"✅ Rs{amount} deposited successfully.")
        self.check_balance()

    def withdraw(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print("❌ Incorrect PIN.")
            return
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return
        self.balance -= amount
        print(f"✅ Rs{amount} withdrawn successfully.")
        self.check_balance()

    def exit(self):
        print("💳 Thank you for using the ATM. Goodbye!")
        quit()
    @staticmethod
    def display_menu():
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

# Welcome message
print("💸 Welcome to ATM CLI 🏧")
print("=" * 40)

atm = ATM()

try:
    user_pin = int(input("Enter your PIN: "))
except ValueError:
    print("❌ PIN must be a number.")
    exit()

if atm.check_pin(user_pin):
    while True:
        ATM.display_menu()
        choice = input("Enter your choice (1, 2, 3, 4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = int(input("Enter amount to deposit: "))
                atm.deposit(user_pin, amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            try:
                amount = int(input("Enter amount to withdraw: "))
                atm.withdraw(user_pin, amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            atm.exit()
        else:
            print("❌ Invalid option. Please choose 1-4.")
else:
    print("❌ Incorrect PIN. Access denied.")