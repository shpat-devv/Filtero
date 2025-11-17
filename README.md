# Filtero

Filtero is a simple and fun platform for applying preset filters to your images. It’s built with Django on the backend and React on the frontend, and the whole goal is to make it super easy for you to upload a picture, pick a filter, and download something cooler than what you started with. More advanced editing features are coming soon, so this project will keep growing over time.

---

## How it works?

When you open the frontend, it will automatically take you to the login page (unless you’re already logged in). To make the connection between the frontend and backend work, you need to create a .env file inside the root of the frontend and set a VITE_API_URL.

```Example frontend .env
VITE_API_URL = "http://127.0.0.1:8000/
```

 This would work if the backend is running locally on the port 8000 (which is the default for django). The frontend will use that address to communicate with the backend via urls, the main endpoints are:

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
- [FAQ](#faq)
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
    /api         # Django app
        /migrations    # Database migrations
        /views         # API views
        /models        # Database models
        /serializers   # Data serializers
        /image_process  # Image processing logic
    /backend      # Django project settings
        /settings.py  # Project settings
        /urls.py      # URL configurations
    manage.py    # Django management script
    sqlite.db    # SQLite database file

/frontend     # React app
    /public
        default.jpeg  # Default image used in the app
    /src
        /components  # React components
        /pages       # React pages
        /styles      # CSS styles
        constants.js # Variables like ACCESS_TOKEN, REFRESH_TOKEN
        api.js       # Axios API calls
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

```
cd backend/api/image_process
make filter
```
---

## FAQ
**Q: Can I add my own filters?**
A: Yes, inside the source code in the `backend/api/image_process` directory you can edit the c files and add any filter preset you want.
**Q: Is there a limit to the image size I can upload?**
A: Currently, there is no limit, but very large images may take longer to process.
**Q: How secure is my data?**
A: This uses JWT for authentication and follow best practices to ensure your data is secure.   
**Q: Why do i need a .env file?**
A: Because hardcoding URLs sucks and breaks things when you deploy. Also security risk.
**Q: What image formats are supported?**
A: Currently i have tested it with jpeg, png and bmp formats.
**Q: Where are my images stored?**
A: Uploaded images are stored in the `media/` directory and immediately deleted after processing for privacy (its to save space actually).
**Q: How can i host this project?**
A: Im hosting it using vercel for the frontend and render for the backend, They both have free tiers that work great for small projects like this.
---

## License

This project was made for fun, do whatever you want with it!.

---
