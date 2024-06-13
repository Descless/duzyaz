Düzyaz.AI
Düzyaz.AI, kullanıcıların yazılarındaki yazım hatalarını otomatik olarak düzelten bir web tabanlı uygulamadır. Bu proje, özellikle Türkçe metinlerdeki yazım hatalarını tespit etmeyi ve düzeltmeyi amaçlamaktadır.

Projenin Amacı
Düzyaz.AI'nin amacı, kullanıcılara zamanlarını ve çabalarını daha verimli kullanmalarını sağlayarak, yazılarının kalitesini artırmaktır.

Kapsam
Türkçe metinlerdeki yazım hatalarını tespit etme ve düzeltme.
Gelecekte daha fazla dil desteği eklenebilir.
Özellikler
Otomatik yazım hatası düzeltme
Kullanıcı profili oluşturma
Kullanıcı dostu arayüz
Kullanıcı Kitlesi
Öğrenciler
Çalışanlar
Genel olarak yazı yazan herkes
Kullanım Senaryoları
Kullanıcılar, fatura, rapor veya diğer yazılarını uygulamaya yükleyebilir. Uygulama, metindeki hataları bulur ve düzeltilmiş metni sunar.

Gereksinimler
İşlevsel Gereksinimler
Yazım hatalarının otomatik düzeltilmesi
Türkçe dil desteği (gelecekte daha fazla dil eklenebilir)
Kullanıcı profili oluşturma
Arayüz Gereksinimleri
Kullanıcı dostu bir web arayüzü
Metin girişi için bir alan
Düzeltilmiş metnin gösterildiği bir alan
Performans Gereksinimleri
Tepki süresi (düzeltmelerin hızlı bir şekilde gösterilmesi)
Kabul edilebilir doğruluk oranı (doğru düzeltmelerin yapılması)
Güvenlik Gereksinimleri
Kullanıcı verilerinin gizliliği
Verilerin şifrelenmesi
Üçüncü taraflarla veri paylaşımının olmaması
Kısıtlar
Teknolojik Kısıtlar: Uygulamanın web tabanlı olması ve çeşitli tarayıcılarla uyumlu çalışması gerekiyor.
Bütçe ve Maliyet Kısıtları: Proje bütçesi sınırlı olduğundan, düşük maliyetli çözümler tercih ediliyor.
Zaman Kısıtları: Proje belirli bir zaman dilimi içinde tamamlanması gerekiyor.
Kurulum
Gerekli paketleri yükleyin:

sh
Kodu kopyala
pip install openai flask flask-mysqldb requests
OpenAI API anahtarınızı alın ve YOUR_API_KEY ile değiştirin:

python
Kodu kopyala
openai.api_key = 'YOUR_API_KEY'
MySQL veritabanı yapılandırmasını yapın:

python
Kodu kopyala
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'
Kullanım
Flask uygulamasını başlatın:

sh
Kodu kopyala
python app.py
API'ye POST isteği gönderin:

python
Kodu kopyala
import requests

url = 'http://localhost:5000/correct'
data = {'text': 'Bu bir örnek cümledir ve baz hataları içerir.'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(response.json())
Proje Dosyaları
app.py: Flask uygulamasının ana dosyası.
autoCorrect.py: Yazım hatalarını düzeltme fonksiyonlarını içerir.
login.py: Kullanıcı oturum açma fonksiyonlarını içerir.
Gereksinim_Dokuman.pdf: Projenin gereksinim dokümanı.
README.md: Projenin açıklayıcı dokümanı.
Versiyon Geçmişi
Versiyon 1.0: İlk sürüm
Katkıda Bulunma
Katkıda bulunmak isterseniz lütfen bir pull request gönderin veya bir issue açın.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
