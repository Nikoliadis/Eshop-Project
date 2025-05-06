# 🤝 Οδηγίες Συμμετοχής (Team Contribution Guidelines)

Καλώς ήρθατε στο επίσημο repo της ομάδας μας! Για να διατηρήσουμε τον κώδικα καθαρό, λειτουργικό και συνεργατικό, ακολουθούμε τις εξής οδηγίες:

---

## 🔄 Git Workflow

### 🔹 Branching

- **Μην κάνετε ποτέ push απευθείας στο `main`.**
- Δημιουργείτε νέο branch με βάση το αντικείμενό σας:

```
git checkout -b nikos-backend
git checkout -b nontas-db
git checkout -b loras-frontend
```

---

### 🔹 Commits

- Κάνετε τακτικά commits με **καθαρά και περιγραφικά μηνύματα**:

```
git commit -m "Add login route"
git commit -m "Fix navbar CSS for mobile"
```

---

### 🔹 Push

- Κάνετε push στο **δικό σας branch**, όχι στο `main`.

```
git push origin your-branch-name
```

---

## 🚀 Pull Requests (PR)

- Όταν ολοκληρώσετε ένα task, κάνετε PR προς το `main` branch.
- Ένα άλλο μέλος της ομάδας κάνει **review και approve** πριν γίνει merge.
- **Μόνο ο Νίκος** (Admin) κάνει merge στο `main`.

---

## ✅ Κανόνες Καθαρού Κώδικα

- Γράφουμε **modular** και **καλά σχολιασμένο** κώδικα.
- Δεν αφήνουμε `print()` ή debugging code στο `main`.
- Όταν αλλάζουμε κοινά αρχεία (`base.html`, `models.py`), το συζητάμε πρώτα.

---

## 📂 Δομή Repo

Ακολουθούμε τη δομή που έχει τεθεί στο README. Αν χρειαστεί αλλαγή, συζητιέται πρώτα.

---

## 📞 Συνεννόηση

- Για κάθε σημαντική αλλαγή, συζητάμε στο group chat πριν προχωρήσει.
- Αν κάποιος λείπει ή μπλοκάρει, ενημερώνει την ομάδα.

---

Καλή δουλειά και σεβασμός στην ομάδα μας! 💪
