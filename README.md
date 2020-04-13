# TestWebApp
A Tutorial to guide testing on WebApp and enable CI/CD. The repository uses Python 3x and Django for demonstration.

First we will develop a simple web application that deals with funding for start up projects and then we shall apply testing methods to make the web application rock solid.

## Types of Tests
* Document based testing
* Unit Testing
* Integration Testing
* Functional testing.

## Installations
* Install Python 3.7.x if needed
> mkdir learn_django_test
> cd learn_django_test
> git clone https://github.com/vatsamail/TestWebApp.git
> virtualenv --no-site-packages [--python=<path to python 3.x>] env
> source env/bin/activate.csh #linux
> env\Scrips\activate #windows
> cd TestWebApp
> pip install -r requirements.txt
> cd startupmoney
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
> python manage.py test

Note: db.sqlite3 ships with the git. To access the admin pages- user: admin, password: superuser

## Links:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/admin/doc/

## Doc Tests

## Unit Tests
The idea of testing modules and atomic entities independently.
Running unit tests:

>python manage.py test handlemoney
### URL tests
- Refer tests/test_urls.py
### View tests
- Refer tests/test_views.py
### Form tests
- Refer tests/test_forms.py
### Model tests
- Refer tests/test_models.py
## Integration Tests

## Functional Tests

## References
* https://pypi.org/project/robotframework-djangolibrary
* https://github.com/TheDumbfounds/budget-application-tutorial
* https://docs.djangoproject.com/en/2.1/topics/testing
* https://django-testing-docs.readthedocs.io/en/latest/basic_doctests.html
