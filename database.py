from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# Create SQLite database
DATABASE_URL = "sqlite:///finance_tracker.db"
engine = create_engine(DATABASE_URL, echo=True)

# Define ORM base
Base = declarative_base()

# Define Transaction table
class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add transaction
def add_transaction(date, amount, category, description):
    new_transaction = Transaction(
        date=datetime.strptime(date, "%d-%m-%Y"),
        amount=amount,
        category=category,
        description=description
    )
    session.add(new_transaction)
    session.commit()
    print("Transaction added successfully!")

# Function to get transactions
def get_transactions(start_date, end_date):
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")
    
    transactions = session.query(Transaction).filter(
        Transaction.date >= start_date, Transaction.date <= end_date
    ).all()

    if transactions:
        for t in transactions:
            print(f"{t.date} - {t.amount} - {t.category} - {t.description}")
    else:
        print("No transactions found.")
    
    return transactions

def get_transaction_data():
    transactions = session.query(Transaction).all()
    
    if not transactions:
        print("No transactions available for visualization.")
        return None
    
    data = defaultdict(list)
    
    for t in transactions:
        data["dates"].append(t.date)
        data["amounts"].append(t.amount)
        data["categories"].append(t.category)
    
    return data
