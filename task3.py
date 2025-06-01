import os
import shutil


source_folder = "source_images"
destination_folder = "jpg_images"


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


files_moved = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")
        files_moved += 1

print(f"\nTotal .jpg files moved: {files_moved}")
