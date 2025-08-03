from typing import List, Tuple, Set
from pathlib import Path
import os

# Configuration
BROWSER = "Chrome"
DEVICE1 = "PocoX3Pro"
DEVICE2 = "RedmiNote10Pro"
DEVICE_PAIR = f"{DEVICE1}_{DEVICE2}"

# Directory setup
BASE_DIR = Path("Fonts")
COMPARED_DIR = BASE_DIR / "Compared"
UNCOMPARED_FONTS_DIR = BASE_DIR / "Uncompared"

# Comparing device font files
DEVICE1_FONTS = UNCOMPARED_FONTS_DIR / DEVICE_PAIR / DEVICE1 / f"{BROWSER}Fonts.txt"
DEVICE2_FONTS = UNCOMPARED_FONTS_DIR / DEVICE_PAIR / DEVICE2 / f"{BROWSER}Fonts.txt"

# Output directories
COMMON_OUTPUT_DIR = COMPARED_DIR / "Common" / DEVICE_PAIR
UNCOMMON_OUTPUT_DIR = COMPARED_DIR / "Uncommon" / DEVICE_PAIR

# Create output directories if they don't exist
os.makedirs(COMMON_OUTPUT_DIR, parents=True, exist_ok=True)
os.makedirs(UNCOMMON_OUTPUT_DIR / DEVICE1, parents=True, exist_ok=True)
os.makedirs(UNCOMMON_OUTPUT_DIR / DEVICE2, parents=True, exist_ok=True)


def load_font_list(filepath: Path) -> List[str]:
    """Reads a text file with one font per line and returns a cleaned list of font names."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def compare_fonts(list_a: List[str], list_b: List[str]) -> Tuple[Set[str], Set[str], Set[str]]:
    """Compares two lists of font names and returns common fonts, only in list A, and only in list B."""
    set_a = set(list_a)
    set_b = set(list_b)

    common = set_a & set_b
    only_in_a = set_a - set_b
    only_in_b = set_b - set_a

    return common, only_in_a, only_in_b

def save_fonts_to_file(fonts: Set[str], filepath: Path) -> None:
    """Save a set of fonts to a file, one per line."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for font in sorted(fonts):
            f.write(f"{font}\n")

def save_fonts(common: Set[str], only_a: Set[str], only_b: Set[str]) -> None:
    """Prints the font comparison results and saves them to files."""
    # Save common fonts
    common_file = COMMON_OUTPUT_DIR / f"{BROWSER}Fonts.txt"
    save_fonts_to_file(common, common_file)
    
    # Save device-specific uncommon fonts
    only_a_file = UNCOMMON_OUTPUT_DIR / DEVICE1 / f"{BROWSER}Fonts.txt"
    only_b_file = UNCOMMON_OUTPUT_DIR / DEVICE2 / f"{BROWSER}Fonts.txt"
    save_fonts_to_file(only_a, only_a_file)
    save_fonts_to_file(only_b, only_b_file)
    

if __name__ == "__main__":
    list_a = load_font_list(DEVICE1_FONTS)
    list_b = load_font_list(DEVICE2_FONTS)
    
    common_fonts, only_in_a, only_in_b = compare_fonts(list_a, list_b)
    
    save_fonts(common_fonts, only_in_a, only_in_b)
    
    print("\n" + "="*50)
    print(f"Comparison Results ({BROWSER} on {DEVICE1} vs {DEVICE2})")
    print("="*50)
    print(f"\n✅ Common fonts ({len(common_fonts)}):")
    print(f"   Saved to: {common_fonts}")
    print(f"\n🔍 Fonts only in {DEVICE1} ({len(only_in_a)}):")
    print(f"   Saved to: {only_in_a}")
    print(f"\n🔍 Fonts only in {DEVICE2} ({len(only_in_b)}):")
    print(f"   Saved to: {only_in_b}")
    print("\n" + "="*50)
