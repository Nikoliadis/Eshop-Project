# 🔧 Project Name – Company Website / eShop

## 📌 Περιγραφή

Πρόκειται για ένα πλήρως λειτουργικό δυναμικό website με δυνατότητα παρουσίασης υπηρεσιών, portfolio, επικοινωνίας και (προαιρετικά) ηλεκτρονικών πωλήσεων. Το project αναπτύσσεται με Flask, SQLAlchemy και HTML/CSS/Bootstrap.

---

## 🧠 Ομάδα Ανάπτυξης

| Ρόλος                | Όνομα  | Περιγραφή εργασιών                                      |
| -------------------- | ------ | ------------------------------------------------------- |
| 👨‍💻 Backend Developer | Νίκος  | Flask app, routing, views, business logic, APIs         |
| 🧠 Database Manager  | Νώντας | Σχεδιασμός schema, δημιουργία μοντέλων, queries         |
| 🎨 Frontend & Design | Λόρας  | HTML/CSS, Bootstrap, responsive design, UI/UX templates |

---

## 🚀 Τεχνολογίες

- Python 3.x
- Flask
- SQLAlchemy
- Jinja2 Templates
- Bootstrap 5
- SQLite / PostgreSQL (ανάλογα με την εγκατάσταση)

---

## 📁 Δομή Project

```
project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── services.html
│   │   └── contact.html
│   └── static/
│       ├── css/
│       └── js/
├── run.py
├── config.py
```

---

## ⚙️ Εγκατάσταση – Βήμα προς Βήμα

```bash
git clone https://github.com/Nikoliadis/Eshop-Project.git
cd Eshop-Project
python -m venv venv
venv\Scripts\activate  # ή source venv/bin/activate σε Mac/Linux

# Αν είσαι σε PowerShell και έχει θέμα, τρέξε:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

pip install flask flask_sqlalchemy flask_login flask_migrate
python eshop.py
```

---

## 🚀 Push στο GitHub (manual setup)

```bash
# 1. Άνοιξε τερματικό μέσα στον φάκελο του project
cd path\to\Eshop-Project

# 2. Αν δεν έχεις κάνει ακόμα
git init

# 3. Πρόσθεσε όλα τα αρχεία
git add .

# 4. Κάνε commit με μήνυμα
git commit -m "Setup Flask project with models and requirements"

# 5. Σύνδεσε το GitHub repo
git remote add origin https://github.com/username/eshop-project.git

# 6. Στείλε τα αρχεία
git push -u origin main
```

---

## 📩 Επικοινωνία Ομάδας

- Email Νίκου: nikos@example.com
- Email Νώντα: nontas@example.com
- Email Λόρα: loras@example.com
