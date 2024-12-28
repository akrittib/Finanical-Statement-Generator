def generate_income_statement(data):
    income = data[data["Type"] == "Income"]["Amount"].sum()
    expenses = data[data["Type"] == "Expense"]["Amount"].sum()
    net_income = income + expenses 

    return{
        "Revenue": net_income,
        "Expenses": -expenses,
        "Net Income": net_income,
    }