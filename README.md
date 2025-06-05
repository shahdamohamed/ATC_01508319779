# 🎟️ Event Booking API

This is a Django REST Framework-based API for an **Event Booking System**. Users can browse available events, view event details, register accounts, and book events. The system handles event creation, user registrations, and secure bookings with role-based access.

---

## 🚀 Features

- 🔒 User Registration & Authentication (via API)
- 📆 List All Available Events
- 🔍 View Detailed Event Information
- 📝 Book Events (Authenticated Users)
- 🙋 View Your Bookings (User-Specific)
- 🔧 Admin Support to Add/Edit/Delete Events

---

## 📁 Project Structure

```
event_booking/
├── event_booking/      # Main Django project settings
├── events/             # App handling events and bookings
├── users/              # App managing user registration and authentication
└── requirements.txt    # Dependencies
```

---

## 🧑‍💻 Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** Token-based Authentication
- **Database:** SQLite (default, can be swapped)
- **API Tooling:** DRF Browsable API, JSON APIs

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shahdamohamed/event_booking.git
   cd event_booking
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

---

## 🛠️ API Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/events/` | GET | List all events |
| `/api/events/<id>/` | GET | Get details of a single event |
| `/api/events/<id>/book/` | POST | Book an event (authenticated) |
| `/api/bookings/` | GET | List user bookings |
| `/api/register/` | POST | Register new users |
| `/api/token/` | POST | get access and refersh token |
| `/api/token/refresh/` | POST | get refersh token |
| `/api/token/logout/` | POST | remove token and logout |


> 🔐 Token authentication is required for booking and viewing user-specific bookings.

---

## 🔐 Authentication

- After registration, use your credentials to get a token (if configured).
- Include the token in the header for protected routes:
  ```
  Authorization: Token <your-token>
  ```

---

## 🙋 Author

**Shahda Mohamed**  
🔗 [GitHub Profile](https://github.com/shahdamohamed)

---