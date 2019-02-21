Cookiecutter Django Webpack
=======================

STILL UNDER DEVELOPMENT
-----------------------

Cookiecutter Django Webpack can be used in production scenarios only if you know how it Works.
Please use this at your own discretion.

Basic Webpack Configuration works.
Cookiecutter Django Webpack ships with bootstrap "4.3.1".

Usage
---------

Note: Use a Virtual Env to setup your projects.

* Installation
    $ cookiecutter https://github.com/kiran-capoor94/cookiecutter-django-webpack
* Use default for setup options.
* Enter the project directory where package.json file is
    $ cd project_slug/
* Install Node Dependencies
    $ npm install
* Run Webpack in Dev Environment with live compilation of your static files
    $ npm run watch
* In a separate terminal, run the django sever
    $ python manage.py runserver_plus 0.0.0.0:8000

TODO List:
---------
* Seamless Docker-Compose/Docker Integration for Django + Webpack
* Abstracting Webpack Builds and adding conditional operations with respect to Gulp/Docker..etc.
* Supporting 100% Coverage & Tests
* Make Documentation

Powered by Cookiecutter Django, Cookiecutter Django Webpack is a framework for jumpstarting
production-ready Django projects quickly.

* Documentation for Pydanny's Cookiecutter Django: https://cookiecutter-django.readthedocs.io/en/latest/
* See Troubleshooting for common errors and obstacles
* If you have problems with Cookiecutter Django, please open issues don't send
  emails to the me.

For More info:
- https://cookiecutter-django.readthedocs.io/en/latest/