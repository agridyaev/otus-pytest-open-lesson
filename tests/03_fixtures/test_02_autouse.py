import pytest


@pytest.fixture(autouse=True)
def auto():
    print('\nAutouse fixture')


def test_01():
    print('test_01 started')


def test_02():
    print('test_02 started')
