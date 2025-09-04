# ============== インポート ==============
import tkinter as tk                           # GUI
try:
    from playsound import playsound            # 任意：mp3再生
    SOUND = True
except Exception:
    SOUND = False
from pathlib import Path                       # パス操作
import subprocess                              # 外部コマンド実行

# ============== 設定 ==============
BASE = Path(__file__).parent
SOUNDS = {
    "YES": str((BASE / "yes.mp3").resolve()),
    "NO":  str((BASE / "no.mp3").resolve()),
}
FULLSCREEN_FLASH = True

# ============== サウンド ==============
def try_afplay(path: str) -> bool:
    try:
        subprocess.Popen(["afplay", path])
        return True
    except Exception:
        return False

def beep(key):
    path = SOUNDS.get(key)
    if path:
        if SOUND:
            try:
                playsound(path, block=False)
                return
            except Exception:
                pass
        if try_afplay(path):
            return
    root.bell()

# ============== オーバーレイ表示 ==============
def show_overlay(text, color):
    if not FULLSCREEN_FLASH:
        return
    ov = tk.Toplevel(root)
    ov.configure(bg="black")
    ov.attributes("-fullscreen", True)
    ov.attributes("-topmost", True)
    lbl = tk.Label(ov, text=text, fg=color, bg="black", font=("Arial", 200, "bold"))
    lbl.place(relx=0.5, rely=0.5, anchor="center")
    ov.bind("<Key>",    lambda e: ov.destroy())
    ov.bind("<Button>", lambda e: ov.destroy())
    ov.after(5000, ov.destroy)

# ============== ハンドラ ==============
def click(text, color):
    status.config(text=text, fg=color)
    beep(text)
    show_overlay(text, color)

# ============== UI ==============
root = tk.Tk()
root.title("Yes / No")
root.geometry("520x320")

status = tk.Label(root, text="...", font=("Arial", 48))
status.pack(expand=True)

btns = tk.Frame(root)
btns.pack(pady=10)

tk.Button(btns, text="YES", font=("Arial", 32), width=8, height=2,
          command=lambda: click("YES", "green")).pack(side="left", padx=10)
tk.Button(btns, text="NO",  font=("Arial", 32), width=8, height=2,
          command=lambda: click("NO",  "red")).pack(side="left", padx=10)

root.bind("<Return>", lambda e: click("YES", "green"))
root.bind("<Escape>", lambda e: click("NO",  "red"))

# ============== 起動 ==============
root.mainloop()