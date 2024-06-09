from models import model
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import database

app = Flask(__name__)

app.config['MYSQL_HOST'] = database.host
app.config['MYSQL_USER'] = database.user
app.config['MYSQL_PASSWORD'] = database.password
app.config['MYSQL_DB'] = database.database

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('ana_sayfa.html')

@app.route('/duzelt_sayfasi')
def correct_page():
    return render_template('duzelt_sayfasi.html')

@app.route('/login', methods=['GET', 'POST'] )
def login_page():
    if request.method == 'POST':
        is_true = model.login_page(request, mysql)
        if is_true == False:
           return redirect(url_for('login_page'))
        if is_true == True:
           return redirect(url_for('correct_page')) 
    else:
        return render_template('giris_ekrani.html')

@app.route('/sign_in', methods=['GET', 'POST'] )
def sign_in_page():
    if request.method == 'POST':
        model.sign_in(request, mysql)
        return redirect(url_for('login_page'))
        #if is_true == False:
           #return redirect(url_for('sign_in_page'))
       # if is_true == True:
          # return redirect(url_for('login_page'))
    else:
        return render_template('kayit_ekrani.html')  

@app.route('/correct', methods=['POST'])
def correct_text():
    input_text = request.form.get('input')

    if not input_text:
      return redirect(url_for('correct_page'))

    corrected_text = model.correct_text(input_text)

    return render_template('duzelt_sayfasi.html',corrected=corrected_text, text=input_text )
    

if __name__ == '__main__':
    app.run(debug=True)