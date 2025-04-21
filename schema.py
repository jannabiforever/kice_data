import json
from PIL import Image

# No DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

_SCHEMA_FILE_PATH = "schema.json"

def _load_schema():
    with open(_SCHEMA_FILE_PATH, 'r') as file:
        return json.load(file)


SCHEMA = _load_schema()

def get_piece(png_files: list[str], scheme):
    page, box = scheme['page'], tuple(scheme['box'])
    image = Image.open(png_files[page])
    piece = image.crop(box)
    return piece

if __name__ == "__main__":
    for i, scheme in enumerate(SCHEMA):
        page = scheme['page']
        print(f"Page: {page}")
        print(f"Box: {scheme["box"]}")
