# Sales Order & Inventory Management System

## Project Overview

This project is a simplified **Sales Order and Inventory Management System** built using **Django and Django REST Framework**.
It simulates a B2B backend system where dealers can place orders for products while the system manages inventory and order status automatically.

The system ensures proper **stock validation, order status transitions, and inventory management**, preventing over-ordering and maintaining accurate stock levels.

This project was implemented as part of the **Vikmo Fresher Developer Assignment**.


# Features Implemented

### Product Management

* Create, update, delete, and list products
* Each product has a **unique SKU**
* Product pricing and description support
* Product stock visible through inventory

### Dealer Management

* Create and manage dealer/customer information
* Dealers can place multiple orders

### Inventory Management

* Each product has **exactly one inventory record**
* Admin-only APIs for viewing and updating inventory
* Stock automatically deducted when orders are confirmed

### Order Management

* Dealers can create **draft orders**
* Orders contain multiple **order items**
* Automatic **line total and order total calculations**

### Order Status Flow

Orders follow strict status transitions:


Draft → Confirmed → Delivered


Rules:

* Draft orders can be edited
* Confirmed orders cannot be modified
* Delivered orders are final

### Stock Validation

Before confirming an order:

* System checks available inventory
* Prevents ordering more than available stock
* Returns clear error messages if stock is insufficient

Example error:


Insufficient stock for Brake Pad. Available: 5, Requested: 10


# Tech Stack

Backend:

* Python 3
* Django
* Django REST Framework

Database:

* PostgreSQL

Tools:

* Postman (API Testing)
* Git & GitHub


# Project Structure


vikmo-inventory-system
│
├── core
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│
├── vikmo_inventory
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── manage.py



# Setup Instructions

## 1. Clone the repository


git clone https://github.com/Mohammed-Najmudeen-K/vikmo-inventory-system.git
cd vikmo-inventory-system

## 2. Install dependencies


pip install -r requirements.txt




## 3. Configure Environment Variables

Create a `.env` file in the root directory:


SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=vikmo_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432




## 4. Run migrations

python manage.py makemigrations
python manage.py migrate




## 6. Create admin user


python manage.py createsuperuser




## 7. Run the server


python manage.py runserver


Server will start at:


http://127.0.0.1:8000




# API Documentation

## Products

Create Product


POST /api/products/


Example Request


{
"name": "Brake Pad",
"sku": "BP001",
"price": 500,
"description": "High quality brake pad"
}




List Products


GET /api/products/




## Dealers

Create Dealer

POST /api/dealers/


Example


{
"name": "ABC Motors",
"email": "abc@example.com",
"phone": "9876543210",
"address": "Chennai"
}


## Orders

Create Order


POST /api/orders/


Example

{
"dealer": 1,
"items": [
{
"product": 1,
"quantity": 10,
"unit_price": 500
}
]
}


Confirm Order

POST /api/orders/{id}/confirm/

When confirmed:

* Stock is validated
* Inventory is reduced



Deliver Order

POST /api/orders/{id}/deliver/

## Inventory (Admin Only)

List inventory


GET /api/inventory/


Update stock


PUT /api/inventory/{product_id}/


Example


{
"quantity": 100
}


# Business Rules Implemented

### Stock Validation

Order confirmation checks stock availability.

### Automatic Stock Deduction

Stock is deducted only when order changes from:


Draft → Confirmed


### Order Editing Restrictions

| Status    | Editable |
| --------- | -------- |
| Draft     | Yes      |
| Confirmed | No       |
| Delivered | No       |



# Sample Test Scenario

### Successful Order Flow

1. Create Product **Brake Pad**
2. Add Inventory **100 units**
3. Create Dealer **ABC Motors**
4. Create Draft Order for **10 units**
5. Confirm Order → Stock becomes **90**
6. Deliver Order → Order completed



### Insufficient Stock Scenario

Product stock: **5**

Order request: **10**

Result:

Error: Insufficient stock for Brake Pad. Available: 5, Requested: 10




# Assumptions

* Each product has exactly **one inventory record**
* Inventory updates are **admin only**
* Order totals are calculated automatically
* Stock cannot go below zero



# API Testing

All APIs were tested using **Postman**.

A Postman collection can be included in the repository for easy testing.

