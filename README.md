# 環境構築

```
pip install pytest
```

# テスト実行方法

```
pytest -s -p no:warnings
```

# なぜやるか

```
　　　　 ,、,,,、,,, 
　　　 _,,;' '" '' ;;,, 
　　（rヽ,;''""''゛゛;,ﾉｒ）　　　　 
　　 ,; i ___　、___iヽ゛;,　　テスト書いてないとかお前それ@t_wadaの前でも同じ事言えんの？
　 ,;'''|ヽ・〉〈・ノ |ﾞ ';, 
　 ,;''"|　 　▼　　 |ﾞ゛';, 
　 ,;''　ヽ ＿人＿  /　,;'_ 
 ／ｼ、    ヽ  ⌒⌒  /　 ﾘ　＼ 
|　　 "ｒ,,｀"'''ﾞ´　　,,ﾐ| 
|　　 　 ﾘ、　　　　,ﾘ　　 | 
|　　i 　゛ｒ、ﾉ,,ｒ" i _ | 
|　　｀ー――-----------┴ ⌒´ ） 
（ヽ  _____________ ,, ＿´） 
 （_⌒_______________ ,, ィ 
     T                 |
     |                 |
```

# TDD(テスト駆動開発)のサイクル

* Red 失敗するテストを書く
* Green 最速で雑にテストを通す
* Refactor テストOKを維持したままリファクタ

# 問題

TDDのサイクルを使って、世界のナベアツクラスを作ろう

[解答例はこちら](https://github.com/yheihei/fundamentalist_tdd/tree/demo)

## 世界のナベアツクラスの仕様

* 数字を入れたら数字を返す
* 3の倍数のときはアホになる
* 3がつく数字のときもアホになる

# 参考図書

[テスト駆動開発](https://amzn.to/3ubkIVk)
