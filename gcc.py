from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

names = [
"Alice",
"Bob",
"Mallory"
]

for name in names:
	img = Image.open("/path/to/your/e-card.png")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("/path/to/fontfile.ttf", 20)

    # offset where to start drawing text
	mainoffset = (103,425)
	xoff,yoff = mainoffset
	draw.text(mainoffset,"Dear " + name + ",",(0,0,0),font=font)

    # save the file with the person's name
    # use Excel/Word to mail-merge and send out any number of custom e-cards
	img.save(name + '-regular.png')