import re
from pathlib import Path

def normalize_repeated_fonts(font_list: list[str]) -> list[str]:
    cleaned_fonts = set()

    for font in font_list:
        font = font.strip()
        # Try to detect and remove repeated patterns
        match = re.match(r"^(.+?)\1+$", font)
        if match:
            cleaned = match.group(1)
        else:
            # Fallback: split into words, take last half if both halves are identical
            words = font.split()
            mid = len(words) // 2
            if words[:mid] == words[mid:]:
                cleaned = " ".join(words[:mid])
            else:
                cleaned = font
        cleaned_fonts.add(cleaned)

    return sorted(cleaned_fonts)



def get_font_list(filename: str = "Fonts/Unique/duplicate_fonts.txt") -> list[str]:
    """Read in font list from text file."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content.splitlines()

def save_to_txt(font_list: list, filename: str = "Fonts/Unique/unique_fonts.txt"):
    """Saves a list of fonts to a text file, ensuring no empty lines are written."""
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    # Filter out any empty strings from the list before saving
    font_list = [font for font in font_list if font]
    if font_list:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(font_list))
        print(f"Saved {len(font_list)} unique fonts to '{filename}'.")
    else:
        print(f"No fonts to save to '{filename}'.")


if __name__ == "__main__":
    filename = "Fonts/Unique/duplicate_fonts.txt"
    raw_text = get_font_list(filename)
    fonts = normalize_repeated_fonts(raw_text)
    save_to_txt(fonts, "Fonts/Unique/unique_fonts.txt")
