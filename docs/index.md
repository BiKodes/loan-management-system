# loan-management-system

[![Build Status](https://travis-ci.org/BikoCodes/loan-management-system.svg?branch=master)](https://travis-ci.org/BikoCodes/loan-management-system)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Customers loan management system for clients applying loans online and approval being processed online. It helps to reduce the queing factor during loan processing period.. Check out the project's [documentation](http://BikoCodes.github.io/loan-management-system/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```
