import pandas as pd
import matplotlib as plt 

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        required_columns = {"Date", "Description", "Amount", "Type"}
        if not required_columns.issubset(data.columns):
            raise ValueError("CSV must contain columns: Date, Description, Amount, Type")
        data["Amount"] = data["Amount"].astype(float)
        return data 
    except Exception as e: 
        print(f"Error loading file {e}")
        return None
    
def categorize_transactions(data): 
    categories = data.groupby("Type")["Amount"].sum()
    return categories

def plot_income_vs_expenses(data):
    summary = data[data["Type"].isin(["Income", "Expense"])]
    summary = summary.groupby("Type")["Amount"].sum()
    summary.plot(kind="bar", title="Income vs Expenses")
    plt.ylabel("Amount") 
    plt.show()
