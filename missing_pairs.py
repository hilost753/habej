import os
import shutil

def clean_missing_pairs(folder_path):
    image_exts = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
    annotation_ext = ".txt"

    unmatched_folder = os.path.join(folder_path, "unmatched")
    os.makedirs(unmatched_folder, exist_ok=True)

    files = os.listdir(folder_path)

    # Separate images and text files
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_exts]
    texts  = [f for f in files if f.endswith(annotation_ext)]

    image_bases = {os.path.splitext(f)[0] for f in images}
    text_bases  = {os.path.splitext(f)[0] for f in texts}

    # Files with no matching annotation
    images_without_txt = image_bases - text_bases

    # Text files with no matching image
    txt_without_images = text_bases - image_bases

    # Move unmatched image files
    for base in images_without_txt:
        for ext in image_exts:
            img_file = base + ext
            full_path = os.path.join(folder_path, img_file)
            if os.path.exists(full_path):
                print(f"Moving unmatched image: {img_file}")
                shutil.move(full_path, unmatched_folder)

    # Move unmatched annotation files
    for base in txt_without_images:
        txt_file = base + ".txt"
        full_path = os.path.join(folder_path, txt_file)
        if os.path.exists(full_path):
            print(f"Moving unmatched annotation: {txt_file}")
            shutil.move(full_path, unmatched_folder)

    print("\n✔ Cleaning complete!")
    print(f"Unmatched files moved to: {unmatched_folder}")


# Example usage:
clean_missing_pairs("dataset")
