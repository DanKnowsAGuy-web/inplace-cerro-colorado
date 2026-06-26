# -*- coding: utf-8 -*-
# Regenerates every image in assets/img/ from the original scanned report PDF.
# Put the PDF in source/ (any *.pdf), then run:  python3 src/extract_images.py
# Requires: poppler-utils (pdftoppm) on the system, plus Pillow and numpy.
import os, glob, subprocess, tempfile
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = glob.glob(os.path.join(ROOT,'source','*.pdf'))
OUT  = os.path.join(ROOT,'assets','img')
os.makedirs(OUT, exist_ok=True)
if not SRC:
    raise SystemExit('No PDF found in source/. Drop the original report PDF there first.')
PDF = SRC[0]
print('Source PDF:', os.path.basename(PDF))

TMP = tempfile.mkdtemp()
def render(page, dpi):
    pre = os.path.join(TMP, f'p{page}_{dpi}')
    subprocess.run(['pdftoppm','-jpeg','-r',str(dpi),'-f',str(page),'-l',str(page),PDF,pre],
                   check=True)
    f = glob.glob(pre+'*')[0]
    return Image.open(f).convert('RGB')

def save(im, name, w, q=78):
    if im.width > w:
        im = im.resize((w, int(im.height*w/im.width)))
    im.save(os.path.join(OUT, name+'.jpg'), quality=q, optimize=True)

def longest_run(mask):
    best=(0,0); i=0; n=len(mask)
    while i<n:
        if mask[i]:
            j=i
            while j<n and mask[j]: j+=1
            if j-i>best[1]-best[0]: best=(i,j)
            i=j
        else: i+=1
    return best

def single_photo(page):
    im = render(page, 200); a=np.asarray(im).astype(np.int16); W,H=im.size
    bright=a.mean(axis=2); chroma=a.max(axis=2)-a.min(axis=2)
    ink=((bright<225)|(chroma>28)); ink[:150,:]=0; ink[2150:,:]=0
    y0,y1=longest_run(ink.mean(axis=1)>0.30)
    sub=ink[y0:y1,:]; x0,x1=longest_run(sub.mean(axis=0)>0.30)
    return im.crop((int(x0),int(y0),int(x1),int(y1)))

# Single-photo process pages
for page,name in [(10,'pg10_1'),(11,'pg11_1'),(12,'pg12_1'),(13,'pg13_1'),(14,'pg14_1')]:
    save(single_photo(page), name, 820)
    print('photo', name)

# Panel pages: 2 columns x 3 rows
COLS=[(248,768),(858,1390)]; ROWS=[(206,650),(786,1208),(1326,1748)]
for page in (29,30,31):
    im=render(page,200); k=0
    for (y0,y1) in ROWS:
        for (x0,x1) in COLS:
            k+=1; save(im.crop((x0,y0,x1,y1)), f'pg{page}_{k}', 820)
    print('panel page', page)

# Laboratory certificates (pages 17-28): trim margins and footer
for p in range(17,29):
    im=render(p,170); W,H=im.size
    save(im.crop((int(W*0.04),int(H*0.02),int(W*0.97),int(H*0.965))), f'cert{p}', 1000, 72)
    print('cert', p)

# Engineering drawings
im=render(32,170); W,H=im.size
save(im.crop((int(W*0.03),int(H*0.20),int(W*0.99),int(H*0.80))), 'draw32', 1500)
im=render(33,170); W,H=im.size
save(im.crop((int(W*0.03),int(H*0.02),int(W*0.99),int(H*0.965))), 'draw33', 1300)
print('drawings done')
print('All images written to', OUT)
