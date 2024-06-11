import os
from models import model
from flask import Flask, render_template, request, redirect, url_for
import psycopg2


app = Flask(__name__)

db = psycopg2.connect(database=os.getenv('database'), user=os.getenv('user'), 
                        password=os.getenv('password'), host=os.getenv('host'), port=os.getenv('port'))

is_logged_in = False

@app.route('/')
def index():
    if is_logged_in == False:
        return render_template('ana_sayfa.html')
    else:
        return render_template('kullanici_ana_sayfa.html')



@app.route('/duzelt_sayfasi')
def correct_page():
    return render_template('duzelt_sayfasi.html')

@app.route('/giris_ekrani', methods=['GET', 'POST'] )
def login_page():
    global is_logged_in
    if request.method == 'POST':
        is_true = model.login_page(request, db)
        if is_true == False:
           return redirect(url_for('login_page'))
        if is_true == True:
           is_logged_in = True
           print(is_logged_in)
           return redirect(url_for('index')) 
    else:
        return render_template('giris_ekrani.html')

@app.route('/sign_in', methods=['GET', 'POST'] )
def sign_in_page():
    if request.method == 'POST':
        model.sign_in(request, db)
        return redirect(url_for('login_page'))
    else:
        return render_template('kayit_ekrani.html')  

@app.route('/correct', methods=['POST'])
def correct_text():
    input_text = request.form.get('input')

    if not input_text:
      return redirect(url_for('correct_page'))

    corrected_text = model.correct_text(input_text)

    return render_template('duzelt_sayfasi.html',corrected=corrected_text, text=input_text )
    

@app.route('/urunler')
def products_page():
    if is_logged_in == False:
        return render_template('urunler.html')
    if is_logged_in == True:
        return render_template('kullanici_urunler.html')

@app.route('/hakkimizda')
def about_page():
    if is_logged_in == False:
        return render_template('hakkimizda.html')
    if is_logged_in == True:
        return render_template('kullanici_hakkimizda.html')

@app.route('/iletisim')
def contact_page():
    if is_logged_in == False:
        return render_template('iletisim.html')
    if is_logged_in == True:
        return render_template('kullanici_iletisim.html')
    
@app.route('/logout')
def logout():
    global is_logged_in
    is_logged_in = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)