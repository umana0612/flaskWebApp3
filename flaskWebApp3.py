from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

#TODO: first download cars.csv from canvas
# 1) read the cars.csv file and convert it to a pandas dataframe
# 2) Create a route to return the first 10 rows of the dataframe
# 3) Create a route to return the list of car manufacturers
# 4) Create a route to return the car name and price

df = pd.read_csv('cars.csv')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my First API"})
@app.route('/cars')
def get_cars():
    return jsonify(df.head(10).to_json(orient='records'))

@app.route('/manufacturers')
def manufacturers():
    return jsonify(df['CarName'].str.split().str[0].unique.tolist())

@app.route('/cars/prices')
def get_prices():
    return jsonify(df[['CarName','price']].to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
