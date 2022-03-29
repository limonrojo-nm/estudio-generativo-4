from zlib import c, DibujoPrincipal
dibujo_principal = DibujoPrincipal([])

def setup():
    size(c.ancho, c.alto)
    frameRate(c.fps)
    background(*c.bg_color)

def draw():
    dibujo_principal.dibujar()
    c.procesar_fotograma()
    # exportador_fotogramas()
