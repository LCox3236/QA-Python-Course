def calculate_income_tax(salary):
    personal_allowance = 11850  # Tax-free allowance
    basic_rate_threshold = 34500
    higher_rate_threshold = 150000

    taxable_income = max(0, salary - personal_allowance)  
    tax = 0

    if taxable_income > higher_rate_threshold:
        tax += (taxable_income - higher_rate_threshold) * 0.45
        taxable_income = higher_rate_threshold  

    if taxable_income > basic_rate_threshold:
        tax += (taxable_income - basic_rate_threshold) * 0.4
        taxable_income = basic_rate_threshold 

    if taxable_income > 0:
        tax += taxable_income * 0.2

    print(f"Income tax payable on £{salary}: £{tax:.2f}")

calculate_income_tax(200000)

