from tkinter import simpledialog


def to_monthly(amount, frequency):
    amount = float(amount)
    if frequency == "Hourly":
        hours = simpledialog.askfloat("Hours Worked", "Hours per week?")
        return amount * hours * 4.345
    if frequency == "Daily":
        return amount * 30.437
    if frequency == "Weekly":
        return amount * 4.345
    if frequency == "Monthly":
        return amount
    if frequency == "Yearly":
        return amount / 12
    return amount


def calculate_monthly_summary(income_rows, expense_rows):
    income_total = 0
    expense_total = 0

    for frame, row in income_rows:
        try:
            amt = row["amount"].get()
            freq = row["frequency"].get()
            income_total += to_monthly(amt, freq)
        except:
            pass

    for frame, row in expense_rows:
        try:
            amt = row["amount"].get()
            freq = row["frequency"].get()
            expense_total += to_monthly(amt, freq)
        except:
            pass

    net = income_total - expense_total

    return (
        f"Monthly Income:  ${income_total:,.2f}\n"
        f"Monthly Expense: ${expense_total:,.2f}\n\n"
        f"Net Profit:      ${net:,.2f}"
    )
