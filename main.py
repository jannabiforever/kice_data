import os
import schema


PNG_ROOT_FOLDER = "png/"


def folders():
    """Return a generator of folder paths in the PNG_ROOT_FOLDER.
    which looks like this: 'png/2025_11'"""
    for item in os.listdir(PNG_ROOT_FOLDER):
        item_path = os.path.join(PNG_ROOT_FOLDER, item)
        if os.path.isdir(item_path):
            yield item_path


def main():
    for folder in folders():
        print(f"processing folder: {folder}")
        png_files = sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.png')])
        for idx, scheme in enumerate(schema.SCHEMA):
            formatted_idx = str(idx + 1).zfill(2)
            cropped = schema.get_piece(png_files, scheme)
            cropped.save(os.path.join(folder, f"{formatted_idx}.png"))


if __name__ == "__main__":
    main()
