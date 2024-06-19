from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from pymongo.errors import PyMongoError
 
app = Flask(__name__)
mongo_uri = 'mongodb+srv://hafisayeni:40hyUfg8n6bod5pT@healthcare.yeweczc.mongodb.net/?retryWrites=true&w=majority&appName=healthcare'
client = MongoClient(mongo_uri)
db = client.survey_db
collection = db.users

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        total_income = request.form['total_income']
        expenses = {
            'utilities': request.form.get('utilities', 0),
            'entertainment': request.form.get('entertainment', 0),
            'school_fees': request.form.get('school_fees', 0),
            'shopping': request.form.get('shopping', 0),
            'healthcare': request.form.get('healthcare', 0)
        }
        user_data = {
            'name': name,
            'age': age,
            'gender': gender,
            'total_income': total_income,
            'expenses': expenses
        }
        collection.insert_one(user_data)
        print("Data submitted successfully!")
    except (PyMongoError, Exception) as e:
        print(f"Failed to submit data: {e}")
    return redirect('/')
 
if __name__ == '__main__':
    app.run(debug=True)