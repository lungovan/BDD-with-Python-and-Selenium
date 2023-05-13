
## Web Application Under Test
The website that is being tested by this framework is https://demo.guru99.com/test/upload/, a third-party application that contains a demo upload page.

## Test Framework
This project contains a Selenium Python test framework, implements the Page Object Model design pattern and utilises Pytest BDD.

### Tech stack
As this is a Python project, build and dependency management is handled by Pipenv, so there is a `Pipfile` (and associated `.lock` file) defining the versions of the dependencies:
* Python
* Selenium
* Pytest
* Pytest BDD
* Webdriver-Manager

### Project Structure
The project uses a standard structure:
* `assets` - This folder contains test files for features such as uploading
* `data`  - This folder contains test data json files that will need for tests that requires to run with multiple data values
* `features`  - This folder contains the Gherkin `.feature` files, one per website page.
* `pages` - The Page Object Model implementation of the individual website pages, one class file per page.
* `step_defs` - A collection of files containing the implementation of the steps from the BDD feature files.
* `config.json` - A JSON object used to define certain configuration options such as the browser, whether to run headless and the implicit wait timeout.
* `conftest.py` - This file contains methods to set up the browser (having read in the required parameters from the `config.json` file) and make that available to the page methods. Finally, steps that are common across multiple feature files (with the exception of the page title steps noted above) are contained within this file.

### Supported Browsers
The `conftest.py` module uses the Webdriver-Manager dependency to manage the various browser drivers. The `browser` Pytest fixture returns the relevant WebDriver instance for the chosen browser, with support for:
* Chrome - the default option
* Firefox

The browser to be used can be passed in via a Pytest command line parameter with a key of `browser`, defaulting to Chrome if no such property is specified.

The `headless` pproperty is used to determine whether the browser should run in headless mode.

### Setup and Run tests

#### Setup
Go to the directory in which the repo has been cloned.
Run commands:
`pip install pipenv` and `pipenv install`

#### Run tests
`pipenv run pytest` within the directory in which the repo has been cloned. 

The `browser` property can also be specified on the command line, e.g. `pipenv run pytest --browser Firefox` will run the test suite in Firefox.


### CI Pipeline
This repo contains a CI pipeline implemented using [GitHub Actions]. Any push to the `main` branch or any pull request on the `main` branch will trigger the pipeline, which runs in a Linux VM on the cloud within GitHub. The pipeline consists of two separate jobs which run in parallel:
* `run-tests-on-chrome`
* `run-tests-on-firefox`
  
Each job checks out the repo then runs the test suite on Chrome/Firefox via `pipenv run pytest` or `pipenv run pytest --browser Firefox`.

In addition to the automated triggers above, the CI pipeline has a manual trigger actionable by clicking "Run workflow" on the [Continuous Integration](https://github.com/lungovan/file-upload-test-bdd/actions/workflows/ci.yml) page. 
This allows the user to select the branch to run the pipeline on, so tests can be run on a branch without the need for a pull request. This option is only visible if you are the repo owner.