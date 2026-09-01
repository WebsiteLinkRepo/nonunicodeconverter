from fontTools.ttLib import TTFont
import sys

try:
    font = TTFont('/home/samuelvictor/Downloads/Shreelipi_4642.TTF')
    cmap = font['cmap'].getBestCmap()
    with open('scratch/cmap.txt', 'w', encoding='utf-8') as f:
        for k, v in cmap.items():
            f.write(f'{k} (0x{k:x} - {chr(k) if k < 256 else "?"}) -> {v}\n')
    print("Dumped cmap successfully.")
except Exception as e:
    print(f"Error: {e}")
