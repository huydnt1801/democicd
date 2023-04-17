import pytest


class Test:
    def test_success(self):
        assert 1 == 1

    def test_fail(self):
        assert 1 == 0
