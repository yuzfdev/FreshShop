# FreshShop 🌾

## Overview
FreshSop is a comprehensive e-commerce platform dedicated to providing high-quality art supplies, office essentials, and creative materials. Our platform connects consumers directly with trusted suppliers to ensure freshness and quality in every purchase.

## 🌟 Key Features

### Customer Experience
- **Real-time Stock Updates**: Shows in-stock, low-stock, or out-of-stock status for all products
- **Shopping Cart & Wishlist**: Easily save and purchase your favorite items

### Technical Features
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **User Authentication**: Secure login/signup with email verification
- **Order Management**: Track and manage current and past orders
- **Performance Optimization**: Fast loading times and efficient database queries

## 💻 Tech Stack

### Frontend
- **HTML5/CSS3**: Modern, semantic markup with advanced styling
- **Bootstrap 5**: Responsive grid system and UI components

### Backend
- **Django**: Robust Python web framework with built-in security features

### Database
- **MySQL 8.0**: Reliable relational database for product and user data storage

## 📊 Database Schema

### Core Models
- **Product**: name, category, description, price, stock, image
- **User**: username, email, password
- **Cart**: user, products, quantity

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9+
- pip
- virtualenv
- MySQL

### Local Development Setup
```bash
# Clone the repository
git clone https://github.com/yuzfdev/FreshShop.git
cd FreshShop

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django mysqlclient pillow

# Configure database
# Edit settings.py with your database credentials

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load demo data (optional)
python manage.py loaddata demo_data.json

# Start development server
python manage.py runserver
```
