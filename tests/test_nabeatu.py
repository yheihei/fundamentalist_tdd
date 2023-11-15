import pytest
from app.nabeatu import Nabeatu


class TestNabeatu:
    def test_1(self):

        assert 1 == Nabeatu(1).call()

        # 3がつく数字の場合バカになる
        assert '3(バカ)' == Nabeatu(3).call()
