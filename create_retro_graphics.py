#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.chdir('images')

# Retro web colors from late 90s/early 2000s
BLUE_GRADIENT_START = (102, 153, 204)  # #6699CC
BLUE_GRADIENT_END = (68, 119, 170)     # #4477AA
ORANGE = (255, 153, 51)                 # #FF9933
ORANGE_DARK = (204, 102, 0)            # #CC6600
GRAY = (192, 192, 192)                  # #C0C0C0
WHITE = (255, 255, 255)
DARK_GRAY = (102, 102, 102)

def gradient_vertical(width, height, color1, color2):
    """Create vertical gradient"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def create_button(width, height, text, bg_color1, bg_color2):
    """Create a button with gradient and text"""
    img = gradient_vertical(width, height, bg_color1, bg_color2)
    draw = ImageDraw.Draw(img)
    
    # Try to use a nicer font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    except:
        font = ImageFont.load_default()
    
    # Center text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 2
    
    # Text with shadow
    draw.text((x+1, y+1), text, fill=DARK_GRAY, font=font)
    draw.text((x, y), text, fill=WHITE, font=font)
    
    return img

print("Creating retro-styled navigation graphics...")

# Header left (493x146) - Main title area
img = gradient_vertical(493, 146, BLUE_GRADIENT_START, BLUE_GRADIENT_END)
draw = ImageDraw.Draw(img)
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

draw.text((20, 40), "Site perso de", fill=WHITE, font=subtitle_font)
draw.text((20, 70), "Simon Rabaux", fill=WHITE, font=title_font)
img.save('index_01.gif')
print("✓ Created index_01.gif (header left)")

# Header right (307x146) - Complementary header
img = gradient_vertical(307, 146, BLUE_GRADIENT_START, BLUE_GRADIENT_END)
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font = ImageFont.load_default()
draw.text((40, 60), "Blagues à", fill=WHITE, font=font)
draw.text((40, 90), "2 balles", fill=WHITE, font=font)
img.save('index_02.gif')
print("✓ Created index_02.gif (header right)")

# Sub-banner (648x64)
img = gradient_vertical(648, 64, ORANGE, ORANGE_DARK)
img.save('index_03.gif')
print("✓ Created index_03.gif (sub-banner)")

# Small header element (152x64)
img = gradient_vertical(152, 64, GRAY, (160, 160, 160))
img.save('index_04.gif')
print("✓ Created index_04.gif (header element)")

# Center decorative (315x256) - Large decoration
img = Image.new('RGB', (315, 256), (245, 245, 245))
draw = ImageDraw.Draw(img)
# Draw some retro geometric shapes
for i in range(5):
    x = 50 + i * 50
    y = 80 + i * 20
    draw.rectangle([x, y, x+40, y+40], fill=BLUE_GRADIENT_START, outline=BLUE_GRADIENT_END)
img.save('index_13.gif')
print("✓ Created index_13.gif (center decoration)")

# Blagues perso button (183x56)
img = create_button(183, 56, "Blagues perso", ORANGE, ORANGE_DARK)
img.save('index_14.gif')
print("✓ Created index_14.gif (blagues perso button)")

# Videos button (96x56)
img = create_button(96, 56, "Vidéos", ORANGE, ORANGE_DARK)
img.save('index_16.gif')
print("✓ Created index_16.gif (videos button)")

# Bottom decoration (414x70)
img = gradient_vertical(414, 70, GRAY, (200, 200, 200))
img.save('index_17.gif')
print("✓ Created index_17.gif (bottom decoration)")

print("\n✓ All 8 missing navigation graphics created!")
print("Run 'open ../index.html' to preview the site.")
