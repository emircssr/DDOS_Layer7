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
