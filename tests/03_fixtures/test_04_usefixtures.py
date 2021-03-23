import os
import pytest


@pytest.fixture
def class_fixt():
    print('\nclass_fixt started')


@pytest.mark.usefixtures('class_fixt')
class TestSomething:
    def test_3(self):
        print('test_3 started')

    def test_4(self):
        print('test_4 started')


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello\n")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
