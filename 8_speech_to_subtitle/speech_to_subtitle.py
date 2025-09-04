import threading                       # 録音を別スレッドで実行
import tkinter as tk                   # GUI
from tkinter import scrolledtext       # スクロール付きテキストエリア
import speech_recognition as sr        # 音声認識（Google Web Speech API）

# ============== 設定 ==============
LANG = "ja-JP"
PHRASE_LIMIT = 15  # 1回の認識時間（秒）

# ============== アプリ本体 ==============
class CaptionApp:
    def __init__(self, root):
        self.root = root
        root.title("音声から簡易字幕アプリ")
        root.geometry("900x360")

        self.text_area = scrolledtext.ScrolledText(root, wrap="word", font=("Arial", 16))
        self.text_area.pack(fill="both", expand=True)

        self.status = tk.Label(root, text="待機中", anchor="w")
        self.status.pack(fill="x")

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.recognizer.pause_threshold = 1.2
        self.recognizer.non_speaking_duration = 0.5
        self.running = False

    def append_text(self, text):
        self.text_area.insert("end", text + "\n")
        self.text_area.see("end")

    def listen_loop(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        while self.running:
            try:
                with self.mic as source:
                    audio = self.recognizer.listen(source, phrase_time_limit=PHRASE_LIMIT, timeout=3)
                result = self.recognizer.recognize_google(audio, language=LANG)
                self.root.after(0, self.append_text, result)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                self.root.after(0, self.append_text, f"[通信エラー] {e}")
            except Exception as e:
                self.root.after(0, self.append_text, f"[エラー] {e}")

    def start(self):
        if self.running:
            return
        self.running = True
        threading.Thread(target=self.listen_loop, daemon=True).start()
        self.status.config(text="録音中...話してください")

    def stop(self):
        self.running = False
        self.status.config(text="停止しました")

    def clear(self):
        self.text_area.delete("1.0", "end")

# ============== 起動 ==============
if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionApp(root)

    frame = tk.Frame(root)
    frame.pack(fill="x", pady=5)
    tk.Button(frame, text="▶ 開始", command=app.start).pack(side="left", padx=5)
    tk.Button(frame, text="■ 停止", command=app.stop).pack(side="left", padx=5)
    tk.Button(frame, text="🧹 クリア", command=app.clear).pack(side="left", padx=5)

    root.mainloop()