# Django Multilingual FAQ System

## 🚀 Overview
This project is a Django-based FAQ management system with multilingual support, a WYSIWYG editor, caching for performance, and a REST API.

## 🛠 Features
- ✅ **Multilingual Support:** FAQs support multiple languages (English, Hindi, Bengali).
- ✅ **WYSIWYG Editor:** Rich-text formatting using `django-ckeditor`.
- ✅ **REST API:** Fully functional API for FAQ retrieval and management.
- ✅ **Language-Based Queries:** Retrieve FAQs in a specific language using `?lang=hi` or `?lang=bn`.
- ✅ **Caching for Performance:** Uses Redis to cache translations for fast responses.
- ✅ **Admin Panel:** User-friendly interface for managing FAQs.

---

## 🚀 Installation Guide

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/django-multilingual-faq.git
cd django-multilingual-faq
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up the Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ **Run the Development Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/admin` to access the admin panel.

---

## 🔥 API Usage

### ✅ **Retrieve FAQs (English by Default)**
```http
GET /api/faqs/
```
**Response:**
```json
{
  "faqs": [
    {
      "id": 1,
      "question": "What is Django?",
      "answer": "<p>Django is a Python framework.</p>"
    }
  ]
}
```

### ✅ **Retrieve FAQs in Hindi**
```http
GET /api/faqs/?lang=hi
```

### ✅ **Retrieve FAQs in Bengali**
```http
GET /api/faqs/?lang=bn
```

---

## 🛠 Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL / SQLite
- **Caching:** Redis
- **Translation:** `googletrans`
- **Admin Panel:** Django Admin with `django-ckeditor`

---

## 📜 Contribution Guidelines
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m "feat: Added XYZ feature"`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a Pull Request.

---

## 📜 Git Commit Conventions
Follow conventional commit messages:
- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`

---

## 📌 License
This project is licensed under the MIT License.

---

## 📞 Contact
For queries, contact: `taha.sadikot.m@gmail.com`
