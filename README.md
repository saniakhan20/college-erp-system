# 🎓 College ERP System (Full-Stack Backend Architecture)

A scalable and modular College ERP backend system built using Django, Django REST Framework, and MySQL.

This project is designed with enterprise-level backend architecture, role-based access control, modular app structure, and RESTful API design to manage academic, administrative, and placement operations of an educational institution.

---

## 🚀 Project Overview

Colleges often rely on fragmented systems for managing student records, faculty data, attendance, examinations, finance, and placement activities.

This ERP system centralizes all institutional operations into a unified, scalable backend platform with:

- Custom Authentication System
- Role-Based Access Control (RBAC)
- Modular App Architecture
- RESTful API Layer
- Relational Database Design
- Clean Separation of Concerns

---

## 🏗️ System Architecture

Frontend (React / Mobile App)  
        ↓  
Django REST API Layer  
        ↓  
Django ORM  
        ↓  
MySQL Database  

### Backend Layers

1. Models Layer – Database schema and relationships  
2. Serializer Layer – Python object ↔ JSON transformation  
3. View Layer (API) – Business logic and request handling  
4. Authentication Layer – Custom user model and roles  
5. Admin Layer – Administrative interface for internal management  

---

## 🔐 Authentication & Authorization

- Custom `CustomUser` model
- Role-based system:
  - ADMIN
  - FACULTY
  - STUDENT
- One-to-One mapping:
  - User ↔ Student
  - User ↔ Faculty

Designed to support:
- Role-restricted API endpoints
- Future JWT-based authentication
- Secure access control

---

## 📦 Core Modules

### 👨‍🎓 Students
- Student profile management
- Academic information
- Department & Course mapping

### 👨‍🏫 Faculty
- Faculty profile management
- Department linkage

### 📚 Academics
- Departments
- Courses
- Subjects

### 📊 Attendance
- Attendance tracking system

### 💰 Finance
- Fee management (expandable)

### 💼 Placement
- Company records
- Job postings
- Student applications (expandable)

---

## 🔗 REST API Example

### Fetch Students

GET /api/students/

Returns:

```json
[
  {
    "id": 1,
    "enrollment_no": "CSE001",
    "first_name": "John",
    "cgpa": 8.9
  }
]
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | React.js |
| UI Styling | Tailwind CSS/Bootstrap |
| Backend Framework | Django |
| API Framework | Django REST Framework |
| Database | MySQL |
| Authentication | Custom User Model(RBAC) |
| Version Control | Git & GitHub |
| Architecture Style | Modular Monolithic Backend |


---

## 🧠 Key Engineering Concepts Implemented

- Custom AbstractUser Model
- OneToOne Relationships
- Foreign Key Relational Mapping
- RESTful Endpoint Design
- ModelSerializer Usage
- Generic Class-Based Views
- Separation of Concerns
- Clean Modular App Structure

---

## ⚙️ How to Run Locally

### 1️⃣ Clone Repository

git clone https://github.com/saniakhan20/college-erp-system.git

### 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Configure Database (MySQL)

Update settings.py with your database credentials.

### 5️⃣ Run Migrations

python manage.py makemigrations  
python manage.py migrate  

### 6️⃣ Create Superuser

python manage.py createsuperuser  

### 7️⃣ Start Server

python manage.py runserver  

---

## 📈 Future Enhancements

- JWT Authentication
- Role-based API Permissions
- React Frontend Integration
- Placement Workflow Automation
- Marks & Examination Module
- Deployment (AWS / Render / Railway)
- Docker Containerization

---

## 🎯 Project Objective

To demonstrate backend system design skills, database modeling expertise, authentication architecture, and RESTful API development aligned with industry-level full-stack engineering practices.

---

## 👩‍💻 Author

Sania Khan  
Backend Developer | Django | REST APIs | Database Design
