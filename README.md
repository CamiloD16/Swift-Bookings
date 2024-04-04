# Swift-Bookings

This Django application is designed to manage the storage of a bookshop, this app provides a convenient way to organize and track your book inventory.

## Features

- **Book Management**: Add, edit, and delete books in your inventory.
- **Category Management**: Organize books into different categories for easy browsing.
- **Search Functionality**: Quickly find books by title, author, or category.
- **User Authentication**: Secure your data with user authentication and authorization.
- **User and Admin Roles**: Users can browse, search, and request to borrow books. Admins have access to additional features such as managing user requests and updating book availability.
- **Responsive Design**: Access the app from any device with its responsive design.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/CamiloD16/Swift-Bookings
    ```

2. Navigate to the project directory:

    ```
    cd book-storage-management
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Django migrations to set up the database:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

6. Access the application by visiting `http://localhost:8000` in your web browser.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.