# Düzyaz.AI

Düzyaz.AI, kullanıcıların yazılarındaki yazım hatalarını otomatik olarak düzelten bir web tabanlı uygulamadır. Bu proje, özellikle Türkçe metinlerdeki yazım hatalarını tespit etmeyi ve düzeltmeyi amaçlamaktadır.

## Projenin Amacı

Düzyaz.AI'nin amacı, kullanıcılara zamanlarını ve çabalarını daha verimli kullanmalarını sağlayarak, yazılarının kalitesini artırmaktır. 

## Kapsam

- Türkçe metinlerdeki yazım hatalarını tespit etme ve düzeltme.
- Gelecekte daha fazla dil desteği eklenebilir.

## Özellikler

- Otomatik yazım hatası düzeltme
- Kullanıcı profili oluşturma
- Kullanıcı dostu arayüz

## Kullanıcı Kitlesi

- Öğrenciler
- Çalışanlar
- Genel olarak yazı yazan herkes

## Kullanım Senaryoları

Kullanıcılar, fatura, rapor veya diğer yazılarını kopyalayıp uygulamaya yükleyebilir. Uygulama, metindeki hataları bulur ve düzeltilmiş metni sunar.

## Gereksinimler

### İşlevsel Gereksinimler

- Yazım hatalarının otomatik düzeltilmesi
- Türkçe dil desteği (gelecekte daha fazla dil eklenebilir)
- Kullanıcı profili oluşturma

### Arayüz Gereksinimleri

- Kullanıcı dostu bir web arayüzü
- Metin girişi için bir alan
- Düzeltilmiş metnin gösterildiği bir alan

### Performans Gereksinimleri

- Tepki süresi (düzeltmelerin hızlı bir şekilde gösterilmesi)
- Kabul edilebilir doğruluk oranı (doğru düzeltmelerin yapılması)

### Güvenlik Gereksinimleri

- Kullanıcı verilerinin gizliliği
- Verilerin şifrelenmesi
- Üçüncü taraflarla veri paylaşımının olmaması

## Kısıtlar

- Teknolojik Kısıtlar: Uygulamanın web tabanlı olması ve çeşitli tarayıcılarla uyumlu çalışması gerekiyor.
- Bütçe ve Maliyet Kısıtları: Proje bütçesi sınırlı olduğundan, düşük maliyetli çözümler tercih ediliyor.
- Zaman Kısıtları: Proje belirli bir zaman dilimi içinde tamamlanması gerekiyor.


### Gerekli Yazılımlar

1. Python 3.7 veya daha yeni bir sürüm
2. MySQL veritabanı

## Kullanım

1. Web tarayıcınızı açın ve `https://duzyaz.onrender.com/` adresine gidin.

2. Siteye giriş yapın veya kayıt olun.

3. 'Düzyaz.AI' butonuna tıklayın.

4. Metninizi giriş alanına yazın ve "Düzelt" butonuna tıklayın.

6. Düzeltilmiş metni görüntüleyin.

## Proje Dosyaları

- `app.py`: Flask uygulamasının ana dosyası.
- `autoCorrect.py`: Yazım hatalarını düzeltme fonksiyonlarını içerir.
- `login.py`: Kullanıcı oturum açma fonksiyonlarını içerir.
- `Gereksinim_Dokuman.pdf`: Projenin gereksinim dokümanı.
- `README.md`: Projenin açıklayıcı dokümanı.

## Proje Mimarisi

1. **Flask Uygulaması**:
   - `app.py` dosyası Flask uygulamasının ana dosyasıdır ve tüm rotaları içerir.
   - `login.py` dosyası, kullanıcıların oturum açma ve kayıt işlemlerini yönetir.
   - `autoCorrect.py` dosyası, OpenAI API'sini kullanarak metin düzeltme işlevlerini içerir.

2. **Veritabanı**:
   - PostgreSQL veritabanı kullanıcı profilleri ve yazım düzeltme geçmişini saklamak için kullanılır.
   - Veritabanı yapılandırması `app.py` dosyasında tanımlanmıştır.

3. **Arayüz**:
   - Kullanıcı dostu bir web arayüzü, kullanıcıların metinlerini kopyalayıp düzeltmelerini sağlar.

## Katkıda Bulunma

Katkıda bulunmak isterseniz lütfen bir pull request gönderin veya bir issue açın. Katkılarınızı memnuniyetle karşılıyoruz!

