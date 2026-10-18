# Secure Transaction Records using Tuple

# Transaction details
transaction = (
    "TXN1001",      # Transaction ID
    "Inzamamul Haque Qureshi",        # Customer Name
    25000.00,       # Amount
    "Deposit",      # Transaction Type
    "15-07-2026"    # Date
)

# Display transaction details
print("Transaction Record")
print("Transaction ID :", transaction[0])
print("Customer Name  :", transaction[1])
print("Amount         :", transaction[2])
print("Transaction Type :", transaction[3])
print("Date           :", transaction[4])
