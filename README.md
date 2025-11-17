# Filtero

Filtero is a user-friendly platform for applying preset filters to your images, with advanced image editing features coming soon. Built with Django (backend) and React (frontend), Filtero makes it easy to enhance your photos and share your creativity.

---

## How it works?

First you have the frontend which my default sends you to the login page (if you're not already logged in). To have a working connection you need to create a .env file inside the root of the frontend and set the VITE_API_URL to a value. EXAMPLE:

```
VITE_API_URL = "http://127.0.0.1:8000/
```

 This would work if the backend is running locally on the port 8000 (which is the default for django). The frontend will use that address to communicate with the backend via urls, the main urls are:

```
/api/user/register/  # will register new user
/api/token/          # will authenticate user using a token
/api/token/refresh/  # will refresh the token of an authenticated user
/api/image/          # will accept images and send the filtered image back
```

To communicate with those urls i made an api.js file in src folder which uses axios for all the communication

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Error Handling](#error-handling)
- [License](#license)

---

## Features

- **Preset Filters:** Instantly apply a variety of filters to your images.
- **Image Upload:** Upload images directly from your device.
- **Download & Share:** Download your edited images or share them online.
- **Upcoming:** Full-featured image editing tools.

---

## Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/)
- **Frontend:** [React](https://react.dev/)
- **Database:** SQLite
- **APIs:** RESTful, axios
- **Authentication:** JWT

---

## Installation

To install and setup Filtero run these commands:

```clone project using git
git clone https://github.com/shpat-devv/Filtero.git
cd Filtero
```

```backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

```frontend setup
cd ../frontend
npm install
npm run dev
```

---

### Environment Variables

Create `.env` files in both `backend/` and `frontend/` directories.

Example config for backend .env:

```
SECRET_KEY = 'example key'
DEBUG = True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Example config for frontend.env
```
/api/user/register/  # will register new user
/api/token/          # will authenticate user using a token
/api/token/refresh/  # will refresh the token of an authenticated user
/api/image/          # will accept images and send the filtered image back
```

---

## Project Structure

```
/backend      # Django project
/frontend     # React app
```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## Error Handling

If you get any missing environment variable errors, make sure you have created the .env files in both backend and frontend with the correct variables as shown above.

If you encounter issues about missing packages, ensure you have installed all dependencies shown above.

If you get a database error, ensure you have run the migrations for the backend.

If you get a missing file error like this:

```FileNotFoundError: [Errno 2] No such file or directory: '/Users/your_user/Documents/Code/Python/Filtero/backend/api/image_process/filter'```

That means the program used for the image processing is missing. You can compile it from source using these commands:

```cd backend/api/image_process
make filter
```
---

## License

This project was made for fun, do whatever you want with it!.

---
