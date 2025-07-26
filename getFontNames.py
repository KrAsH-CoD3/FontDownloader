import os

#  Get font names from folder and remove extension
directory_path = r"Path/to/fonts"

file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

with open('Output/path/to/fonts_names.txt', 'w', encoding='utf-8') as f:
    for name in file_names:
        new_name = name.split('.')[0]
        f.write(new_name + '\n')
