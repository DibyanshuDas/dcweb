with open('src/pages/About.tsx', 'r') as f:
    content = f.read()

# Replace the messy line with a cleaner one
import re
new_bg = "backgroundImage: `url('data:image/svg+xml,%3Csvg width=\"100%25\" height=\"100%25\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M-10,40 Q25,10 60,60 T110,30\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,42 Q25,12 60,62 T110,32\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,44 Q25,14 60,64 T110,34\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,46 Q25,16 60,66 T110,36\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,48 Q25,18 60,68 T110,38\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,50 Q25,20 60,70 T110,40\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,52 Q25,22 60,72 T110,42\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,54 Q25,24 60,74 T110,44\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,56 Q25,26 60,76 T110,46\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,58 Q25,28 60,78 T110,48\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,60 Q25,30 60,80 T110,50\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3C/svg%3E')`"

content = re.sub(r'backgroundImage: "url\([^)]+\)"', new_bg, content)

with open('src/pages/About.tsx', 'w') as f:
    f.write(content)
print("Done")
