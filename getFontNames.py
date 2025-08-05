import os

#  Get font names from folder and remove extension
directory_path = r"C:\Users\LMAO\AppData\Local\camoufox\camoufox\Cache\fonts"

file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]


if __name__ == "__main__":
    with open(r'Fonts\Camoufox\Fonts_names.txt', 'w', encoding='utf-8') as f:
        for name in file_names:
            new_name = name.split('.')[0]
            f.write(new_name + '\n')
