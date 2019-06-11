from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont
image = Image.open('/media/chaand/New Volume4/Coding/Python/OCR/image.jpg')
enhancer = ImageEnhance.Color(image)
images = []
for i in range(0, 10):
	images.append(enhancer.enhance(i/10))
first_image = images[0]
contact_sheet = Image.new(first_image.mode, (first_image.width*3, first_image.height*3))
x , y =0, 0
fnt = ImageFont.truetype('/media/chaand/New Volume4/Coding/Python/OCR/font.odt', 40)
temp_img = images[0]
for img in images:
	txt = Image.new('RGBA', img.size, (255,255,255,0))
	d = ImageDraw.Draw(txt)
	d.text((10,60), "x"+ str(x) + "y" + str(y) , font=fnt, fill=(255,255,255,255))
	pixelMap = first_image.load()
	pix_val = list(first_image.getdata())
	if(x == 0):
		pix_val1 = [(s[0]+(80), s[1], s[2]) for s in pix_val]
	if(x == (x + first_image.width)):
		pix_val1 = [(s[0], s[1]+(80), s[2]) for s in pix_val]
	if(x == (x + first_image.width + first_image.width)):
		pix_val1 = [(s[0], s[1], s[2]+(80)) for s in pix_val]
	temp_img.putdata(pix_val1, scale = 1.0)
	contact_sheet.paste(temp_img, (x, y))
	if(x+first_image.width == contact_sheet.width):
		x = 0
		y = y + first_image.height
	else:
		x = x + first_image.width
#contact_sheet = contact_sheet.resize((int(contact_sheet.width)))	
contact_sheet.save('temp111.png')
