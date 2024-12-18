class ATM:
    def __init__(self):
        self.pin=None
        self.balance=0
    
    def main(self):
        book_list = []  # List to store book objects
        while True:
            choice = input("1) Create Pin \n 2)Change Pin \n 3)Check Balance \n 4)Withdraw \n 5)Deposit \n 6)Exit")
            if choice == '1':
                create_pin()
            elif choice == '2':
                change_pin()
            elif choice == '3':
                check_bal()
            elif choice=='4':
                withdraw()
            elif choice=='5':
                deposit()
            elif choice=='6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")

    def create_pin():
        if self.pin is not None:
            print("Pin is already created")
        else:
            self.pin=input("Create Your PIN: ")
            print("PIN created succesfully")

    def change_pin():
        if self.pin is not None:
            print("No PIN set")
        else:
            current_pin=input("Enter Your Current Pin: ")
            if current_pin==self.pin:
                new_pin=input("Enter New Pin: ")
                self.pin=new_pin
                print("PIN Changed Succesfully")
            else:
                print("Your Current pin is Wrong !!!!!!!")

    def check_bal():
        if self.pin is not None:
            print("No PIN set")
        else:
            current_pin=input("Enter Your Current Pin: ")
            if current_pin==self.pin:
                print("Your Current Balance is: ",self.balance)
            else:
                print("Entered Pin is Incorrect !!!!!!!")

    def withdraw():
        if self.pin is not None:
            print("No PIN set")
        else:
            current_pin=input("Enter Your Current Pin: ")
            if current_pin==self.pin:
                amount=float(input("Enter Amount to Withdraw: "))
                if amount>self.balace:
                    print("Insufficient Balance !!!!")
                else:
                    self.balance-=amount
                    print(amount," Withdrwal Successfully")
                    print("Your Updated Balance is: ",self.balance)

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
                
atm =ATM()
atm.main()
