# **Sharebite Backend**

Sharebite is a Django-based backend application for a food-sharing platform where users can post, claim, donate, and interact with food posts. This project is designed to work seamlessly with a React frontend via RESTful APIs.

---

## **Features**

- **User Management**: Individual users, NGOs, and restaurants can register, log in, and manage profiles.
- **Food Posts**: Users can create, view, like, share, and bookmark food posts with details like food name, image, and description.
- **Food Claims**: Users can claim food items and view pickup location details and contact information.
- **Donations**: Any user can donate funds to a food post.
- **Interactions**: Supports liking, sharing, and bookmarking of food posts.

---

## **Technologies Used**

- **Backend Framework**: Django 4.x
- **API**: Django REST Framework
- **Database**: SQLite (Development)
- **Image Handling**: Pillow for image uploads
- **Deployment**: Compatible with services like Render, Heroku, and AWS.

---

## **Getting Started**

### Prerequisites
- Python 3.11+
- Virtual environment (e.g., `venv`)
- Git for version control

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/happyabhinavmaurya/sharebitebackend.git
   cd sharebitebackend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Test the API by visiting:
   ```
   http://127.0.0.1:8000/api/
   ```

---

## **Project Structure**

```
sharebite-backend/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## **API Endpoints**

### **Authentication**
- `POST /api/auth/login/`: User login
- `POST /api/auth/signup/`: User registration

### **Food Posts**
- `GET /api/food-posts/`: List all food posts
- `POST /api/food-posts/`: Create a new food post
- `GET /api/food-posts/<id>/`: Retrieve details of a specific post

### **Claims**
- `POST /api/claims/`: Claim a food post
- `GET /api/claims/`: View claims by user

### **Donations**
- `POST /api/donations/`: Donate to a food post

### **Interactions**
- `POST /api/interactions/`: Like, share, or bookmark a food post

---

## **Contributing**

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For inquiries or feedback, reach out to:
- **Author**: Abhinav Maurya
- **Email**: [happyabhinavmaurya@gmail.com](mailto:happyabhinavmaurya@gmail.com)

Happy coding! 🎉

--- 
