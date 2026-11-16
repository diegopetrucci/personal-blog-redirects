#!/usr/bin/env python3
"""Build the legacy hostname site, refreshing feeds from the live personal blog."""
from pathlib import Path
import shutil
from urllib.request import urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / '_site'
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
for source in ROOT.iterdir():
    if source.name in {'_site', '.git', '.github', 'scripts', 'README.md', '.gitignore'}:
        continue
    destination = OUTPUT / source.name
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)

for remote, local in [('feed.xml', 'feed.xml'), ('feed/', 'feed/index.html')]:
    with urlopen('https://diegopetrucci.github.io/blog/' + remote, timeout=30) as response:
        content = response.read()
    ET.fromstring(content)
    destination = OUTPUT / local
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)
print('Built legacy redirects and refreshed both feeds from the live blog.')
