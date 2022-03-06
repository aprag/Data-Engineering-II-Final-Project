import pytest
from src.app import app
from flask import url_for

@pytest.fixture
def client():
    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    return client

def test_index(client):
    var = client.get('/')
    assert var.status_code == 200


# we want to test the application end to end
# so firstly we will verify that when we go on the main page, we obtain the main page
# after that, we will run the application with a sentence with a known result and verify that the entire page is what we want to obtain
# Also, during the last verification the results of toxicity percentage will be verify as well
def test_appCall(client):
    resultfile = open('./homepageresult.txt').read() #this is the file containing the response we are waiting for
    
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == resultfile

def test_run(client):
    resultfile = open('./runpageresult.txt').read()
    
    p = {"inputedText":"Hello, my name is Goldy and i want to say to you that i appreciate the fact you are an asshole."}
    response = client.post("/", data=p)
    assert response.status_code == 200
    assert response.data.decode() == resultfile
    
def test_result(client):
    #the utility of this function is just to detail that we obtain the result we are waiting for
    p = {"inputedText":"Hello, my name is Goldy and i want to say to you that i appreciate the fact you are an asshole."}
    response = client.post("/", data=p)
    
    tox = b'Toxicity : 0.93'
    sevtox = b'Severe Toxicity : 0.03'
    obs =b'Obscene : 0.84'
    threat = b'Threat : 0.0'
    insult = b'Insult : 0.82'
    idAt = b'Identity attack : 0.01'
    
    assert tox in response.data
    assert sevtox in response.data
    assert obs in response.data
    assert threat in response.data
    assert insult in response.data
    assert idAt in response.data
    
