import pandas as pd                     # データ処理
import matplotlib.pyplot as plt         # グラフ描画
from matplotlib.patches import Patch    # 凡例（色ラベル）
from matplotlib import rcParams         # フォント設定

# ============== フォント設定 ==============
rcParams['font.family'] = 'Hiragino Mincho ProN'

# ============== データ読み込み ==============
df = pd.read_csv("vision_support_graph.csv")
rates = df["利用率（%）"]

# ============== 色分けルール ==============
colors = [
    '#E74C3C' if r < 40 else '#F4D03F' if r < 70 else '#2ECC71'
    for r in rates
]

# ============== グラフ描画 ==============
plt.figure(figsize=(10, 6))
bars = plt.bar(df["視覚支援機能"], rates, width=0.6, color=colors)

# 凡例
legend_labels = [
    Patch(color='#E74C3C', label='低（<40%）'),
    Patch(color='#F4D03F', label='中（40〜69%）'),
    Patch(color='#2ECC71', label='高（70%以上）')
]
plt.legend(handles=legend_labels, title="利用率")

# 棒の上に数値表示
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval:.1f}%', ha='center')

# タイトル・ラベル
plt.title("視覚支援機能の利用率", fontsize=24, fontweight='bold')
plt.xlabel("視覚支援機能", fontsize=18, labelpad=15)
plt.ylabel("利用率（%）", fontsize=18)

# 軸・装飾
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 出力
plt.savefig("screenshot.png")
plt.show()