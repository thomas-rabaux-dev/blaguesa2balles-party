#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

os.chdir('Content')

placeholders = [
    ('avoir_faim.jpg', 394, 361),
    ('baby_bubble.jpg', 382, 480),
    ('essayage[1].jpg', 367, 489),
    ('football.jpg', 400, 427),
    ('iloveyou2.jpg', 500, 375),
    ('laveur_carreau.jpg', 369, 388),
    ('lifting.jpg', 323, 397),
    ('mini_jedi.jpg', 247, 331),
    ('neige.jpg', 319, 435),
    ('os_chien.jpg', 362, 450),
    ('photo_cochonne.jpg', 465, 473),
    ('photocopieuse.jpg', 450, 462),
    ('photographe.jpg', 454, 355),
    ('place_parking_femme.gif', 280, 184),
    ('premierbaiser.jpg', 548, 413),
    ('se_produire.gif', 260, 400),
    ('souriez.jpg', 300, 364),
    ('va_chercher_nonos.jpg', 550, 405),
    ('voyeur.jpg', 362, 497)
]

for filename, width, height in placeholders:
    if not os.path.exists(filename):
        img = Image.new('RGB', (width, height), color=(220, 220, 220))
        draw = ImageDraw.Draw(img)
        text = '[Not archived]'
        draw.text((width//2-50, height//2), text, fill=(100, 100, 100))
        img.save(filename)
        print(f'Created {filename}')
    else:
        print(f'Skipped {filename} (exists)')

print('Done!')
