# import pytest_mock
# import anthropic
import pytest
from config import Config
from dotenv import load_dotenv
from flask import Flask
from pytest_socket import disable_socket

load_dotenv()


def pytest_runtest_setup():
    disable_socket()


@pytest.fixture()
def app():
    app = Flask(__name__)
    app.config.from_object(Config)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
