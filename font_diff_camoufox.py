from pathlib import Path
import re


BROWSER = "Firefox"   # <=== The browser to compare to Camoufox
DEVICE1 = "PocoX3Pro" # <=== The device to compare to Camoufox

DEVICE2 = "RedmiNote10Pro"  # <=== The second device which common fonts was gotten from
DEVICE_PAIR = f"{DEVICE1}_{DEVICE2}"

BASE_DIR = Path("Fonts")
COMPARED_DIR = BASE_DIR / "Compared"
CAMOUFOX_FONTS_DIR = COMPARED_DIR / "Camoufox"
CAMOUFOX_FONTS = BASE_DIR / "CamoufoxFonts.txt"

COMMON_DIR = CAMOUFOX_FONTS_DIR / "Common"
UNCOMMON_DIR = CAMOUFOX_FONTS_DIR / "Uncommon"

# Input file paths
browser_fonts_file = COMPARED_DIR / "Common" / DEVICE_PAIR / f"{BROWSER}Fonts.txt"

# Output file paths
common_output = COMMON_DIR / f"{DEVICE1}{BROWSER}Fonts.txt"
uncommon_output = UNCOMMON_DIR / f"{DEVICE1}{BROWSER}Fonts.txt"

# Ensure output directories exist
CAMOUFOX_FONTS_DIR.mkdir(parents=True, exist_ok=True)
COMMON_DIR.mkdir(parents=True, exist_ok=True)
UNCOMMON_DIR.mkdir(parents=True, exist_ok=True)

def normalize_font_name(name: str) -> str:
    name = re.sub(r'[-_](Regular|Bold|Italic|Light|Medium|SemiBold|ExtraBold|Black|Thin|ExtraLight)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)
    name = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', name)
    return name.strip().title()

def load_fonts_from_file(filepath):
    """Load font names from a file and return a set of normalized names."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return set(normalize_font_name(line.strip()) for line in f if line.strip())
    except FileNotFoundError:
        print(f"Warning: Font file not found: {filepath}")
        return set()

def save_fonts_to_file(fonts, filepath):
    """Save a set of font names to a file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for font in sorted(fonts):
            f.write(f"{font}\n")

# Load font sets
camoufox_set = load_fonts_from_file(CAMOUFOX_FONTS)
browser_fonts = load_fonts_from_file(browser_fonts_file)

# Compute intersections and differences
common_fonts = camoufox_set & browser_fonts
uncommon_fonts = browser_fonts - camoufox_set

# Save results
save_fonts_to_file(common_fonts, common_output)
save_fonts_to_file(uncommon_fonts, uncommon_output)

print(f"Comparison of {DEVICE1} {BROWSER} Fonts with Camoufox Fonts:")
print(f"  - Common fonts: {len(common_fonts)}")
print(f"  - Uncommon fonts: {len(uncommon_fonts)}")
