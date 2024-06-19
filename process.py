import csv
from pymongo import MongoClient
import pandas as pd
 
class User:
        def __init__(self, age, gender, total_income, expenses):
            self.age = age
            self.gender = gender
            self.total_income = total_income
            self.expenses = expenses
 
        @staticmethod
        def fetch_data_from_mongo():
            client = MongoClient('localhost', 27017)
            db = client.survey_db
            collection = db.users
            data = list(collection.find())
            return data
 
        @staticmethod
        def save_to_csv(data, filename='output_data.csv'):
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
                for entry in data:
                    writer.writerow([entry['age'], entry['gender'], entry['total_income'],
                                     entry['expenses'].get('utilities', 0), entry['expenses'].get('entertainment', 0),
                                     entry['expenses'].get('school_fees', 0), entry['expenses'].get('shopping', 0),
                                     entry['expenses'].get('healthcare', 0)])
 
if __name__ == '__main__':
        user_data = User.fetch_data_from_mongo()
        User.save_to_csv(user_data)