from .autoCorrect import turkish_autocorrect_tool
from werkzeug.security import generate_password_hash, check_password_hash

def login_page(request, db):
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor() 
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        data = cursor.fetchone()
        cursor.close()

        if data is None or not check_password_hash(data[3], password):
             return False
        else:
             return True
        
def sign_in(request, db):
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        password_hash = generate_password_hash(password)

        cursor = db.cursor()
        try:
                query = "INSERT INTO users (email, username, password_hash) VALUES (%s, %s, %s)"
                cursor.execute(query, (email, username, password_hash))
                db.commit()
                print("User inserted successfully")
        except Exception as e:
              print(f"Error: {e}")
        finally:
                cursor.close()
        
def correct_text(input_text):
    return turkish_autocorrect_tool(input_text)


