class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0

    def main(self):
        while True:
            print("""
            1) Create Pin
            2) Change Pin
            3) Check Balance
            4) Withdraw
            5) Deposit
            6) Exit
            """)
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                self.create_pin()
            elif choice == 2:
                self.change_pin()
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                self.withdraw()
            elif choice == 5:
                self.deposit()
            elif choice == 6:
                print("Exiting to ATM")
                break
            else:
                print("Invalid choice, Please try again!")

    def create_pin(self):
        if self.pin is not None:
            print("Pin is already created.")
        else:
            self.pin = input("Create your PIN: ")
            print("Pin created successfully!")

    def change_pin(self):
        if self.pin is None:
            print("No PIN set. Please create a PIN first.")
        else:
            current_pin = input("Enter your current PIN: ")
            if current_pin == self.pin:
                new_pin = input("Enter your new PIN: ")
                self.pin = new_pin
                print("Pin changed successfully!")
            else:
                print("Incorrect PIN!")

    def check_balance(self):
        if self.pin is None:
            print("Please set a PIN first.")
        else:
            pin_input = input("Enter your PIN to check balance: ")
            if pin_input == self.pin:
                print(f"Your current balance is:{self.balance}")
            else:
                print("Incorrect PIN!")

    def withdraw(self):
        if self.pin is None:
            print("Please set a PIN first.")
        else:
            pin_input = input("Enter your PIN to withdraw: ")
            if pin_input == self.pin:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > self.balance:
                    print("Insufficient balance!")
                else:
                    self.balance -= amount
                    print(f"Successfully withdrew {amount}. Your new balance is: {self.balance}")
            else:
                print("Incorrect PIN!")

    def deposit(self):
        if self.pin is None:
            print("Please set a PIN first.")
        else:
            pin_input = input("Enter your PIN to deposit: ")
            if pin_input == self.pin:
                amount = float(input("Enter amount to deposit: $"))
                self.balance += amount
                print(f"Successfully deposited {amount}. Your new balance is: {self.balance}")
            else:
                print("Incorrect PIN!")

# Create an instance of the ATM class and run the main method
atm = Atm()
atm.main()
