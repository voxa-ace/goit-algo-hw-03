import argparse
import shutil
import logging
from pathlib import Path


def setup_logging():
    """Set logging"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_directory(path):
    """Create a directory if not exists"""
    try:
        path.mkdir(exist_ok=True, parents=True)
    except PermissionError:
        logging.error(f"Permission denied: cannot create directory {path}")
    except FileExistsError:
        logging.error(f"Directory {path} already exists, but is not a directory")
    except Exception as e:
        logging.error(f"Unexpected error when creating a directory {path}: {e}")


def copy_file(src_file, dest_dir):
    """Copies the file to the appropriate directory."""
    try:
        shutil.copy2(src_file, dest_dir)
        logging.info(f"File {src_file} successfully copied to {dest_dir}")
    except FileNotFoundError:
        logging.error(f"File not found: {src_file}")
    except PermissionError:
        logging.error(f"Permission denied: cannot copy file {src_file}")
    except Exception as e:
        logging.error(f"Error copying {src_file}: {e}")


def process_files(src, dest):
    """Processes all files in the directory"""
    src_path = Path(src)
    dest_path = Path(dest)

    for item in src_path.rglob('*'):
        if item.is_file():
            file_extension = item.suffix[1:].lower() or 'no_extension'
            extension_dir = dest_path / file_extension
            create_directory(extension_dir)
            copy_file(item, extension_dir / item.name)


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Copy files to a new directory and sort by extension.")
    parser.add_argument("src", help="Path to the source directory")
    parser.add_argument("--dest", help="Path to the destination directory", default="dist")

    args = parser.parse_args()

    try:
        process_files(args.src, args.dest)
    except Exception as e:
        logging.error(f"Error in the copying process: {e}")
        logging.debug("Error details", exc_info=True)


if __name__ == "__main__":
    main()
