principal = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (%): "))
time = int(input("Enter the loan tenure (in years): "))

monthly_rate = annual_rate / (12 * 100)
months = time * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", round(emi, 2))
