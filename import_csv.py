import pandas as pd
from database import session, Transaction
from datetime import datetime

CSV_FILE = "finance_data.csv"  # Update with your actual CSV file path

def import_csv_to_db():
    try:
        # Read CSV into a DataFrame
        df = pd.read_csv(CSV_FILE)

        # Convert the 'date' column to the correct format
        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

        # Iterate through the DataFrame and insert data into the database
        for _, row in df.iterrows():
            transaction = Transaction(
                date=row["date"],
                amount=row["amount"],
                category=row["category"],
                description=row.get("description", "")  # Handle missing descriptions
            )
            session.add(transaction)

        # Commit changes
        session.commit()
        print("✅ Data imported successfully from CSV to the database!")

    except Exception as e:
        print(f"❌ Error importing CSV: {e}")

if __name__ == "__main__":
    import_csv_to_db()
