# tdd_django_pytest

# Learing Links
- Udemy course - [Learn Pytest by building a full Django application with a Continuous Integration system, software testing best practices](https://sparknz.udemy.com/course/pytest-course/learn/lecture/23536728#overview)
- [Course Repository on bitbucket](https://bitbucket.org/e-marco/my-pytest-course/src/master/)
- [Pytest Documentation Home page](https://docs.pytest.org/en/stable/)
- [Pytest Markers](https://docs.pytest.org/en/stable/example/markers.html)
- [Pytest Skip & XFail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [Pytest Parametrize Fixtures](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Pytest Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)

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
