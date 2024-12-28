def generate_balance_sheet(data):
    assets = data[data["Type"] == "Asset"]["Amount"].sum()
    liabilities = data[data["Type"] == "Liability"]["Amount"].sum()
    equity = assets + liabilities

    return{
        "Assets": assets, 
        "Liabilities": liabilities, 
        "Equity": equity
    }