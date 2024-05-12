from flask import Flask, render_template, url_for
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials_file = '/Users/nidhibiswas/flask/token.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
gc = gspread.authorize(credentials)
sheet_title = 'Your Sheet Title'
worksheet = gc.open('Test Sheet').sheet1







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    

if __name__ == '__main__':
    app.run(debug=True)