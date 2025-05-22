# ATM Withdrawal Program 

# Predefined account details
correct_password = "2002"
account_balance = 5000.00  # Initial account balance

# Password verification
user_password = input("Enter your 4-digit PIN: ")

if user_password != correct_password:
    print("Incorrect password. Access denied.")
else:
    # Password is correct, proceed with withdrawal
    print("\nWelcome to ATM Service")
    withdrawal_amount_str = input("Enter amount to withdraw: ")
    
    # Validate numeric input 
    if (withdrawal_amount_str.count('.') > 1 or  # Check for multiple decimals
        not withdrawal_amount_str.replace('.', '', 1).isdigit()):  # Check remaining characters
        print("Invalid input. Please enter numbers only.")
    else:
        withdrawal_amount = float(withdrawal_amount_str)
        
        # Validate withdrawal amount
        if withdrawal_amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif withdrawal_amount > account_balance:
            print("Insufficient funds. Your balance is:", account_balance)
        else:
            # Process withdrawal
            account_balance -= withdrawal_amount
            print("\nWithdrawal successful!")
            print("Amount withdrawn:", withdrawal_amount)
            print("Remaining balance:", account_balance)