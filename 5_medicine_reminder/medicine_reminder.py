import tkinter as tk                   # GUI
from tkinter import messagebox         # ポップアップ

# ============== 状態 ==============
job_id = None  # 現在の予約ID（上書き・停止用）

# ============== ハンドラ ==============
def show_reminder():
    global job_id
    task = task_entry.get().strip() or "お薬"
    messagebox.showinfo("服薬リマインダー", f"💊 飲む薬：{task}")
    job_id = None

def start_reminder():
    global job_id
    hours_ms = int(hours_var.get()) * 60 * 60 * 1000
    if job_id:
        root.after_cancel(job_id)
    job_id = root.after(hours_ms, show_reminder)

def stop_reminder():
    global job_id
    if job_id:
        root.after_cancel(job_id)
        job_id = None

# ============== UI ==============
root = tk.Tk()
root.title("服薬リマインダー（単発）")
root.geometry("400x300")

title_label = tk.Label(root, text="💊 服薬リマインダー", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="これから飲む薬").pack()
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

tk.Label(root, text="通知までの時間（時間）：").pack()
hours_var = tk.StringVar(value="3")
tk.OptionMenu(root, hours_var, "1", "2", "3", "4", "5", "6", "8", "12").pack(pady=5)

tk.Button(root, text="開始", width=10, command=start_reminder).pack(pady=5)
tk.Button(root, text="停止", width=10, command=stop_reminder).pack()

root.mainloop()