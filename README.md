# tdd_django_pytest

# Learning Links
- Udemy course - [Learn Pytest by building a full Django application with a Continuous Integration system, software testing best practices](https://sparknz.udemy.com/course/pytest-course/learn/lecture/23536728#overview)
- [Course Repository on bitbucket](https://bitbucket.org/e-marco/my-pytest-course/src/master/)
- [Pytest Documentation Home page](https://docs.pytest.org/en/stable/)
- [Pytest Markers](https://docs.pytest.org/en/stable/example/markers.html)
- [Pytest Skip & XFail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [Pytest Parametrize Fixtures](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Pytest Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)

# Misc links
[Website by Eden Marco](http://www.israeltechcompanies.com)

# Differences from Course
1. Repo : Github instead of bitbucket
1. 

# Command Line commands
## Run on current directory 
pytest .

## Run on current directory and verbose  output
pytest . -v

## Run on current directory, verbose  output and suppress warnings
pytest . -v -p no:warnings

## Run only those with customer marks ("slow" here)
pytest . -v -p no:warnings -m slow

# Run tests that are NOT marked "slow"
pytest . -v  -m "not slow"

# Make pytest print 
pytest . -v -s

# Commands used to create backend
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
1. Generate project : ./venv/bin/django-admin startproject coronavstech .
1. Migrations : python3 manage.py makemigrations
1. Migrations : python3 manage.py migrate
1. Create admin user : python3 manage.py createsuperuser (vrbabu)
1. Start server : python3 manage.py runserver
1. Create app : python3 manage.py startapp companies