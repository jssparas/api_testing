import json, requests
import pytest
import config


def test_get_emojis():
    resp = requests.get(f'{config.BASE_URL}/emojis')
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert len(resp.json()) > 0


def test_post_emojis():
    resp = requests.post(f'{config.BASE_URL}/emojis')
    assert resp.status_code == 404
    assert 'message' in resp.json()
    assert resp.json().get('message') == 'Not Found'


def test_delete_emojis():
    resp = requests.delete(f'{config.BASE_URL}/emojis')
    assert resp.status_code == 404
    assert 'message' in resp.json()
    assert resp.json().get('message') == 'Not Found'
