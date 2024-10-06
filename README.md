Vin_Inventory-Management-System-with-python-django-and-mysql-database
I build the entire Inventory Management System Dashboard. I demonstrated how to use template tags, extend on the template inheritance from lesson and watching class recordings.

README Notes for Django URL Configuration
Overview
This code snippet defines URL patterns for a Django application, mapping specific URL paths to their corresponding views. It organizes routes for managing a dashboard, staff details, products, and orders.

URL Patterns
Dashboard

Path: /dashboard/
View: views.index
Name: dashboard-index
Description: Displays the main dashboard page.
Staff Management

Path: /staff/

View: views.staff

Name: dashboard-staff

Description: Lists all staff members.

Detail View:

Path: /staff/detail/<int:pk>
View: views.staff_detail
Name: dashboard-staff-detail
Description: Shows detailed information for a specific staff member identified by their primary key (pk).
Product Management

Path: /product/

View: views.product

Name: dashboard-product

Description: Lists all products.

Delete Product:

Path: /product/delete/<int:pk>/
View: views.product_delete
Name: dashboard-product-delete
Description: Deletes a product identified by its primary key (pk).
Update Product:

Path: /product/update/<int:pk>/
View: views.product_update
Name: dashboard-product-update
Description: Updates details of a product identified by its primary key (pk).
Order Management

Path: /order/
View: views.order
Name: dashboard-order
Description: Displays the orders page.
User Logout

Path: /logout/
View: user_logout
Name: user-logout
Description: Handles user logout functionality.
Add Product

Path: /add-product/
View: add_product
Name: add_product
Description: Provides a form to add a new product.
Usage
Include this URL configuration in the main Django project’s urls.py using Django’s include() function.
Ensure that the corresponding views exist in the views.py file of the same application.
Notes
Use descriptive names for routes to enhance clarity when referencing them in templates and views.
Make sure to handle potential errors, such as invalid primary keys, in the views to improve user experience.
Dependencies
Django must be installed and configured properly.
Ensure that the views imported in this file (views.index, views.staff, etc.) are implemented in the views.py file.
README Notes for Django Views
Overview
This code provides views for a Django dashboard application that allows authenticated users to manage products and orders. It includes functionalities such as adding, updating, deleting products, viewing staff details, and managing orders.

Views
1. Dashboard Index
Function: index
URL: /dashboard/
Description: Displays the dashboard with counts of orders, products, and staff members. Users can submit new orders using the OrderForm.
Context Variables:
orders: List of all orders.
form: Instance of OrderForm.
products_count: Total number of products.
workers_count: Total number of staff members.
order_count: Total number of orders.
2. Staff Management
Function: staff
URL: /staff/
Description: Lists all staff members with counts of products and orders.
Context Variables:
workers: List of all staff members.
product_count: Total number of products.
orders_count: Total number of orders.
3. Staff Detail
Function: staff_detail
URL: /staff/detail/<int:pk>
Description: Displays detailed information for a specific staff member identified by their primary key (pk).
Context Variables:
workers: Details of the selected staff member.
4. Product Management
Function: product
URL: /product/
Description: Lists all products and allows users to add new products using the ProductForm.
Context Variables:
items: List of all products.
product_count: Total number of products.
orders_count: Total number of orders.
workers_count: Total number of staff members.
Notes: Ensure to fix the typo in redirect ('dahboard-product' should be 'dashboard-product').
5. Product Deletion
Function: product_delete
URL: /product/delete/<int:pk>/
Description: Deletes a product identified by its primary key (pk) after confirming the action.
Context Variables:
None specified; a confirmation page is rendered.
6. Product Update
Function: product_update
URL: /product/update/<int:pk>/
Description: Updates the details of a product identified by its primary key (pk).
Context Variables:
form: Instance of ProductForm pre-filled with the product's existing data.
7. Order Management
Function: order
URL: /order/
Description: Displays all orders along with counts of products and staff members.
Context Variables:
orders: List of all orders.
orders_count: Total number of orders.
product_count: Total number of products.
workers_count: Total number of staff members.
8. User Logout
Function: user_logout
URL: /logout/
Description: Logs out the user and redirects them to the login page.
9. Add Product
Function: add_product
URL: /add-product/
Description: Provides a form to add a new product. On successful form submission, it redirects to a success page.
Context Variables:
form: Instance of ProductForm.
Usage
Ensure all necessary models (Product, Order, and User) and forms (ProductForm, OrderForm) are defined in the corresponding files.
Include these views in the urls.py file of your Django application to make them accessible through specified URLs.
Dependencies
Django must be installed and properly configured.
User authentication is required for all views, except user_logout and add_product.
Error Handling
Consider adding error handling for cases where objects (e.g., Product, User) are not found in the database, particularly in staff_detail, product_delete, and product_update views.
README Notes for Django Models
Overview
This code defines the data models for a Django application focused on managing products and orders. It includes two primary models: Product and Order. The application uses Django's built-in User model for staff management.

