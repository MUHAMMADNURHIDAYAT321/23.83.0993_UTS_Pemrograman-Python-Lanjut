import os
import time
import sys
import math
import random

RESET = "\033[0m"

# Warna Color Wave
wave_colors = [
    "\033[31m",  # merah
    "\033[33m",  # kuning
    "\033[32m",  # hijau
    "\033[36m",  # cyan
    "\033[34m",  # biru
    "\033[35m"   # ungu
]

# Warna Sparkle
sparkle_colors = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ==============================================================
#   ANIMASI 1 → COLOR WAVE + SHADOW 3D (FITUR DEFAULT)
# ==============================================================
def animasi_color_wave_shadow():
    indent = 0
    indentIncreasing = True
    t = 0

    try:
        while True:
            clear()

            # Color Wave
            color_index = int((math.sin(t) + 1) / 2 * (len(wave_colors) - 1))
            star_color = wave_colors[color_index]

            stars = star_color + "********" + RESET

            # Shadow 3D
            shadow = "\033[90m........\033[0m"

            print(" " * indent + stars)
            print(" " * (indent + 1) + shadow)

            # Zigzag logic
            if indentIncreasing:
                indent += 1
                if indent == 20:
                    indentIncreasing = False
            else:
                indent -= 1
                if indent == 0:
                    indentIncreasing = True

            t += 0.25
            time.sleep(0.09)

    except KeyboardInterrupt:
        return


# ==============================================================
#   ANIMASI 2 → SPARKLE EFFECT + WARP MODE
# ==============================================================
def animasi_sparkle_warp():
    indent = 0
    indentIncreasing = True
    t = 0

    try:
        while True:
            clear()

            # Warp sinus bergelombang
            wave_offset = int(3 * math.sin(t))
            for _ in range(abs(wave_offset)):
                print("")

            # Sparkle warna
            sparkles = ""
            for _ in range(4):
                if random.random() < 0.6:
                    sparkles += random.choice(sparkle_colors) + random.choice(["*", ".", "o"]) + RESET + " "
                else:
                    sparkles += "  "

            stars = "\033[96m********\033[0m"

            print(" " * indent + stars + "   " + sparkles)

            # Zigzag logic
            if indentIncreasing:
                indent += 1
                if indent == 20:
                    indentIncreasing = False
            else:
                indent -= 1
                if indent == 0:
                    indentIncreasing = True

            t += 0.25
            time.sleep(0.1)

    except KeyboardInterrupt:
        return



# ==============================================================
#                          MENU UTAMA
# ==============================================================
def menu():
    while True:
        clear()
        print("===  MENU ANIMASI TERMINAL  ===")
        print("1. Zig-Zag Color Wave + Shadow 3D")
        print("2. Zig-Zag Sparkle Effect + Warp Mode")
        print("3. Keluar")
        print("----------------------------------")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            animasi_color_wave_shadow()
        elif pilihan == "2":
            animasi_sparkle_warp()
        elif pilihan == "3":
            clear()
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(1)


menu()
