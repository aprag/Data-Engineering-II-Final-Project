import time

import pytest
from src.app import app
from flask import url_for

start_time = time.time()
total_elapsed_time = 0
number_of_request = 0

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


def text_file(number_requ, timer):
    if(number_requ==100):
        f = open("./result.txt", "a")
        f.write(timer)
        f.write("we have :" + str(int(number_requ)) + " Requests\n")
        f.close()
        
    
    
@pytest.mark.parametrize('execution_number', range(100))
def test_stress(client, execution_number):
    global start_time
    global total_elapsed_time
    global number_of_request
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    total_elapsed_time = total_elapsed_time + elapsed_time
    status = client.get('/')

    assert status.status_code == 200
    number_of_request += 1

    monitoringTime = "Finished in: " + str(int(total_elapsed_time))  + " seconds\n"
    text_file(number_of_request,monitoringTime)
    
    
        
