import pytest
from app.nabeatu import Nabeatu


class TestNabeatu:
    def test_正常系(self):

        assert 1 == Nabeatu(1).call()

        # 3の倍数の場合バカになる
        assert '3(バカ)' == Nabeatu(3).call()
        assert '9(バカ)' == Nabeatu(9).call()
        assert '12(バカ)' == Nabeatu(12).call()

        # 3が付く数字の場合もバカになる
        assert '13(バカ)' == Nabeatu(13).call()

    def test_準正常系(self):
        # 数字以外を入れたらValueErrorになる
        with pytest.raises(ValueError) as e:
            Nabeatu('a').call()
        assert '数字を入れてください' == str(e.value)

        # 0以下の値を入れたらValueErrorになる
        with pytest.raises(ValueError) as e:
            Nabeatu(0).call()
        with pytest.raises(ValueError) as e:
            Nabeatu(-1).call()
        assert '1以上の数値を入れてください' == str(e.value)
