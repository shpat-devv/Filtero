# Filtero

Filtero is a simple and fun platform for applying preset filters to your images. It’s built with Django on the backend and React on the frontend.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Incoming Updates](#incoming-updates)
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

## Planning

Filtero is just meant to be a fun full stack project to be used in my portfolio. Basically its a platform where users can create accounts, select photos to apply filters, and then view/manage all the images.

The important parts are that the user handling works, that the image filtering works and that everything gets stored. I visualize a modern interface, where after login the user can select an image (that meets criteria). That image gets sent to the django backend, where it will be converted to gimp and applied the filter using the C program. Afterwards the image gets uploaded and stored on an s3 bucket? specific to the user

backend:

    user
        allow user creations
        dissallow duplications
        handle jwt tokens
    image
        receive images
        apply filter using C program
        store in s3 bucket
        send url back to user
        let user download and do whatever
    extra



## License

This project was made for fun, do whatever you want with it!.

---
