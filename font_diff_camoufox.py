from pathlib import Path
import re

BROWSER = "Firefox"
DEVICE = "PocoX3Pro"
BASE_DIR = Path("Fonts")
CAMOUFOX_FONTS = BASE_DIR / "Camoufox" / "Fonts_names.txt"
DEVICE_BROWSER_FONTS = BASE_DIR / "Common" / f"{BROWSER}.txt"
COMMON_OUTPUT = BASE_DIR / "Camoufox" / "Common" / f"{DEVICE}_{BROWSER}.txt"
UNCOMMON_OUTPUT = BASE_DIR / "Camoufox" / "Uncommon" / f"{DEVICE}_{BROWSER}.txt"

def normalize_font_name(name: str) -> str:
    name = re.sub(r'[-_](Regular|Bold|Italic|Light|Medium|SemiBold|ExtraBold|Black|Thin|ExtraLight)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)
    name = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', name)
    return name.strip().title()

# Ensure the output directories exist
COMMON_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
UNCOMMON_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with open(CAMOUFOX_FONTS, 'r', encoding='utf-8') as f:
    camoufox_set = set(normalize_font_name(line.strip()) for line in f if line.strip())

with open(DEVICE_BROWSER_FONTS, 'r', encoding='utf-8') as f:
    device_browser_set = set(normalize_font_name(line.strip()) for line in f if line.strip())

# Compute intersections and differences
common_fonts = camoufox_set & device_browser_set
uncommon_fonts = device_browser_set - camoufox_set

# Write common fonts
with open(COMMON_OUTPUT, 'w', encoding='utf-8') as f:
    for font in sorted(common_fonts):
        f.write(font + '\n')

# Write uncommon fonts
with open(UNCOMMON_OUTPUT, 'w', encoding='utf-8') as f:
    for font in sorted(uncommon_fonts):
        f.write(font + '\n')
