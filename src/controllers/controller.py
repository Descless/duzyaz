from models.autoCorrect import turkish_autocorrect_tool
import database


# insert data into table.
def login_page(request, mysql):
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
            return False
        else:
            return True
    
def correct_text(input_text):
    return turkish_autocorrect_tool(input_text)
