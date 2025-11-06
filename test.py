import os

def combine_files_with_headers(folder_path):
    output_filename = 'dock_x_df.txt'
    output_path = os.path.join("C:\\Users\\JustImagine\\workspace\\python\\python\\", output_filename)

    with open(output_path, 'w', encoding='utf-8', errors='replace') as out_file:
        for root, dirs, files in os.walk(folder_path):
            for fname in files:
                if fname == output_filename:
                    continue
                fpath = os.path.join(root, fname)
                # Create a relative path for the header
                rel_path = os.path.relpath(fpath, folder_path)
                header = f"//{rel_path.replace(os.sep, '/')}"
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except Exception as e:
                    content = f"[Error reading file: {e}]"
                out_file.write(f"{header}\n{content.rstrip()}\n")

if __name__ == "__main__":
    folder = "C:\\Users\\JustImagine\\workspace\\flutter\\lord_ayyappa_app\\ayyappa_app\\lib"
    if os.path.isdir(folder):
        combine_files_with_headers(folder)
        print("Combined file created as 'dock_x_df.txt'.")
    else:
        print("Invalid folder path.")