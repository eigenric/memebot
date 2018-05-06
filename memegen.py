import os
from textwrap import wrap

from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color


def get_length(width):
    return int((33.0 / 1024.0) * (width + 0.0))


def generar_meme(texto, nombre_imagen):
    imagen = Image(filename=nombre_imagen)
    imagen.resize(1024,
                  int(((imagen.height * 1.0) / (imagen.width * 1.0)) * 1024.0))

    texto = "\n".join(wrap(texto, get_length(imagen.width))).upper()

    text_draw = Drawing()

    text_draw.font = os.path.join(os.getcwd(), "impact.ttf")
    text_draw.font_size = 60
    text_draw.text_alignment = "center"
    text_draw.stroke_color = Color("black")
    text_draw.stroke_width = 3
    text_draw.fill_color = Color("white")

    if texto:
        text_draw.text(imagen.width * 60//100, imagen.height * 55//100, texto)

    text_draw(imagen)

    imagen.save(filename=os.path.join(os.getcwd(), "memes", "meme.jpg"))
