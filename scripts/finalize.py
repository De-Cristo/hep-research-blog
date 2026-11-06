"""Finalize the reviewed Quarto output for GitHub Pages."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'docs'
for path in root.glob('*.html'):
    text = path.read_text()
    if not text.lstrip().lower().startswith('<!doctype html>'):
        path.write_text('<!doctype html>\n' + text)
(root / '.nojekyll').write_text('')
