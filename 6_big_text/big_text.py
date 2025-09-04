# ============== インポート ==============
from flask import Flask, request, render_template_string  # Webフレームワーク／リクエスト取得／文字列テンプレ描画

# ============== アプリ生成 ==============
app = Flask(__name__)

# ============== テンプレート ==============
TEMPLATE_FORM = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>大文字テキスト表示</title>
  <style>
    body { text-align: center; margin-top: 3rem; font-family: Arial, sans-serif; }
    input { font-size: 1.2rem; width: 70%; }
    button { font-size: 1.2rem; }
  </style>
</head>
<body>
  <h1>テキストを入力してください</h1>
  <form method="post">
    <input name="msg" placeholder="文字を入力してください">
    <button>表示</button>
  </form>
</body>
</html>
"""

TEMPLATE_SHOW = """
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>大文字テキスト表示</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root { --bg: #fff; --fg: #000; }
    body {
      margin: 0; background: var(--bg); color: var(--fg);
      display:flex; align-items:center; justify-content:center; min-height:100svh;
      font-family: system-ui, sans-serif;
    }
    .big {
      font-size: 12vw; font-weight: 800; line-height: 1; text-align: center;
      word-break: break-word;
    }
    .toolbar {
      position: fixed; inset: 12px 12px auto auto; display: flex; gap: 8px;
    }
    button { font-size: 1rem; padding: .5rem .8rem; }
    .contrast {
      position: fixed; top: 12px; left: 12px;
    }
  </style>
</head>
<body>
  <div class="big" aria-live="polite">{{ msg|e }}</div>

  <div class="toolbar">
    <button type="button" onclick="speak()">読み上げ</button>
  </div>
  <button class="contrast" type="button" onclick="toggleTheme()">高コントラスト</button>

  <script>
    function speak(){
      const u = new SpeechSynthesisUtterance({{ msg|tojson }});
      speechSynthesis.cancel();
      if (u.text && u.text.trim()) speechSynthesis.speak(u);
    }
    function toggleTheme(){
      const r = document.documentElement;
      const dark = r.dataset.theme === 'dark';
      r.dataset.theme = dark ? '' : 'dark';
      document.body.style.background = dark ? '' : '#000';
      document.body.style.color = dark ? '' : '#fff';
    }
  </script>
</body>
</html>
"""

# ============== ルーティング ==============
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        msg = request.form.get("msg", "").strip() or "（空）"
        return render_template_string(TEMPLATE_SHOW, msg=msg)
    return render_template_string(TEMPLATE_FORM)

# ============== 起動 ==============
if __name__ == "__main__":
    app.run(debug=True)