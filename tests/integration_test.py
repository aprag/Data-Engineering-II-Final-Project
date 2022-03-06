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
    
    
    
    
def test_integration(client):
    p = {"inputedText":""} # testing function with post, and watch that we are calling the results page
    response = client.post("/",data=p)
    assert response.status_code == 200
    assert b'<h1>Welcome to the results page.</h1>' in response.data
    
