Banking System Project

📌 Overview

This project is a simple Banking System implemented in Python.
It allows users to:
	•	Create an account
	•	Deposit into checking or saving accounts
	•	Withdraw money with overdraft rules and fees
	•	Transfer money between checking and saving
	•	Automatically deactivate an account after multiple overdrafts

The goal of this project was to practice Object-Oriented Programming (OOP) concepts, error handling, and testing using unit tests.



🧩 Example Code (that I am proud of)

def withdraw_checking(self, amount: float):
    if not self.active:
        print("Account is deactivated due to multiple overdrafts.")
        return False

    if amount <= 0:
        print("Withdrawal amount must be more than 0.")
        return False

    if self.balance_checking < 0 and amount > self.max_withdraw_if_negative:
        print(f"Cannot withdraw more than ${self.max_withdraw_if_negative} when balance is negative.")
        return False

    if (self.balance_checking - amount) < self.max_overdraft_limt:
        print(f"This transaction would exceed the overdraft limit of ${self.max_overdraft_limt}.")
        return False

    balance_before = self.balance_checking
    self.balance_checking -= amount
    balance_after = self.balance_checking

    if balance_before >= 0 and balance_after < 0:
        print("Applying overdraft fee")
        self.balance_checking -= self.overedraft_fee
        self.overdraft_used += 1
        if self.overdraft_used >= self.overdrsft_attempts:
            self.deactivate()

    return True

🔹 Why I am proud of it:
This method shows how we handled business rules like overdraft fees, account deactivation, and safe withdrawals in a clean, step-by-step way.



📚 What I Learned

Through this project, I learned:
	•	How to design classes and methods using OOP principles
	•	The importance of validations and error handling
	•	How to write and run unit tests to verify functionality
	•	Team collaboration and using GitHub for version control



🚀 Future Improvements
	•	Adding a Graphical User Interface (GUI)
	•	Adding database storage instead of CSV
	•	Supporting multiple users with login


📚 Learning Resources
	•	W3Schools – Tutorials for Python
	•	Real Python – Python tutorials and best practices
	•	Python Official Documentation – Reference for Python syntax and libraries
	•	GitHub Guides – How to use Git and GitHub
	•	Stack Overflow – Troubleshooting and coding Q&A