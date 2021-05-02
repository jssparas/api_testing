# api_testing

Python version - 3.6

Install requirements.txt by running - 
`pip install requirements.txt`

## run stub endpoint
`gunicorn api_stub:api`

## in new terminal tab, run pytest to test API endpoint
`pytest`

API Endpoint tested - /emojis

## Answers to the questions
### 1. What concerns would you have from a testing perspective?
* Firstly, would do an impact analysis of the project, like what all can be the use-cases of these API endpoints.
* What could be the scenarios wherein the user will be using these APIs
* What could be the load factor, performance hits, etc

### 2. How would you go about tackling the QA for this work?
* We need to understand the scope of the project, types of testing methodologies (functional or non-functional)
* functional like how does an API endpoint behaves given different user-inputs, what are the different outputs we get 
with different sets of inputs.
* non-functional like performance testing, hitting the API endpoint with large number of simultaenous requests and check the response time 
of the endpoint, how fast the endpoint is returning the result

### 3. What sort of tests would be worth describing or worth automating?
* We can always automate tests that will be required as a part of regression suite i.e. need to be tested in every version release
like checking various reponses (happy path tests), basically the behaviour which API endpoints must show in ideal case.
* And also some negative tests, like if an API is supposed not to implement POST request, then that automated test must be there with 404 status assertion

### 4. What tools would you use?
I have used following tools: 
* falcon framework (https://falcon.readthedocs.io/en/stable/index.html) to implement the stub endpoint
* Python (3.6)
* gunicorn to run the stub on local server
* pytest library to write api tests
* requests library to perform REST calls on the endpoint
