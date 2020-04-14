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

Note: db.sqlite3 ships with the git. To access the admin pages- _user: admin, password: superuser_

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
- Refer handlemoney/tests/test_urls.py
### View tests
- Refer handlemoney/tests/test_views.py
### Form tests
- Refer handlemoney/tests/test_forms.py
### Model tests
- Refer handlemoney/tests/test_models.py

## Integration Tests

## Functional Tests
- make chrome browser as the default browser
- install chromedriver. The version of the chrome can be found in the "About" section in the settings. Download the driver accordingly.
- copy the chromedriver.exe to functional_tests/ folder. For linux, use appropriate binary.
- Refer functional_tests/test_project_list_page.py

>python manage.py test functional_tests

##### To run all the tests, simply execute _python manage.py test_
## References
* https://pypi.org/project/robotframework-djangolibrary
* https://github.com/TheDumbfounds/budget-application-tutorial
* https://docs.djangoproject.com/en/2.1/topics/testing
* https://django-testing-docs.readthedocs.io/en/latest/basic_doctests.html
* https://selenium-python.readthedocs.io/getting-started.html
