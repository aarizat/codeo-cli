import os

import mechanicalsoup as ms
import pytest

from codeo.codeo import CodeoBrowser

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")
CODE = "print('Hola Codeo')"
PROBLEM_URL = "http://127.0.0.1:3000/problemas/0x0-hola-codeo"


@pytest.fixture
def codeo_br():
    br = ms.StatefulBrowser()
    cb = CodeoBrowser(br)
    yield cb
    cb.close()


@pytest.fixture(scope="session")
def source_code(tmpdir_factory):
    file = tmpdir_factory.mktemp("data").join("hi_codeo.py")
    with open(file, "w") as f:
        f.write(CODE)
    return file


def test_codeo_login(codeo_br):
    codeo_br.login(USER_NAME, PASSWORD)
    assert codeo_br.browser.url == "http://127.0.0.1:3000/"


def test_submit_hola_codeo_problem(codeo_br, source_code):
    codeo_br.login(USER_NAME, PASSWORD)
    codeo_br.submit_problem(PROBLEM_URL, source_code)
    assert "envios" in codeo_br.browser.url


def test_read_source_code(source_code):
    assert CODE in CodeoBrowser.read_source_code(source_code)


def test_get_programming_language(source_code):
    assert "Python 3" == CodeoBrowser.get_language(source_code)
