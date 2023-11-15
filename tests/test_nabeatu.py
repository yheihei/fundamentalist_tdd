import pytest
from app.nabeatu import Nabeatu


class TestNabeatu:
    def test_1(self):

        assert 1 == Nabeatu(1).call()

        # 3の倍数の場合バカになる
        assert '3(バカ)' == Nabeatu(3).call()
        assert '9(バカ)' == Nabeatu(9).call()
        assert '12(バカ)' == Nabeatu(12).call()

        # 3が付く数字の場合もバカになる
        assert '13(バカ)' == Nabeatu(13).call()
