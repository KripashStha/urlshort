# URL Shortener

A simple URL shortener web application built with Django. Users can create short links, track clicks, and manage their URLs.

# Hosted at:

kripash.pythonanywhere.com

## Features

- User registration and login
- Create short URLs from long links
- Custom short codes (optional)
- Expiration time for URLs (optional)
- Click tracking / analytics
- Edit and delete your URLs
- Responsive design

## Additional Features

### Custom Short URLs
Users can set their own custom short code instead of getting a random one. For example, instead of `abc123`, you can make it `mylink`. The system checks if the custom code is already taken.

### URL Expiration
When creating a short URL, users can set an expiration time:
- Never (default)
- 1 Hour
- 1 Day
- 1 Week
- 1 Month

After expiration, the short link shows an "expired" page instead of redirecting.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/url-shortner.git
cd url-shortner
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

On Windows:
```bash
venv\Scripts\activate
```

On Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Go to source folder

```bash
cd src
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the server

```bash
python manage.py runserver
```

### 8. Open in browser

Go to `http://127.0.0.1:8000`

## How to Use

1. Register a new account or login
2. Click "Create URL" in the navbar
3. Enter your long URL
4. (Optional) Enter a custom short code
5. (Optional) Select expiration time
6. Click "Shorten URL"
7. Copy and use your short link!

## Screenshots

### Home Page
The landing page with links to login or register.
<img width="1280" height="712" alt="image" src="https://github.com/user-attachments/assets/81b9d548-1dee-4568-a8ae-ce735568da81" />

### Create URL
Form to enter long URL, optional custom code, and expiration time.
<img width="977" height="527" alt="image" src="https://github.com/user-attachments/assets/d23bca9e-9d2d-4b07-b797-29006a6eebdd" />

### My URLs
Dashboard showing all your created short URLs with click counts.
<img width="1003" height="499" alt="image" src="https://github.com/user-attachments/assets/8d5dd2e8-01c9-4fc6-80de-202ffd644c32" />

## Tech Stack

- Python
- Django
- SQLite (default database)
- Bootstrap 4 (styling)
- HTML/CSS
