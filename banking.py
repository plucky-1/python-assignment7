"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number not in accounts:
        accounts[account_number]= {"name":name,"balance":0.0, **kwargs}
        return f"account sucessfully created,your account name is: {name} ,account number: {account_number} and overdraft_limit is: {kwargs}"

    else:
        return f"oops, {account_number} already exist!"
print(create_account(222,"Aaron",overdraft_limit = 50))
print(create_account(221,"john",over_draft_limit = 100))
        
def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        return f"₦{amount} was successfully deposited into your account"

    else:
        return f"acount with {account_number} not found"
print(deposit(222,200))
print(deposit(221,100))
def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number in accounts:
        total_over_draft = accounts[account_number].get("over_draft_limit",0.0)
        total_balance = accounts[account_number]["balance"]
        
        if total_balance + total_over_draft >= amount:
            accounts[account_number]["balance"] -= amount
            return f"successfully withdrew ₦ {amount}"

        else:
            return "Insufficient funds"
    else:
        return f"oops!,{accout_number} not found!"

print(withdraw(222,30))

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    if from_acc and to_acc in accounts:
        total_balance = accounts[from_acc]["balance"]
        total_over_draft = accounts[from_acc].get("over_draft_limit",0.0)
 
        if total_balance + total_over_draft >= amount:
            accounts[from_acc]["balance"] -= amount
            accounts[to_acc]["balance"] += amount
            return f"successfully transfered ₦ {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}"
        else:
            return "Insufficient funds"
    else:
        return "either or none of the account not found!"

print(transfer(222,221,20))
