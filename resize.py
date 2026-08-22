import sys
from PIL import Image
img = Image.open('public/team/alumni/shristi-singh.jpg')
img.thumbnail((300, 300))
img.save('shristi_small.jpg', format='JPEG', quality=85)
