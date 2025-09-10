# ワンクリックランチャー

## 概要
仕事用・プライベート用にまとめてアプリやWebサイトを一括で起動できるGUIツールです。
よく使うアプリやサービスをワンクリックで開けるため、複雑な操作が難しい体の不自由な人に便利です。
「ワンクリックで必要な環境をすぐ整える」ことを目的とした支援アプリです。

## 主な機能

### 仕事用セット
- 音声支援（Siri / Windows音声設定）
- メモアプリ（TextEdit / メモ帳、音声入力に対応）
- ChatGPT（音声入力に対応）
- Zoom（音声会議・字幕機能あり）
- Google カレンダー（音声アシスタントと連携可能）
- Google Drive（音声入力や読み上げに対応）

### プライベート用セット
- ChatGPT（音声入力に対応）
- Instagram（スクリーンリーダー対応、音声入力で検索可能）
- YouTube（音声検索や字幕機能に対応）
- Netflix（字幕・音声ガイド機能に対応）
- Amazon（音声検索・Alexa連携可能）
- 楽天市場（音声検索対応）
- Spotify（音声操作やスマートスピーカー連携可能）

### 特長
 • Mac と Windows 両対応（自動判定して適切なアプリを起動）
 • GUIボタンで簡単操作（「仕事用」「プライベート用」を選ぶだけ）
 • よく使うサービスを一括起動して、毎回の立ち上げ作業を効率化

### 動作イメージ
 1. アプリを起動すると「仕事用を開始」「プライベートを開始」のボタンが表示されます。
 2. 「仕事用」を押せば仕事に必要なアプリ・Webサービスがまとめて開きます。
 3. 「プライベート」を押せばSNSや動画サービス、音楽配信などが起動します。


対象: 複雑な操作が難しい体の不自由な人  
対象分野: GUIアプリ  
使用ライブラリ: tkinter, subprocess, platform, webbrowser


## デモ動画
[![デモ動画を見る](https://img.youtube.com/vi/lUqwyf3ikow/0.jpg)](https://www.youtube.com/watch?v=lUqwyf3ikow)

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot_1.png)
![screenshot](images/screenshot_2.png)

- 実行環境: Python 3.x（macOS / Windows）
- 依存: 標準ライブラリ（追加インストール不要）


## 実行方法
```bash
python one_click_launcher.py
```

## ファイル構成（例）
```
3_one_click_launcher/
├── one_click_launcher.py
├── images/
│   └── screenshot_1.png   # 実行時の画面サンプル (仕事用モード)
│   └── screenshot_2.png   # 実行時の画面サンプル (プラベート用モード)
└── README.md            # このファイル
```


## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。
