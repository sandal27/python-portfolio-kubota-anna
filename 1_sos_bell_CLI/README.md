# SOSベル（CLI版）

## デモ動画
[![デモ動画を見る](https://img.youtube.com/vi/FdvcAs6GrUc/0.jpg)](https://www.youtube.com/watch?v=FdvcAs6GrUc)

##  概要
ターミナル（CLI）で **SOS 緊急サイン** を赤背景・白文字で点滅表示する、超シンプルなユーティリティ。
開発者やデモ用に「赤点滅でSOSを伝える仕組み」を 視覚的に体験してもらうためのサンプル。

- 実行環境: Python 3.x（macOS / Windows / Linux）
- 依存: `colorama`（端末の文字色・背景色の制御）


## セットアップ
推奨: 仮想環境を使う（任意）

```bash
# venv の作成と有効化
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows

# 依存ライブラリのインストール
pip install colorama
```


##  実行方法
```bash
python sos_bell_CLI.py
```

実行すると、以下のように点滅表示されます：

```
=== SOSベル起動 ===
  SOS!!  
         
  SOS!!  
         
...（繰り返し）
=== 終了 ===
```


## 調整できる設定
スクリプト先頭の定数を変更できます。

- `FLASH_TIMES`（初期値: `10`）  点滅回数。偶数番目に「SOS!!」、奇数番目に空行を表示します。

- `FLASH_INTERVAL`（初期値: `0.5`）  点滅間隔（秒）。値を小さくすると速く、大きくするとゆっくり点滅します。


## 注意事項
- 本ツールは **デモ／学習目的** です。実際の緊急通報には使用できません。  
- 端末やシェルの配色設定によっては、色の見え方が異なる場合があります。


## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot.png)


## ファイル構成
```
1_sos_bell_CLI/
├── sos_bell_CLI.py
├── README.md
└── images/
    └── screenshot.png   # 実行時の画面サンプル
```

## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。
