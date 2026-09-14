#!/usr/bin/env python3
"""Post-render hook to ensure downloadable PDF (via Typst) and EPUB exist in _book/"""
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BOOK_DIR = BASE_DIR / "_book"
CACHE_DIR = BASE_DIR / ".cache_downloads"

def post_render():
    if not BOOK_DIR.exists():
        return
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Si se generó un nuevo Nous.pdf en _book (vía Typst), guardarlo en caché
    pdf_in_book = BOOK_DIR / "Nous.pdf"
    cache_pdf = CACHE_DIR / "Nous.pdf"
    if pdf_in_book.exists():
        shutil.copy2(pdf_in_book, cache_pdf)
    elif cache_pdf.exists():
        shutil.copy2(cache_pdf, pdf_in_book)
        print("📄 [Post-Render] Nous.pdf (Typst) asegurado en _book/")

    # 2. Si se generó un nuevo Nous.epub en _book, guardarlo en caché
    epub_in_book = BOOK_DIR / "Nous.epub"
    cache_epub = CACHE_DIR / "Nous.epub"
    if epub_in_book.exists():
        shutil.copy2(epub_in_book, cache_epub)
    elif cache_epub.exists():
        shutil.copy2(cache_epub, epub_in_book)
        print("📱 [Post-Render] Nous.epub asegurado en _book/")

if __name__ == "__main__":
    post_render()
