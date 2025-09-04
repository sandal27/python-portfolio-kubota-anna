# Yes/No ボタン

## 概要
大きな **YES / NO** ボタンで意思表示を支援するシンプルなデスクトップアプリ（Tkinter）。  
押した内容を画面中央に表示し、効果音（任意）や全画面オーバーレイで周囲に分かりやすく伝えられる。  
キーボード操作（Enter=YES / Esc=NO）にも対応。

- 実行環境: Python 3.x（macOS / Windows）
- 依存ライブラリ: なし（任意で `playsound` を使用して mp3 再生）


## セットアップ
任意: 効果音を使う場合だけ `playsound` を入れる。

```bash
pip install playsound   # 任意
```

プロジェクト直下に `yes.mp3` / `no.mp3` を置く。置かない場合はシステムのビープ音にフォールバック。


## 実行方法
```bash
python yes_no_button.py
```


## 操作
- マウス: 「YES」「NO」ボタンをクリック
- キーボード: `Enter` → YES、`Esc` → NO


## 調整できる設定
- `FULLSCREEN_FLASH`（既定: `True`）  
  クリック時に全画面オーバーレイ（黒背景＋大文字）を出すかどうか。無効にする場合は `False`。

- オーバーレイの表示時間  
  `ov.after(5000, ov.destroy)` の数値（ミリ秒）を変更（例: 3000 なら 3 秒）。

- 効果音の扱い  
  `playsound` が使えれば mp3 を再生。使えない / mp3 が無い場合はシステムのビープ (`root.bell()`) に自動フォールバック。  
  macOS では `afplay` コマンドが使える環境なら自動的にそちらも試行。


## 注意事項
- `afplay` は macOS 専用。Windows では `playsound` が無い場合、ビープ音のみ。
- mp3 パスは `yes_no_button.py` と同じディレクトリに `yes.mp3` / `no.mp3` を配置する前提。


## スクリーンショット
> `images/screenshot.png`  
![screenshot](images/screenshot_1.png)
![screenshot](images/screenshot_2.png)


## ファイル構成
```
7_yes_no_button/
├── yes_no_button.py
├── yes.mp3
├── no.mp3
├── images/
│   └── screenshot_1.png   # 実行時の画面サンプル
│   └── screenshot_2.png   # 実行時の画面サンプル_全画面
└── README.md              # このファイル
```

## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。

