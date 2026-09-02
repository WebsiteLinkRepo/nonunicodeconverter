import os
import glob

# List of individual glyph cards
glyph_files = sorted(glob.glob('scratch/shreelipi_telugu/glyphs/*.png'))
print(f"Total glyph cards available: {len(glyph_files)}")

# Print some ranges
for f in glyph_files[:30]:
    print(f)
