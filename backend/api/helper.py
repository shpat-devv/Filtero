#helpers file to take care of extra functionality inside the views.py

import os
import subprocess
import pathlib
from PIL import Image

current_path = pathlib.Path().resolve()

image_processor = os.path.join(current_path, "api/image_process", "filter")
allowed_filters = ["blur", "grayscale", "sepia", "invert"]
out_file = "image.bmp"

def delete_file(url):
    os.remove(url)

def apply_filter(in_file, filter_name, out_file):
    if filter_name.lower() not in allowed_filters:
        raise ValueError(f"Filter '{filter_name}' is not allowed")

    if hasattr(in_file, 'path'):
        in_path = in_file.path 
    else:
        in_path = str(in_file)

    out_path = str(out_file)

    try:
        with Image.open(in_path) as img:
            img.convert("RGB").save(in_path)
    except Exception as e:
        print(f"Failed to convert image {in_path} to RGB: {e}")
        raise

    try:
        result = subprocess.run(
            [image_processor, filter_name[0], in_path, out_path],
            check=True,
            capture_output=True,
            text=True
        )
        print("Filter applied successfully")
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Couldn't execute {image_processor} with filter {filter_name}")
        print("Return code:", e.returncode)
        print("stdout:", e.stdout)
        print("stderr:", e.stderr)
        raise
