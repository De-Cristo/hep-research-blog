"""Finalize the reviewed Quarto output for GitHub Pages."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / 'docs'
for path in root.glob('*.html'):
    text = path.read_text()
    if not text.lstrip().lower().startswith('<!doctype html>'):
        path.write_text('<!doctype html>\n' + text)
(root / '.nojekyll').write_text('')

# Keep a GitHub-rendered reading copy in sync with the canonical Quarto source.
project = root.parent
source = (project / 'index.qmd').read_text().split('---', 2)[2].strip()
reading_copy = project / 'weekly' / '2026-11-04.md'
reading_copy.parent.mkdir(exist_ok=True)
reading_copy.write_text('# HEP weekly reading for 4 November 2026\n\n' + source + '\n')
