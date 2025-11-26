import os

def batch_rename(folder_path):
    IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

    files = os.listdir(folder_path)
    images = sorted([f for f in files if os.path.splitext(f)[1].lower() in IMG_EXTS])

    count = 1
    for img in images:
        name, ext = os.path.splitext(img)
        txt_file = name + ".txt"

        img_path = os.path.join(folder_path, img)
        txt_path = os.path.join(folder_path, txt_file)

        # New names
        new_base = f"{count:04d}"      # 0001, 0002, ...
        new_img = new_base + ext
        new_txt = new_base + ".txt"

        # Rename only if annotation exists
        if os.path.exists(txt_path):
            print(f"Renaming: {img} → {new_img}")
            print(f"Renaming: {txt_file} → {new_txt}")

            os.rename(img_path, os.path.join(folder_path, new_img))
            os.rename(txt_path, os.path.join(folder_path, new_txt))

            count += 1
        else:
            print(f"⚠️ Skipped (missing .txt): {img}")

    print("\n✔ Batch renaming complete!")

# Example usage:
batch_rename("dataset")
