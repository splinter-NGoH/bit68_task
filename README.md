# bit68_project

bit68_task

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy bit68_project

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### docker commands
build:

	$ docker compose -f local.yml up --build -d --remove-orphans

up:

	$ docker compose -f local.yml up -d

down:

	$ docker compose -f local.yml down

logs:

	$ docker compose -f local.yml logs

migrate:

	$ docker compose -f local.yml run --rm api python3 manage.py migrate

makemigrations:

	$ docker compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:

	$ docker compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:

	$ docker compose -f local.yml run --rm api python3 manage.py createsuperuser

down-v:

	$ docker compose -f local.yml down -v



authors-db:

	$ docker compose -f local.yml exec {postgres_servicecname} psql --username=alphaogilo --dbname=authors-live

flake8:

	$ docker compose -f local.yml exec api flake8 .

black-check:

	$ docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:

	$ docker compose -f local.yml exec api black --diff --exclude=migrations .

black:

	$ docker compose -f local.yml exec api black --exclude=migrations .

isort-check:

	$ docker compose -f local.yml exec api isort . --check-only --skip env --skip migrations

isort-diff:

	$ docker compose -f local.yml exec api isort . --diff --skip env --skip migrations

isort:

	$ docker compose -f local.yml exec api isort . --skip env --skip migrations	




#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application .

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
