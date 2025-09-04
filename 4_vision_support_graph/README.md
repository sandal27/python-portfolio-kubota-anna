# 視覚支援機能の利用率グラフ

## 概要
CSVデータをもとに、視覚支援機能の利用率を色分け棒グラフで可視化するツール。  
利用率に応じて赤・黄・緑で分類し、視覚的にわかりやすく表示する。

- 実行環境: Python 3.x（macOS / Windows / Linux）
- 依存: pandas, matplotlib


## セットアップ
```bash
pip install pandas matplotlib
```

## 実行方法
```bash
python vision_support_graph.py
```

実行すると、以下のようなグラフが表示される：

- 棒の色分け  
  - 赤: 利用率 < 40%  
  - 黄: 40〜69%  
  - 緑: 70%以上  
- 各棒の上に利用率（%）を数値で表示  


## 入力データ
使用する CSV ファイル（例: `vision_support.csv`）：

```csv
視覚支援機能,利用率（%）
拡大鏡,65.2
色反転,42.7
高コントラスト,58.9
スクリーンリーダー,73.5
字幕表示,81.3
```

## スクリーンショット
> `images/screenshot.png` 
![screenshot](images/screenshot.png)


## ファイル構成（例）
```
4_vision_support_graph/
├── vision_support.csv
├── vision_support_graph.py
├── images/
│   └── screenshot.png   # 実行時のグラフサンプル
└── README.md            # このファイル
```

## ライセンス
このリポジトリ内のコードは、個人ポートフォリオの実演・学習用途を想定しています。
