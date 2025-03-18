
# Django Event Management API

This project was used to learn the Django REST Framework. It's an event management API, that allows to create events, purchase tickets for an event, and list payments made.

It includes auth, api versioning, and very modular and reusable pagination, filtering and ordering.

## Models

- Event
- Ticket
- Payment

## Running the project

### Cloning the repo:

    git clone https://github.com/Kurler3/django_event_mgnt_api.git

### Creating a virtual environment:

    pip install virtualenv
    python -m venv [venv_name]

### Activate the virtual environment:

    source [venv_name]/bin/activate

### Install dependencies:

    cd django_event_mgnt_api
    pip install -r requirements.txt

### Configuring the environmental variables:

    Create a .env file and fill in the following vars:

        - SECRET_KEY: This is the key django uses.
        - JWT_SIGNING_KEY: Key used to sign the auth tokens.

### Configure the database:

    python manage.py migrate

### Run the server:

    python manage.py runserver