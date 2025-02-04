import sys
import glob, os

for file in glob.glob("*.png"):
    infile = file
    outfile = file.replace(".png", ".svg")

    from PIL import Image
    image = Image.open(infile).convert('RGBA')
    data = image.load()
    out = open(outfile, "w")
    out.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    out.write(
        '<svg id="svg2" xmlns="http://www.w3.org/2000/svg" version="1.1" width="%(x)i" height="%(y)i" viewBox="0 0 %(x)i %(y)i">\n'
        % {
            'x': image.size[0],
            'y': image.size[1]
        })
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            rgba = data[x, y]
            rgb = '#%02x%02x%02x' % rgba[:3]
            if rgba[3] > 0:
                out.write(
                    '<rect width="1" height="1" x="%i" y="%i" fill-opacity="%.2f" />\n'
                    % (x, y, rgba[3] / 255.0))
    out.write('</svg>\n')
    out.close()
