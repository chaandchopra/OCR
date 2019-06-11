from PIL import Image
from PIL import ImageEnhance
#from IPython.display import display
image = Image.open('/media/chaand/New Volume4/Coding/Python/OCR/image.jpg')
pixelMap = image.load()
image=image.convert('RGB')
pix_val = list(image.getdata())
pix_val1 = [(s[0]+80, s[1], s[2]) for s in pix_val]
#for i in pix_val:
#	temp = list(i)
#	for j in range(0, 3):				
#		if(j == 0):
#			temp[0] = (temp[0]+ 80)%255
#			i = tuple(temp)
image.putdata(pix_val1, scale = 1.0)
image.show()
#image.show()
#img = Image.new( image.mode, image.size)
#pixelsNew = image.load()
#print(pixelMap[0,0])
#for i in range(img.size[0]):
#	for j in range(img.size[1]):
#		color = image.getpixel((i, j))
#		print(color)
#		new_color = tuple(
#		if 205 in pixelMap[i,j]:
#			pixelMap[i,j] = (0,0,0,255)
#		pixelsNew[i,j] = pixelMap[i,j]
#image.close()
#img.show()
#img.save('tee.jpg')
#img.close()


