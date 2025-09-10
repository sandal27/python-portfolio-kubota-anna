# SOSベル（CLI版）

##  概要
このアプリは、Python で作成した 簡易 SOS ベル です。
実行するとターミナル画面に「SOS!!」が赤背景・白文字で点滅表示され、緊急信号を再現します。

主な機能
 1. 点滅表示：赤い背景と白文字で「SOS!!」を表示
 2. 点滅回数の設定：FLASH_TIMES で回数を指定可能
 3. 点滅間隔の設定：FLASH_INTERVAL で点滅の速度を調整可能
 4. 自動リセット：colorama の機能で色設定が毎回リセットされ、画面が乱れない

動作イメージ
 1. 起動すると「=== SOSベル起動 ===」と表示
 2. 赤背景の「SOS!!」と空白が交互に点滅
 3. 設定回数の点滅が終わると「=== 終了 ===」で終了

対象: 聴覚に頼らずに緊急を視覚で伝えるニーズ
対象分野: CLIアプリ
使用ライブラリ: colorama

## デモ動画
[![デモ動画を見る](https://img.youtube.com/vi/FdvcAs6GrUc/0.jpg)](https://www.youtube.com/watch?v=FdvcAs6GrUc)

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot.png)

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

## 注意事項
- 本ツールは **デモ／学習目的** です。実際の緊急通報には使用できません。  
- 端末やシェルの配色設定によっては、色の見え方が異なる場合があります。


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
