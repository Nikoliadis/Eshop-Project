# 🚀 Manual: Deploy Flask App on Hetzner VPS (Ubuntu 22.04)

Αυτός ο οδηγός δείχνει βήμα-βήμα πώς να ανεβάσετε Flask app σε VPS (Hetzner) με Gunicorn + NGINX + HTTPS.

---

## 🖥️ 1. Δημιουργία VPS
- Πηγαίνουμε στο [Hetzner Cloud](https://console.hetzner.cloud/)
- Δημιουργούμε νέο Server (π.χ. CX11 - Ubuntu 22.04)
- Παίρνουμε τη δημόσια IP (π.χ. `95.179.XXX.XXX`)

---

## 🔐 2. Συνδεόμαστε με SSH

```bash
ssh root@your.server.ip
```

---

## ⚙️ 3. Εγκατάσταση Εργαλείων

```bash
apt update && apt upgrade -y
apt install python3 python3-pip python3-venv nginx ufw -y
```

---

## 🐍 4. Φτιάχνουμε το Flask project

```bash
mkdir /var/www/flaskapp
cd /var/www/flaskapp
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn
```

**Παράδειγμα `app.py`:**

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app live on VPS!"
```

---

## 🔥 5. Δοκιμή με Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

Αν δεις "Running on http://0.0.0.0:8000", είσαι ΟΚ.

---

## 🌐 6. Ρύθμιση NGINX

```bash
nano /etc/nginx/sites-available/flaskapp
```

**Περιεχόμενο:**

```nginx
server {
    listen 80;
    server_name yourdomain.gr;

    location / {
        proxy_pass http://127.0.0.1:8000;
        include proxy_params;
        proxy_redirect off;
    }
}
```

```bash
ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
nginx -t
systemctl restart nginx
```

---

## 🔒 7. Προσθήκη HTTPS (Let’s Encrypt)

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d yourdomain.gr
```

---

## 🔥 8. Autostart με systemd

```bash
nano /etc/systemd/system/flaskapp.service
```

**Περιεχόμενο:**

```ini
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/flaskapp
Environment="PATH=/var/www/flaskapp/venv/bin"
ExecStart=/var/www/flaskapp/venv/bin/gunicorn --workers 3 --bind unix:/var/www/flaskapp/flaskapp.sock app:app

[Install]
WantedBy=multi-user.target
```

```bash
systemctl start flaskapp
systemctl enable flaskapp
```

---

## 🧱 9. Firewall (προαιρετικά)

```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
```

---

## ✅ Τέλος! Το Flask app σας είναι live!

Ανοίξτε τον browser σας:  
`https://yourdomain.gr`

