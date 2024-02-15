# Django-Gallery

# Image Gallery Project

## Overview
This is a Django web application for managing and displaying an image gallery. Users can sign up, log in, upload images, and view them in the gallery.

## Features
- User authentication: Users can sign up, log in, and log out.
- Image upload: Authenticated users can upload images to the gallery.
- Gallery view: Only the uploader can view images uploaded by them.
- Image details: Each image displays details such as the uploader's username and upload timestamp.
- Responsive design: The gallery is designed to work well on desktop and mobile devices.

## Setup
1. **Clone the repository:**
git clone <https://github.com/eshanpandey/Django-Gallery.git>

2. **Install dependencies:**
pip install -r requirements.txt

3. **Run migrations:**
python manage.py migrate


4. **Start the development server:**
python manage.py runserver


5. **Access the application:**
Visit `http://localhost:8000/gallery` in your web browser.

## Technologies Used
- Django
- HTML/CSS
- Bootstrap (optional for styling)
- SQLite (default database)

## Folder Structure
- **gallery/**: Django app directory containing models, views, and templates.
- **media/**: Directory to store uploaded images.
- **templates/**: HTML templates for rendering views.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

   


