from PIL import Image, ImageDraw, ImageFilter , ImageFont
import requests


# create Canvas 
canvas = Image.new('RGB', (400, 250), (230, 230, 230))
draw = ImageDraw.Draw(canvas)

#####################
#  sacar la lista de urls de CANDIDATO de la db 
cesarUrlImage = 'https://declara.jne.gob.pe/Assets/Fotos-HojaVida/136626.jpg?1611899645675'
candidatoImg = Image.open(requests.get(cesarUrlImage, stream=True).raw)

# insert image candidato
# resize
resized_candidato = candidatoImg.resize((round(candidatoImg.size[0]*0.25), round(candidatoImg.size[1]*0.25)))
canvas.paste(resized_candidato,(20, 20))
# draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)

#####################

#  sacar la lista de urls de PARTIDO de la db 
partidoUrlImage = 'https://aplicaciones007.jne.gob.pe/srop_publico/Consulta/Simbolo/GetSimbolo/1257'
partidoImg = Image.open(requests.get(partidoUrlImage, stream=True).raw)

# insert image partido
  #resize
resized_partido = partidoImg.resize((round(partidoImg.size[0]*0.15), round(partidoImg.size[1]*0.15)))
# draw = ImageDraw.Draw(canvas)
canvas.paste(resized_partido,(80, 100))
# draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)

#####################

# import images and icons 
museum = Image.open("museum.png")
like = Image.open("like.png")
dislike = Image.open("dislike.png")
description = Image.open("description.png")


resized_museum = museum.resize((round(museum.size[0]*0.08), round(museum.size[1]*0.08)))
canvas.paste(resized_museum,(20, 160),resized_museum)



# get TEXT Data
# CONSTATNS 
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 

font10 = ImageFont.truetype('Roboto-Light.ttf', 10)
font12 = ImageFont.truetype('Roboto-Light.ttf', 12)
font14 = ImageFont.truetype('Roboto-Light.ttf', 14)

font16 = ImageFont.truetype('Roboto-Light.ttf', 16)
font20 = ImageFont.truetype('Roboto-Light.ttf', 20)
font30 = ImageFont.truetype('Roboto-Light.ttf', 30)

cesarUrlData = 'https://api-dev.candidatos.pe/v1/candidato/34/?format=json'
requestData = requests.get(cesarUrlData)
data = requestData.json()

# Insert Text to image
# Create an Image Object from an Image
width, height = canvas.size
draw = ImageDraw.Draw(canvas)


text1 = data["jne_organizacion_politica"]
text2 = f'{data["nombres"]} {data["apellido_paterno"]} {data["apellido_materno"]}'


# draw watermark in the bottom right corner
draw.text((125, 20), str(text1), fill=BLACK,font=font10)
draw.text((125, 40), str(text2), fill=BLACK,font=font20)


text3 = data["profesion"]

import textwrap
lines = textwrap.wrap(text3, width=30)
y_text = 80
for line in lines:
  line_width, line_height = font14.getsize(line)
  draw.text((125 , y_text), line, fill=BLACK,font=font14)
  y_text += line_height + 5  # add spacer bottom




canvas.show()


