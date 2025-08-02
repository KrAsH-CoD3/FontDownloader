from dotenv import load_dotenv
from pathlib import Path
import requests
import os
import re

load_dotenv()
API_KEY = os.getenv("GOOGLE_FONTS_API_KEY") or os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("Missing GOOGLE_FONTS_API_KEY or API_KEY in .env")

BROWSER = "Firefox"
DEVICE1 = "PocoX3Pro"
DEVICE2 = "RedmiNote10Pro"

# Directory setup
BASE_DIR = Path("Fonts")
CAMOUFOX_FONTS = BASE_DIR / "Camoufox" / "Fonts_names.txt"  # All available fonts
COMMON_FONTS_DIR = BASE_DIR / "Common"
UNCOMMON_FONTS_DIR = BASE_DIR / "Uncommon"
BASE_DOWNLOADED_FONTS_DIR = BASE_DIR / "Downloaded_fonts"
DOWNLOADED_FONTS_DIR = BASE_DOWNLOADED_FONTS_DIR / f"{DEVICE1}_{DEVICE2}" / BROWSER

WANTED_FONT_LIST_FILE = COMMON_FONTS_DIR / f"{DEVICE1}_{DEVICE2}" / f"{BROWSER}Fonts.txt"
NOT_FOUND_FILE = DOWNLOADED_FONTS_DIR / "AAA_NOT_FOUND_FONTS.txt"

# Ensure directories exist
os.makedirs(DOWNLOADED_FONTS_DIR, exist_ok=True)
os.makedirs(COMMON_FONTS_DIR, exist_ok=True)
os.makedirs(UNCOMMON_FONTS_DIR, exist_ok=True)

def normalize_font_name(name: str) -> str:
    name = re.sub(r'[-_](Regular|Bold|Italic|Light|Medium|SemiBold|ExtraBold|Black|Thin|ExtraLight)$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)
    name = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', name)
    return name.strip().title()

def load_font_names(filepath: Path) -> set[str]:
    with open(filepath, "r", encoding="utf-8") as f:
        return set(normalize_font_name(line.strip()) for line in f if line.strip())

def fetch_google_fonts(api_key: str) -> dict:
    url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}&sort=alpha"
    resp = requests.get(url)
    resp.raise_for_status()
    return {item["family"]: item for item in resp.json().get("items", [])}

def download_font_file(url: str, save_path: Path):
    resp = requests.get(url)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(resp.content)

def main():
    # Load available fonts from Camoufox
    full_font_set = load_font_names(CAMOUFOX_FONTS)
    
    # Load wanted fonts for the specified browser
    if not WANTED_FONT_LIST_FILE.exists():
        print(f"❌ Font list not found: {WANTED_FONT_LIST_FILE}")
        return
        
    wanted_font_set = load_font_names(WANTED_FONT_LIST_FILE)
    fonts_to_download = wanted_font_set - full_font_set

    if not fonts_to_download:
        print("🎉 All wanted fonts are already present. Nothing to download.")
        return

    print("📦 Fetching Google Fonts metadata...")
    google_fonts = fetch_google_fonts(API_KEY)
    google_fonts_normalized = {
        normalize_font_name(name): name for name in google_fonts
    }

    downloaded, not_found = [], []

    for norm_name in sorted(fonts_to_download):
        google_family = google_fonts_normalized.get(norm_name)
        if not google_family:
            print(f"❌ Not found: {norm_name}")
            not_found.append(norm_name)
            continue

        meta = google_fonts[google_family]
        files = meta.get("files", {})
        variant = "regular" if "regular" in files else next(iter(files))
        url = files[variant]
        file_name = f"{google_family}{'' if variant == 'regular' else f' {variant}'}.ttf"
        save_path = DOWNLOADED_FONTS_DIR / BROWSER / file_name

        if save_path.exists():
            print(f"🔁 Already downloaded: {google_family} ({variant})")
            continue

        print(f"⬇️ Downloading: {google_family} ({variant})")
        try:
            download_font_file(url, save_path)
            downloaded.append(f"{google_family} ({variant})")
        except Exception as e:
            print(f"⚠️ Error downloading {google_family}: {e}")
            not_found.append(norm_name)

    if downloaded:
        print("\n✅ Downloaded:")
        for d in downloaded:
            print(f"  - {d}")

    if not_found:
        print("\n⚠️ Not Found:")
        for nf in not_found:
            print(f"  - {nf}")
        with open(NOT_FOUND_FILE, "w", encoding="utf-8") as f:
            f.write('\n'.join(not_found))

if __name__ == "__main__":
    main()