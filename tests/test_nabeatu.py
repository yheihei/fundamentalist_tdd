import pytest
from app.nabeatu import Nabeatu


class TestNabeatu:
    def test_1(self):

        assert 1 == Nabeatu(1).call()
