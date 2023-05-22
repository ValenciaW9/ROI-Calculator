class RentalPropertyCalculator:
    def __init__(self, purchase_price, monthly_rent, monthly_expenses):
        self.purchase_price = purchase_price
        self.monthly_rent = monthly_rent
        self.monthly_expenses = monthly_expenses

    def calculate_roi(self):
        annual_rent = self.monthly_rent * 12
        net_income = annual_rent - (self.monthly_expenses * 12)
        roi = (net_income / self.purchase_price) * 100
        return roi

# Create an instance of RentalPropertyCalculator
calculator = RentalPropertyCalculator(400000, 3000, 1000)

# Calculate and print ROI
roi = calculator.calculate_roi()
print(f"ROI: {roi:.2f}%")

# Additional ROI Calculation
income = 2000
expenses = 6100
rental_income = 400000
cash_flow = income - expenses
total_investment = 50000
annual_cash_flow = cash_flow * 12
cash_on_cash_roi = (annual_cash_flow / total_investment) * 100

# Print additional ROI calculation results
print(f"Cash Flow: ${cash_flow}")
print(f"Annual Cash Flow: ${annual_cash_flow}")
print(f"Cash-on-Cash ROI: {cash_on_cash_roi:.2f}%")

# Additional Terms and Definitions
# Net Operating Income (NOI)
gross_income = rental_income
operating_expenses = expenses
net_operating_income = gross_income - operating_expenses
print(f"Net Operating Income (NOI): ${net_operating_income}")

# Cap Rate
cap_rate = (net_operating_income / rental_income) * 100
print(f"Cap Rate: {cap_rate:.2f}%")

# Cash-On-Cash Return
cash_on_cash_return = (annual_cash_flow / total_investment) * 100
print(f"Cash-On-Cash Return: {cash_on_cash_return:.2f}%")

# Annual Gross Rent Multiplier (GRM)
grm = rental_income / gross_income
print(f"Annual Gross Rent Multiplier (GRM): {grm:.2f}")

# Annual Cash Flow
debt_amount = 0
annual_cash_flow = net_operating_income - debt_amount
print(f"Annual Cash Flow: ${annual_cash_flow}")
