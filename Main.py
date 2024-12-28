from Utils import load_data
from Income_statement import generate_income_statement
from Balance_sheet import generate_balance_sheet
from Cash_flow import generate_cash_flow_statement
from Utils import plot_income_vs_expenses

def main(): 
    file_path = "Data/Sample_transactions"
    data = load_data(file_path)
    if data is None: 
        return 
    
    print("Income Satement:")
    income_statement = generate_income_statement(data)
    for key, value in income_statement.items(): 
        print(f"{key}: ${value:.2f}")
    
    print("\nBalance Sheet:")
    balance_sheet = generate_balance_sheet(data)
    for key, value in balance_sheet.items():
        print(f"{key}: ${value:.2f}")

    print("\nCash Flow Statement:")
    cash_flow = generate_cash_flow_statement(data)
    for key, value in cash_flow.items():
        print(f"{key}: ${value:.2f}")

    plot_income_vs_expenses(data)

if __name__ == "__main__":
    main()