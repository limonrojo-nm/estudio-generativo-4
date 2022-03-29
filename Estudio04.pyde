from zlib import c

def setup():
    size(c.ancho, c.alto)
    frameRate(c.fps)
    background(c.bg_color, c.bg_alpha)

def draw():
    # dibujo_principal.dibujar()
    c.procesar_fotograma()
    # exportador_fotogramas()
