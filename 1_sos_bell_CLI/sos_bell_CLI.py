import time                # 時間制御（スリープ処理）
from colorama import init, Fore, Back, Style  # ターミナル出力の色付け

# ============== 初期設定 ==============
init(autoreset=True)

FLASH_TIMES = 10        # 点滅回数
FLASH_INTERVAL = 0.5    # 点滅間隔（秒）

# ============== SOSベル処理 ==============
def sos_bell():
    for i in range(FLASH_TIMES):
        if i % 2 == 0:
            print(Back.RED + Fore.WHITE + Style.BRIGHT + "  SOS!!  ")
        else:
            print("        ")
        time.sleep(FLASH_INTERVAL)

# ============== 実行 ==============
if __name__ == "__main__":
    print("=== SOSベル起動 ===")
    sos_bell()
    print("=== 終了 ===")