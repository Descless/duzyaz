from .autoCorrect import turkish_autocorrect_tool
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# insert data into table.
def login_page(request, mysql):
        username = request.form['username']
        password = request.form['password']
        
        # Veritabanı bağlantısı kur
        cursor = mysql.connection.cursor()
        
        # Kullanıcıyı veritabanında sorgula
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        
        # Sorgu sonucunu al
        data = cursor.fetchone()
        
        if data is None or not check_password_hash(data[3], password):
            return False
        else:
            return True
        
def sign_in(request, mysql):
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Veritabanı bağlantısı kur
        cursor = mysql.connection.cursor()

        password_hash = generate_password_hash(password)
        
        # Kullanıcıyı veritabanında sorgula
        try:
            cursor.execute('INSERT INTO users (email, username, password_hash) VALUES (%s, %s, %s)', (email, username, password_hash))
            mysql.connection.commit()
            print("User inserted successfully")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
        
        
def correct_text(input_text):
    return turkish_autocorrect_tool(input_text)


