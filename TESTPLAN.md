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

* `source env/bin/activate`
* `python3 -m nose2`

nose2 also has the `--verbose` optional tag to see the list of tests run
