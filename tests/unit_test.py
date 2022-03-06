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
    
def test_unit_null(client):
    p = {"inputedText":"Hello World"} # here, we are testing the result with a not toxic sentence
    response = client.post("/",data=p)
    assert b'<li class="list-group-item">Toxicity : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Severe Toxicity : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Obscene : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Threat : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Insult : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Identity attack : 0.0 </li>' in response.data
  ## we know that this text is marked 0 on all criteria
  
def test_unit_tox(client):
    p = {"inputedText":"fuck"} # here, we are testing the result with a toxic text
    response = client.post("/",data=p)
    # we know that the text we input will output the following result
    assert b'<li class="list-group-item">Toxicity : 0.99 </li>' in response.data
    assert b'<li class="list-group-item">Severe Toxicity : 0.25 </li>' in response.data
    assert b'<li class="list-group-item">Obscene : 0.99 </li>' in response.data
    assert b'<li class="list-group-item">Threat : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Insult : 0.32 </li>' in response.data
    assert b'<li class="list-group-item">Identity attack : 0.0 </li>' in response.data
    

        

    
