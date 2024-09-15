# DDOS Attack 2070

**DDOS Attack 2070**, HTTP/2, WebSocket, SYN, UDP ve DNS Amplifikasyonu gibi çok vektörlü saldırı yöntemlerini bir araya getiren ileri seviye bir DDOS saldırı aracıdır. 500+ thread kullanarak büyük çaplı saldırılar düzenleyebilir ve savunma sistemlerini aşabilir.

## Özellikler

- **HTTP/2 Flood (500 Thread)**: Uygulama katmanında HTTP/2 protokolü üzerinden saldırı düzenler.
- **WebSocket Flood (200 Thread)**: WebSocket bağlantılarını kullanarak sunucu kaynaklarını boğar.
- **SYN Flood (200 Thread)**: Ağ katmanında SYN paketleri göndererek TCP bağlantı kuyruğunu doldurur.
- **UDP Flood (200 Thread)**: UDP protokolü ile hedef sunucunun bant genişliğini boğar.
- **DNS Amplifikasyonu (100 Thread)**: DNS sunucularına sahte istekler göndererek büyük veri paketleriyle hedefi boğar.
- **Proxy Rotasyonu**: Proxy kullanarak saldırıların kaynağı sürekli değiştirilir.
- **IP Spoofing**: Sahte IP adresleri kullanılarak saldırılar düzenlenir.
- **Base64 Şifreleme**: Saldırıyı başlatmadan önce şifre doğrulaması yapılır.

## Gereksinimler

- Python 3.x
- Gerekli Python paketleri:




## Kullanım

1. **Dosyaları Hazırlayın**:
 - `ddos_attack_2070.py` dosyasını indirin ve bilgisayarınıza kaydedin.
 - Saldırı için proxy listelerini içeren `proxy.txt` dosyasını oluşturun (her satırda bir proxy adresi olacak şekilde).

2. **Script'i Çalıştırın**:
 - Terminal veya komut satırını açın ve dosyanın bulunduğu dizine gidin:
   ```
   cd [dosya_yolu]
   ```
 - DDOS script'ini çalıştırmak için şu komutu çalıştırın:
   ```
   python ddos_attack_2070.py
   ```

3. **Saldırı Parametrelerini Girin**:
 - **Hedef URL**: Saldırıyı yapmak istediğiniz web sitesinin URL'sini girin (örn: `http://example.com`).
 - **Hedef IP**: Web sitesinin IP adresini girin (örn: `192.168.1.1`).
 - **Port**: Hedef sunucunun portunu girin (örn: `80`).
 - **Saldırı Süresi**: Saldırının kaç saniye süreceğini belirtin (örn: `60`).

4. **Şifre Doğrulama**:
 - Program şifre isteyecektir. Şifre: `emircssr`.

5. **Onay**:
 - Son olarak, saldırıyı başlatmak isteyip istemediğiniz sorulacaktır. "evet" yazarsanız saldırı başlatılacaktır, "hayır" yazarsanız iptal edilecektir.

## Yasal Uyarı

Bu araç yalnızca eğitim ve araştırma amaçlıdır. Yasal olmayan kullanım, suç teşkil edebilir ve ciddi hukuki sonuçlara yol açabilir. Lütfen yerel yasalar ve etik kurallar çerçevesinde kullanın. Proje sahipleri ve geliştiriciler, bu aracın yasa dışı kullanımından sorumlu değildir.
