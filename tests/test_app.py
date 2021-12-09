from flaskr import create_app
import os
import json
import flask
import pytest


from Botosaurus.app import event_hook
from Botosaurus.app import index

@pytest.fixture
def client():
    app=flask(__name__)
    client = app.test_client()

def test_index():
    response = client.get('/')
    assert response.get_data() == b'Welcome to our server !!'

def test_event_hooke_token_failure():
    url = '/slack/events'
    VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN')

    mock_json_dict = {
        'token' : {},
        'type' : 'url_verification'
    }

    response=client.post(url, json_dict=mock_json_dict)
    assert response.status_code == 403

def test_event_hooke_type_failure():
    url = '/slack/events'
    VERIFICATION_TOKEN = os.getenv('VERIFICATION_TOKEN')

    mock_json_dict = {
        'token' : {os.getenv('VERIFICATION_TOKEN')},
        'type' : {}
    }

    response=client.post(url, json_dict=mock_json_dict)
    assert response.status_code == 500