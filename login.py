from flask import Flask, request, redirect, url_for, render_template


def login(mysql):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Veritabanı bağlantısı kur
        conn = mysql.connect()
        cursor = conn.cursor()
        
        # Kullanıcıyı veritabanında sorgula
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        
        # Sorgu sonucunu al
        data = cursor.fetchone()
        
        if data is None:
            # Kullanıcı bulunamadı veya şifre yanlış
            return redirect(url_for('index'))
        else:
            # Kullanıcı bulundu, başarı sayfasına yönlendir
            return redirect(url_for('success', name=username))
    else:
        return render_template('giris_ekrani.html')   # GET isteği için login formunu göster