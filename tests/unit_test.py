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

    
def test_unit_null(client):
    p = {"inputedText":"Is it ok for you"} 
    response = client.post("/",data=p)
    assert b'<li class="list-group-item">Toxicity : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Severe Toxicity : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Obscene : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Threat : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Insult : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Identity attack : 0.0 </li>' in response.data
  
def test_unit_tox(client):
    p = {"inputedText":"dumb"} 
    response = client.post("/",data=p)
    assert b'<li class="list-group-item">Toxicity : 0.96 </li>' in response.data
    assert b'<li class="list-group-item">Severe Toxicity : 0.02 </li>' in response.data
    assert b'<li class="list-group-item">Obscene : 0.55 </li>' in response.data
    assert b'<li class="list-group-item">Threat : 0.0 </li>' in response.data
    assert b'<li class="list-group-item">Insult : 0.88 </li>' in response.data
    assert b'<li class="list-group-item">Identity attack : 0.02 </li>' in response.data
    

def test_index(client):
    var = client.get('/')
    assert var.status_code == 200        

    