Models
1. Product Model
Class: Product

Description: Represents a product with associated details.

Fields:

name: A CharField that stores the name of the product (max length: 100, nullable).
category: A CharField that stores the category of the product. Uses predefined choices (Stationary, Electronics, Food).
quantity: A PositiveIntegerField that indicates the available quantity of the product (nullable).
Meta Options:

verbose_name_plural: Sets the plural name for the model to "Products".
String Representation:

def __str__(self):
    return f'{self.name}-{self.quantity}'
This method returns a string representation of the product, showing its name and quantity.

2. Order Model
Class: Order

Description: Represents an order placed for a product by a staff member.

Fields:

product: A ForeignKey linking to the Product model. Uses CASCADE for deletion behavior, meaning if a product is deleted, the associated orders will also be deleted (nullable).
staff: A ForeignKey linking to the built-in User model. Uses CASCADE for deletion behavior (nullable).
order_quantity: A PositiveIntegerField that indicates the quantity of the product ordered (nullable).
date: A DateTimeField that records the date and time when the order was created, automatically set to now when the order is added.
Meta Options:

verbose_name_plural: Sets the plural name for the model to "Orders".
String Representation:

def __str__(self):
    staff_username = self.staff.username if self.staff else 'No Staff Assigned'
    return f'{self.product} ordered by {staff_username}'
This method returns a string representation of the order, showing the product and the staff member who placed the order, or indicating that no staff is assigned.

Usage
Include this model code in your models.py file within the relevant Django app.
Run migrations to create the corresponding database tables:
python manage.py makemigrations
python manage.py migrate
Notes
Ensure that the User model from django.contrib.auth.models is correctly set up and that users have been created in the database for the Order model to function properly.
Consider adding validation to ensure that order_quantity does not exceed the quantity available in the Product model.
Dependencies
Django must be installed and properly configured.
The application relies on Django's built-in authentication framework for managing staff users.
License
Include licensing information here if applicable.
README Notes for Django Forms
Overview
This code defines forms for the Product and Order models in a Django application. It uses Django's ModelForm class to create forms based on the models, enabling easy data entry and validation.

Forms
1. Product Form
Class: ProductForm
Description: A form for creating or updating Product instances.
Meta Options:
Model: Links to the Product model.
Fields: Specifies the fields to include in the form:
name: The name of the product.
category: The category of the product (with predefined choices).
quantity: The available quantity of the product.
Usage
To use the ProductForm, create an instance of the form in a view and pass it to a template for rendering. For example:

form = ProductForm(request.POST or None)
if form.is_valid():
    form.save()
2. Order Form
Class: OrderForm
Description: A form for creating or updating Order instances.
Meta Options:
Model: Links to the Order model.
Fields: Specifies the fields to include in the form:
product: The product being ordered (linked to the Product model).
order_quantity: The quantity of the product being ordered.
Usage
To use the OrderForm, create an instance of the form in a view similar to the ProductForm:

form = OrderForm(request.POST or None)
if form.is_valid():
    form.save()
Notes
Both forms automatically handle validation based on the model field definitions.
If any fields are required or have specific validation rules in the models, those rules will apply to the forms as well.
Dependencies
Django must be installed and properly configured.
Ensure the relevant models (Product and Order) are defined in the same application.
README Notes for Django Settings
Overview
This file contains the configuration settings for a Django project named DjangoIMS. It defines various settings related to the project's structure, database, applications, middleware, templates, static files, and more.

