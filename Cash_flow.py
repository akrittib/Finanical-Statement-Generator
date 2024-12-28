def generate_cash_flow_statement(data):
    operating = data[data["Type"].isin (["Income", "Expense",])]["Amount"].sum()
    investing = data[data["Type"] == "Asset"]["Amount"].sum()
    financing = data[data ["Type"] == "Liability"]["Amount"].sum()

    return{
        "Operating Activities": operating, 
        "Investing Activities": investing, 
        "Financing Activities": financing
    }