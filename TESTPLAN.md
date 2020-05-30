## Test Plan
This document details the way tests will be run for the application.

## Exploratory Testing
Check out the app and explore how it works.
This is done by:
* Running the app locally
* Testing all functionalities of the app
* ex) Does this button work the way it's supposed to?
* ex) Is it possible to input invalid values and cause the result to not make sense?

## Unit Testing
Using python's integrated unittest module:

* Test run.py flask program by checking if each page loads correctly
* Test api.py by checking that each function functions as intended

## Automated Testing
The whole test suite can be run from the root project directory by:

1. Access the virtual environment
* `source env/bin/activate`

2. Run all tests
* `python3 -m nose2`

nose2 also has the `--verbose` optional tag to see the list of tests run.

There are two test files, one testing the flask routes and one testing the api.

To run each test file seperately:

1. Access the virtual environment
* `source env/bin/activate`

2. Install dependencies and modules
* `pip3 install -e .`

3. Run test_flask.py
* `python3 test/test_flask.py`

or

3. Run test_api.py
* `python3 test/test_api.py`

Both `python3 test/test_{module}.py` tests have an optional verbosity option 
* `python3 test/test_flask.py -v`

## Coverage
Using python's installed coverage.py module:

1. Access the virtual environment
* `source env/bin/activate`

2. Install dependencies and modules
* `pip3 install -e .`

3. Run coverage with test file
* `coverage run --source paint_calculator test/test_api.py`

4. Run coverage report
* `coverage report`

## Problems Encountered
I had a bit of trouble at first on getting the app itself to run, but after moving the config.py file it worked.

I was doing a lot of code outside of a virtual environment, then I decided to change everything to a virtual environment. I added the virtual environment in the repo, so that all dependencies and modules that were needed for testing were already available for anybody's machine.

I also had a little trouble with getting to use flask's test_client() function. I didn't realize that I was importing the incorrect module of the app. After looking at each of the files in the app and seeing what gets requested in certain actions of the app, I started to understand the app more.

I didn't get to test all of the things I wanted for the flask app. I wanted to see if I would be able to see the contents of result, but I realized that I couldn't see all of the information if I just called for post('results',...). Because when you press the "See Results" button, it makes a call to /api/v4/calculate. So I decided to just test the api functions seperately.

This was a fun exercise that allowed me to familiarize myself with python and some features of its testing suite.
