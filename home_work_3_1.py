import os
import shutil
import argparse


def copy_files(src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            # Створюємо відповідну піддиректорію в dest
            subdir = os.path.join(dest, item)
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            copy_files(s, subdir) # Рекурсивно копіюємо з піддиректорій
        else:
            file_extension = os.path.splitext(item)[1].lstrip('.').lower()
            if file_extension == '': # Якщо файл без розширення
                file_extension = 'no_extension'
            extension_dir = os.path.join(dest, file_extension)
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            shutil.copy2(s, os.path.join(extension_dir, item))


def main():
    parser = argparse.ArgumentParser(description="Копіювання файлів до нової директорії та сортування за розширенням.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("--dest", help="Шлях до директорії призначення", default="dist")

    args = parser.parse_args()

    try:
        if not os.path.exists(args.dest):
            os.makedirs(args.dest)
        copy_files(args.src, args.dest)
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
