Cookiecutter Django Webpack
=======================

STILL UNDER DEVELOPMENT
-----------------------

Cookiecutter Django Webpack can be used in production scenarios only if you know how it Works.
Please use this at your own discretion.

TODO List:
---------
* Seamless Docker-Compose/Docker Integration for Django + Webpack
* Abstracting Webpack Builds and adding conditional operations with respect to Gulp/Docker..etc.
* Supporting 100% Coverage & Tests
* Make Documentation

Powered by Cookiecutter_, Cookiecutter Django is a framework for jumpstarting
production-ready Django projects quickly.

* Documentation for Pydanny's Cookiecutter Django: https://cookiecutter-django.readthedocs.io/en/latest/
* See Troubleshooting_ for common errors and obstacles
* If you have problems with Cookiecutter Django, please open issues_ don't send
  emails to the me.

Features Built by pydanny & Me (That Work)
------------------------------------------

* For Django 2.1+
* Works with Python 3.6+
* Basic Webpack Configuration and setup
* Twitter Bootstrap_ v4.3.1 (`maintained Foundation fork`_ also available)
* 12-Factor_ based settings via django-environ_
* Secure by default. We believe in SSL.
* Optimized development and production settings
* Registration via django-allauth_
* Comes with custom user model ready to go
* Optional custom static build using Gulp and livereload
* Send emails via Anymail_ (using Mailgun_ by default, but switchable)
* Media storage using Amazon S3
* Docker support using docker-compose_ for development and production (using Caddy_ with LetsEncrypt_ support)
* Procfile_ for deploying to Heroku
* Instructions for deploying to PythonAnywhere_
* Run tests with unittest or py.test
* Customizable PostgreSQL version

For More info:
- https://cookiecutter-django.readthedocs.io/en/latest/