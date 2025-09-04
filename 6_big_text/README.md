# 大文字テキスト表示（Flask）

## 概要
入力したテキストを**超大きな文字**で表示するシンプルなWebアプリ。  
視認性を高めたい人向け。読み上げ（TTS）と高コントラスト切替付き。

- 対象：弱視・高齢者・遠目から見たい状況
- 実行環境：Python 3.x（macOS / Windows / Linux）
- 依存：Flask（サーバ側）、ブラウザの Web Speech API（読み上げ）

## セットアップ
```bash
pip install Flask
```

## 実行
```bash
python big_text.py
```
ブラウザで `http://127.0.0.1:5000/` を開く。フォームにテキストを入力→「表示」。

## 操作・機能
- 読み上げ：画面右上の「読み上げ」ボタンで再生
- 高コントラスト切替：左上のボタンで白/黒を切替（文字の視認性向上）
- レスポンシブ：`vw` を使用し画面幅に追従して巨大表示

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot_1.png)
![screenshot](images/screenshot_2.png)

## ファイル構成
```
6_big_text/
├── big_text.py
├── README.md   　← このファイル
└── images/
    └── screenshot_1.png　　# 実行時の画面サンプル (入力画面)
    └── screenshot_2.png   # 実行時の画面サンプル (通常モード、高コントラストモード)
```
## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。