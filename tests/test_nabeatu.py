import pytest
from app.nabeatu import Nabeatu


class TestNabeatu:
    def test_1以上の数値かつ3の倍数でも3が付く数字でもない場合はそのまま文字列として返す(self):
        assert "1" == Nabeatu(1).call()

    def test_3の倍数の場合アホになる(self):
        assert '3(アホ)' == Nabeatu(3).call()
        assert '9(アホ)' == Nabeatu(9).call()
        assert '12(アホ)' == Nabeatu(12).call()

    def test_3が付く数字の場合もアホになる(self):
        assert '13(アホ)' == Nabeatu(13).call()

    def test_数字以外を入れたらValueErrorになる(self):
        with pytest.raises(ValueError) as e:
            Nabeatu('a').call()
        assert '数字を入れてください' == str(e.value)

    def test_0以下の値を入れたらValueErrorになる(self):
        with pytest.raises(ValueError) as e:
            Nabeatu(0).call()
        with pytest.raises(ValueError) as e:
            Nabeatu(-1).call()
        assert '1以上の数値を入れてください' == str(e.value)

    def test_finale(self):
        for i in range(1, 101):
            print(Nabeatu(i).call())
