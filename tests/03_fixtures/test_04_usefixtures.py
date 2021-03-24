import pytest


@pytest.fixture
def func_fixt():
    print('\nfunc_fixt started')


@pytest.mark.usefixtures('func_fixt')
class TestSomething:
    def test_3(self):
        print('test_3 started')

    def test_4(self):
        print('test_4 started')