Key Sections
1. Basic Configuration
BASE_DIR: Defines the base directory for the project, allowing for easy path management.
SECRET_KEY: A secret key used for cryptographic signing; should be kept secret in production.
DEBUG: A boolean that controls debug mode; should be set to False in production for security reasons.
ALLOWED_HOSTS: A list of strings representing the host/domain names that this Django site can serve.
2. Application Definition
INSTALLED_APPS: Lists all Django applications included in the project, including default Django apps and custom apps like dashboard and user, along with crispy_forms for form styling.
3. Middleware
MIDDLEWARE: A list of middleware components that process requests and responses. Middleware can handle tasks such as security, session management, and authentication.
4. URL Configuration
ROOT_URLCONF: The module that defines the URL patterns for the project.
5. Templates
TEMPLATES: Configuration for template rendering, including backend options, directories for template files, and context processors.
6. WSGI Application
WSGI_APPLICATION: The WSGI application used for deployment.
7. Database Configuration
DATABASES: Defines the database settings; in this case, it uses SQLite for development.
8. Password Validation
AUTH_PASSWORD_VALIDATORS: A list of validators used to enforce password complexity and security.
9. Crispy Forms Configuration
CRISPY_TEMPLATE_PACK: Sets the template pack for crispy_forms. This is used for styling forms with Bootstrap 4.
10. Internationalization
LANGUAGE_CODE, TIME_ZONE: Define the language and timezone settings for the project.
USE_I18N, USE_TZ: Control the use of internationalization and timezone support.
11. Static Files
STATIC_URL: The URL prefix for static files.
STATICFILES_DIRS: Directories where Django will search for additional static files.
STATIC_ROOT: The absolute path to the directory where static files will be collected.
12. Media Files
MEDIA_ROOT: The absolute path to the directory for user-uploaded media files.
MEDIA_URL: The URL that handles the media served from MEDIA_ROOT.
13. Authentication
LOGIN_REDIRECT_URL: The URL to redirect to after a successful login.
LOGIN_URL: The URL to redirect to for login.
14. Email Configuration
EMAIL_BACKEND: The backend used for sending emails.
EMAIL_HOST, EMAIL_PORT: SMTP server configuration for sending emails.
EMAIL_HOST_USER, EMAIL_HOST_PASSWORD: Credentials for the email account used to send emails.
Notes
Security: Make sure to set DEBUG to False in production and use a secure method to manage the SECRET_KEY.
Sensitive Information: Avoid hardcoding sensitive information like email passwords in your settings file. Consider using environment variables or a secrets management service.
Dependencies
Ensure that Django is installed and that the specified apps (dashboard, user, crispy_forms, etc.) are correctly set up.
README Notes for Django URL Configuration
Overview
This file contains the URL routing configuration for the DjangoIMS project. It defines the URL patterns that map to specific views within the application, allowing users to navigate through different parts of the site.

URL Patterns
1. Admin Panel
Path: admin/
View: Admin interface provided by Django.
Usage: Access the Django admin panel for managing the application.
2. Dashboard
Path: '' (root path)
View: Includes the URL patterns defined in the dashboard app.
Usage: Directs users to the main dashboard functionality.
3. User Registration and Profile
Path: register/
View: user_view.register
Name: user-register
Path: profile/
View: user_view.profile
Name: user-profile
Path: profile/update/
View: user_view.profile_update
Name: user-profile-update
4. User Authentication
Login:

Path: '' (root path)
View: Django's built-in LoginView, customized with a specific template.
Name: user-login
Logout:

Path: logout/
View: Django's built-in LogoutView, customized with a specific template.
Name: user-logout
5. Password Management
Password Reset:
Path: password_reset/

View: PasswordResetView
Name: password_reset
Path: password_reset_done/

View: PasswordChangeDoneView
Name: password_reset_done
Path: password_reset_confirm/<uidb64>/<token>/

View: PasswordResetConfirmView
Name: password_reset_confirm
Path: password_reset_complete/

View: PasswordResetCompleteView
Name: password_reset_complete
6. Media Files
Static Serving:
The + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) line ensures that media files are served correctly during development.
Notes
The urlpatterns list is structured to facilitate easy addition or modification of URL patterns.
It uses Django’s built-in authentication views for user login and password management, ensuring secure and standardized handling of these processes.
Ensure that the corresponding views in the user app are implemented correctly to match the URLs defined here.
Dependencies
Make sure that the user and dashboard apps are properly configured and that their views are implemented as expected.
The project must have Django installed and configured.
