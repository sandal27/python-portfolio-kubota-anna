import tkinter as tk                                   # GUI
from PIL import ImageGrab, Image, ImageTk              # 画面キャプチャ／画像処理／Tk表示

# ============== 設定 ==============
window_size = 480
zoom = 3
crop_size = window_size // zoom
refresh_ms = 30

# ============== 表示更新 ==============
def update():
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    left, top = x - crop_size // 2, y - crop_size // 2
    shot = ImageGrab.grab(bbox=(left, top, left + crop_size, top + crop_size))
    zoomed = shot.resize((window_size, window_size), Image.LANCZOS)
    img = ImageTk.PhotoImage(zoomed)
    label.config(image=img)
    label.image = img
    root.after(refresh_ms, update)

def on_esc(_):
    root.destroy()

# ============== UI ==============
root = tk.Tk()
root.title("Lupe")
root.attributes("-topmost", True)
root.resizable(False, False)
root.bind("<Escape>", on_esc)

label = tk.Label(root, width=window_size, height=window_size, bd=2, relief="solid")
label.pack()

# ============== 起動 ==============
update()
root.mainloop()