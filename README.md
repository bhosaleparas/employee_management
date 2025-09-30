# Employee Management System

A modern, responsive web application for managing employee records with a clean and intuitive interface.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3-purple)
![Responsive](https://img.shields.io/badge/design-responsive-success)

## Overview

The Employee Management System is a Django-based web application that allows businesses to efficiently manage their employee records. It provides a complete CRUD (Create, Read, Update, Delete) interface with a modern, responsive design that works seamlessly across all devices.

## Features

### Core Functionality
- **Employee Dashboard** - View all employees in a clean, organized table
- **Add New Employees** - Simple form to add new employee records
- **Edit Employee Details** - Update existing employee information
- **Delete Employees** - Secure deletion with confirmation prompts
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices

### User Experience
- **Modern UI/UX** - Clean, professional interface with smooth animations
- **Intuitive Navigation** - Easy-to-use interface with clear action buttons
- **Visual Feedback** - Hover effects, loading states, and success messages
- **Accessibility** - Proper contrast ratios and keyboard navigation support

### Responsive Design
- **Mobile-First Approach** - Optimized for mobile devices
- **Flexible Layout** - Adapts to different screen sizes
- **Touch-Friendly** - Appropriately sized buttons and form elements

## Technology Stack

### Backend
- **Django** - Python web framework
- **SQLite/PostgreSQL** - Database (configurable)

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom styling with CSS variables
- **Bootstrap 5** - Responsive framework
- **Font Awesome** - Icons
- **JavaScript** - Interactive functionality


## Installation

### Prerequisites
- Python 3.8+
- Django 4.2+
- Modern web browser

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/employee-management-system.git
   cd employee-management-system

2. **Create virtual environment**

    ```bash
    python -m venv venv
    On Windows: venv\Scripts\activate # On Linux source venv/bin/activate(Linux)  


3. **Install Dependencies**

    ```bash
    cd employee_crud
    pip install requirments.txt

4. **Run migrations**

    ```bash
    python manage.py migrate


5. **Run development server**

    ```bash
    python manage.py runserver