from flask import Flask, render_template, request, redirect, url_for
from autoCorrect import turkish_autocorrect_tool
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'kullanici_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('ana_sayfa.html')

@app.route('/duzelt_sayfasi')
def about():
    return render_template('duzelt_sayfasi.html')

@app.route('/login', methods=['GET', 'POST'] )
def contact():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Veritabanı bağlantısı kur
        cursor = mysql.connection.cursor()
        
        # Kullanıcıyı veritabanında sorgula
        query = "SELECT * FROM users WHERE username=%s AND password_hash=%s"
        cursor.execute(query, (username, password))
        
        # Sorgu sonucunu al
        data = cursor.fetchone()
        
        if data is None:
            # Kullanıcı bulunamadı veya şifre yanlış
            return redirect(url_for('contact'))
        else:
            # Kullanıcı bulundu, başarı sayfasına yönlendir
            return redirect(url_for('home', name=username))
    else:
        return render_template('giris_ekrani.html')   # GET isteği için login formunu göster
    
    

@app.route('/correct', methods=['POST'])
def correct_text():
    input_text = request.form.get('input')

    if not input_text:
      return redirect(url_for('about'))
    
    corrected_text = turkish_autocorrect_tool(input_text)
    print(corrected_text)
    return render_template('duzelt_sayfasi.html',corrected=corrected_text, text=input_text )
    
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('giris_ekrani.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)