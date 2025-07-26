import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()

    TO_DOWNLOAD_FONTS = "Fonts/Unmatched_Merged/PocoX3Pro_RedmiNote10Pro.txt"  # your list (one font family per line)
    DOWNLOADED_FONTS_DIR = "Fonts/Downloaded_fonts"
    os.makedirs(DOWNLOADED_FONTS_DIR, exist_ok=True)

    # Load font list (family names)
    with open(TO_DOWNLOAD_FONTS, encoding="utf‑8") as f:
        wanted = [line.strip() for line in f if line.strip()]

    # Get all Google font metadata
    r = requests.get(
        f"https://www.googleapis.com/webfonts/v1/webfonts?key={os.getenv('API_KEY')}&sort=alpha"
    )
    r.raise_for_status()
    families = {item["family"]: item for item in r.json().get("items", [])}

    downloaded = []
    not_found = []

    CAMOUFOX_FONTS_DIR = r"Fonts/CamouFox/fonts_names.txt"

    for fam in wanted:
        meta = families.get(fam)
        if not meta:
            not_found.append(fam)
            continue
        files = meta.get("files", {})
        variant = "regular" if "regular" in files else next(iter(files))
        fname = f"{fam.replace(' ', '_')}_{variant}.ttf"
        downloaded_fonts_path = os.path.join(DOWNLOADED_FONTS_DIR, fname)
        camoufox_fonts_path = os.path.join(CAMOUFOX_FONTS_DIR, fname)

        if (downloaded_fonts:=os.path.exists(downloaded_fonts_path)) or os.path.exists(camoufox_fonts_path):
            print(f"Already exists: {fam} — variant: {variant} in {downloaded_fonts_path if downloaded_fonts else camoufox_fonts_path}")
            downloaded.append(f"{fam} ({variant})")
            continue

        url = files[variant]
        print(f"Downloading {fam} — variant: {variant}")
        resp = requests.get(url)
        resp.raise_for_status()
        with open(path, "wb") as outf:
            outf.write(resp.content)
        downloaded.append(f"{fam} ({variant})")


    # Save not found fonts to a file
    NOT_FOUND_FILE = os.path.join(DOWNLOADED_FONTS_DIR, "AAA_NOT_FOUND_FONTS.txt")
    with open(NOT_FOUND_FILE, "w", encoding="utf-8") as nf_file:
        for nf in not_found:
            nf_file.write(nf + "\n")

    # Summary
    print("\n=== Download Summary ===")
    print("✅ Downloaded:")
    for d in downloaded:
        print("  -", d)
        
    if not_found:
        print("\n⚠️ Not found in Google Fonts:")
        for nf in not_found:
            print("  -", nf)
    else:
        print("\nAll fonts were available and downloaded.")

if __name__ == "__main__":
    main()