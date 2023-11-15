# 環境構築

```
poetry install
poetry shell
```

# テスト実行方法

```
pytest -s -p no:warnings
```

# TDD(テスト駆動開発)のサイクル

* Red 失敗するテストを書く
* Green 最速で雑にテストを通す
* Refactor テストOKを維持したままリファクタ

# 問題

TDDのサイクルを使って、世界のナベアツクラスを作ろう

## 世界のナベアツクラスの仕様

* 数字を入れたら数字を返す
* 3の倍数のときはアホになる
* 3がつく数字のときもアホになる

# 参考図書

[テスト駆動開発](https://amzn.to/3ubkIVk)
