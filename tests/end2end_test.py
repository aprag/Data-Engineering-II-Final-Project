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

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'<h1>Toxicity</h1>' in response.data
    assert b'<title>Data Engineering II</title>' in response.data
    assert b'<h1>Toxicity</h1>' in response.data
    assert b'The application is a toxicity monitor, where the user inputs a piece of text' in response.data

def test_resultpage(client):
    p = {"inputedText":""} # testing function with post, and watch that we are calling the results page
    response = client.post("/",data=p)
    assert response.status_code == 200
    assert b'<h1>This is the results page.</h1>' in response.data
    
def test_result(client):
    #the utility of this function is just to detail that we obtain the result we are waiting for
    p = {"inputedText":"dumb"}
    response = client.post("/", data=p)
    
    tox = b'Toxicity : 0.96'
    sevtox = b'Severe Toxicity : 0.02'
    obs =b'Obscene : 0.55'
    threat = b'Threat : 0.0'
    insult = b'Insult : 0.88'
    idAt = b'Identity attack : 0.02'
    
    assert tox in response.data
    assert sevtox in response.data
    assert obs in response.data
    assert threat in response.data
    assert insult in response.data
    assert idAt in response.data
    