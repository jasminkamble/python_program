class InsufficientBalance(Exception):
    pass


balance = 1000

try:
    amount = 1500

    if amount > balance:
        raise InsufficientBalance("Withdrawal failed: Insufficient balance.")

    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)

except InsufficientBalance as e:
    print("Exception:", e)
