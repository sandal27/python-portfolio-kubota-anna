# 服薬リマインダー（GUI版）

## 概要

このアプリは、Python（Tkinter）で作成した お薬リマインダー です。
決まった時間に通知を表示し、飲み忘れを防ぐためのシンプルな支援ツールです。

主な機能
1. 時間設定：指定した時刻になるとリマインダーが起動
2. 通知表示：ポップアップウィンドウで「お薬の時間」をお知らせ
3. 簡単操作：GUI上で直感的に使えるシンプルな構成
4. 終了操作：OKボタンや閉じる操作で通知を消せる

動作イメージ
 1. アプリを起動すると、バックグラウンドで時刻を監視します。
 2. 指定時間になると、ウィンドウが表示され「お薬の時間です」とお知らせします。
 3. ボタンを押すと通知が閉じ、次のリマインダーに備えます

## デモ動画
[![デモ動画を見る](https://img.youtube.com/vi/3CMfuVnON0c/0.jpg)](https://www.youtube.com/watch?v=3CMfuVnON0c)

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot.png)


- 実行環境: Python 3.x（macOS / Windows / Linux）
- 依存: 標準ライブラリ（tkinter）


## セットアップ
特別な準備は不要。Python 標準の `tkinter` を使用。


## 実行方法
```bash
python medicine_reminder.py
```

## ファイル構成（例）
```
5_medicine_reminder/
├── medicine_reminder.py
├── README.md　　　　　　　← このファイル
└── images/
    └── screenshot.png   # 実行時の画面サンプル
```


## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。
