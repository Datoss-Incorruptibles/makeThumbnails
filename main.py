from PIL import Image, ImageDraw, ImageFilter , ImageFont
import requests


#  sacar la lista de urls de la db 
cesarUrlImage = 'https://declara.jne.gob.pe/Assets/Fotos-HojaVida/136626.jpg?1611899645675'
im2 = Image.open(requests.get(cesarUrlImage, stream=True).raw)

# get Data
cesarUrlData = 'https://api-dev.candidatos.pe/v1/candidato/34/?format=json'
data = requests.get(cesarUrlData)
data1 = data.json()


# create Canvas 
img = Image.new('RGB', (500, 300), (230, 230, 230))


# insert image candidato
  #resize
resized_im = im2.resize((round(im2.size[0]*0.5), round(im2.size[1]*0.5)))

draw = ImageDraw.Draw(img)
# draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)

img.paste(resized_im,(50, 50))



# Insert Text to image

#Create an Image Object from an Image
width, height = img.size

draw = ImageDraw.Draw(img)
text1 = data1["id"]
text2 = data1["jne_organizacion_politica"]
text3 = data1["nombres"]
text4 = data1["profesion"]


# font = ImageFont.load_default()
# font = ImageFont.truetype( 36)
font = ImageFont.truetype('Roboto-Light.ttf', 1000)
# textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((300, 100), str(text1), fill=(255, 0, 0))
draw.text((300, 120), str(text2), fill=(255, 0, 0))
draw.text((300, 140), str(text3), fill=(255, 0, 0))
draw.text((300, 160), str(text4), fill=(255, 0, 0))

img.show()



# img.show()