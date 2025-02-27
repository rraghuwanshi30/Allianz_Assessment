import zipfile
import os

def save_html_to_zip(html_pages: list, zip_filename="hockey_pages.zip"):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for i, html in enumerate(html_pages, start=1):
            file_name = f"{i}.html"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(html)
            zipf.write(file_name)
            os.remove(file_name)
    print(f"Saved all HTML pages in {zip_filename}")
