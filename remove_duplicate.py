import re

def normalize_repeated_fonts(text: str) -> list:
    lines = text.strip().splitlines()
    cleaned_fonts = set()

    for line in lines:
        line = line.strip()
        # Try to detect and remove repeated patterns
        match = re.match(r"^(.+?)\1+$", line)
        if match:
            cleaned = match.group(1)
        else:
            # Fallback: split into words, take last half if both halves are identical
            words = line.split()
            mid = len(words) // 2
            if words[:mid] == words[mid:]:
                cleaned = " ".join(words[:mid])
            else:
                cleaned = line
        cleaned_fonts.add(cleaned)

    return sorted(cleaned_fonts)


def save_to_txt(font_list: list, filename: str = "unique_fonts.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(font_list))
    print(f"Saved {len(font_list)} unique fonts to '{filename}'.")


if __name__ == "__main__":
    raw_text = """
Arimo
CousineCousine
Noto Sans JPNoto Sans JP
Noto Sans KRNoto Sans KR
Noto Sans SCNoto Sans SC
Noto Sans TCNoto Sans TC
TinosTinos
Noto Naskh ArabicNoto Naskh Arabic
Noto Sans AdlamNoto Sans Adlam
Noto Sans ArmenianNoto Sans Armenian
Noto Sans BalineseNoto Sans Balinese
Noto Sans BamumNoto Sans Bamum
Noto Sans BatakNoto Sans Batak
Noto Sans BengaliNoto Sans Bengali
Noto Sans BugineseNoto Sans Buginese
Noto Sans BuhidNoto Sans Buhid
Noto Sans Canadian AboriginalNoto Sans Canadian Aboriginal
Noto Sans ChakmaNoto Sans Chakma
Noto Sans ChamNoto Sans Cham
Noto Sans CherokeeNoto Sans Cherokee
Noto Sans CopticNoto Sans Coptic
Noto Sans DeseretNoto Sans Deseret
Noto Sans DevanagariNoto Sans Devanagari
Noto Sans EthiopicNoto Sans Ethiopic
Noto Sans GeorgianNoto Sans Georgian
Noto Sans GujaratiNoto Sans Gujarati
Noto Sans GurmukhiNoto Sans Gurmukhi
Noto Sans HanunooNoto Sans Hanunoo
Noto Sans HebrewNoto Sans Hebrew
Noto Sans JavaneseNoto Sans Javanese
Noto Sans KannadaNoto Sans Kannada
Noto Sans Kayah LiNoto Sans Kayah Li
Noto Sans KhmerNoto Sans Khmer
Noto Sans LaoNoto Sans Lao
Noto Sans LepchaNoto Sans Lepcha
Noto Sans LimbuNoto Sans Limbu
Noto Sans LisuNoto Sans Lisu
Noto Sans MalayalamNoto Sans Malayalam
Noto Sans MandaicNoto Sans Mandaic
Noto Sans Meetei MayekNoto Sans Meetei Mayek
Noto Sans MongolianNoto Sans Mongolian
Noto Sans MyanmarNoto Sans Myanmar
Noto Sans NKoNoto Sans NKo
Noto Sans New Tai LueNoto Sans New Tai Lue
Noto Sans Ol ChikiNoto Sans Ol Chiki
Noto Sans OriyaNoto Sans Oriya
Noto Sans OsageNoto Sans Osage
Noto Sans OsmanyaNoto Sans Osmanya
Noto Sans RejangNoto Sans Rejang
Noto Sans RunicNoto Sans Runic
Noto Sans SamaritanNoto Sans Samaritan
Noto Sans SaurashtraNoto Sans Saurashtra
Noto Sans ShavianNoto Sans Shavian
Noto Sans SinhalaNoto Sans Sinhala
Noto Sans SundaneseNoto Sans Sundanese
Noto Sans Syloti NagriNoto Sans Syloti Nagri
Noto Sans SymbolsNoto Sans Symbols
Noto Sans TagalogNoto Sans Tagalog
Noto Sans TagbanwaNoto Sans Tagbanwa
Noto Sans Tai LeNoto Sans Tai Le
Noto Sans Tai ThamNoto Sans Tai Tham
Noto Sans Tai VietNoto Sans Tai Viet
Noto Sans TamilNoto Sans Tamil
Noto Sans TeluguNoto Sans Telugu
Noto Sans ThaanaNoto Sans Thaana
Noto Sans ThaiNoto Sans Thai
Noto Sans TifinaghNoto Sans Tifinagh
Noto Sans VaiNoto Sans Vai
Noto Sans YiNoto Sans Yi
Noto Serif ArmenianNoto Serif Armenian
Noto Serif BengaliNoto Serif Bengali
Noto Serif DevanagariNoto Serif Devanagari
Noto Serif EthiopicNoto Serif Ethiopic
Noto Serif GeorgianNoto Serif Georgian
Noto Serif GujaratiNoto Serif Gujarati
Noto Serif HebrewNoto Serif Hebrew
Noto Serif KannadaNoto Serif Kannada
Noto Serif KhmerNoto Serif Khmer
Noto Serif LaoNoto Serif Lao
Noto Serif MalayalamNoto Serif Malayalam
Noto Serif MyanmarNoto Serif Myanmar
Noto Serif SinhalaNoto Serif Sinhala
Noto Serif TamilNoto Serif Tamil
Noto Serif TeluguNoto Serif Telugu
Noto Serif ThaiNoto Serif Thai
STIX Two MathSTIX Two Math
Twemoji MozillaTwemoji Mozilla
"""
    fonts = normalize_repeated_fonts(raw_text)
    save_to_txt(fonts)
