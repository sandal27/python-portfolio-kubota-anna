# 拡大ルーペビューア（Lupe）

## 概要
マウス周辺の画面を拡大表示するシンプルなルーペアプリ。  
視覚支援やプレゼン時の画面強調に利用できる。

- 実行環境: Python 3.x（macOS / Windows）
- 依存: `tkinter`, `pillow`（画像処理ライブラリ）


## セットアップ

```bash
pip install pillow
```

> `tkinter` は Python 標準に含まれているため追加インストール不要。


## 実行方法

```bash
python lupe.py
```

起動すると、マウス周辺を拡大表示するウィンドウが開きます。  
- ウィンドウは常に最前面に表示される  
- `Esc` キーで終了可能  


## 調整できる設定
スクリプト先頭で値を変更できます。

- `window_size`（初期値: `480`） ルーペウィンドウの大きさ（px）
- `zoom`（初期値: `3`） 拡大倍率
- `refresh_ms`（初期値: `30`） 更新間隔（ミリ秒）。小さくすると滑らかだがCPU負荷が上がる

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot.png)

## ファイル構成
```
2_拡大ルーペビューア/
├── lupe.py
└── README.md   ← このファイル
└── images/
    └── screenshot.png   # 実行時の画面サンプル
```

## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。
