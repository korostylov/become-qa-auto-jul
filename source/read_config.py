import pytest
import json

#@pytest.fixture(scope='session')
def config():
  with open('config/config.json') as config_file:
    data = json.load(config_file)
  return data