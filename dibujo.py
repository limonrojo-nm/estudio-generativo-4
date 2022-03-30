from zlib import Dibujo, ConPosicion, Posicion, GenaradorRuido

class CacheFotograma:
    def __init__(self, valor=None, fotograma=None):
        self._en_cache = valor
        self._fotograma = fotograma
    
    @property
    def valor(self): return self._en_cache
    
    def set_valor(self, _valor): self._en_cache = _valor
    
    @property
    def fotograma(self): return self._fotograma
    
    def set_fotograma(self, _fotograma): self._fotograma = _fotograma

class Particula(Dibujo, ConPosicion):
    _conectada = False
    _amplitud_ruido = 3
    _vitalidad = 20
    _hermana_actual = None
    
    def __init__(self):
        self._ngen_x = GenaradorRuido(0.02)
        self._ngen_y = GenaradorRuido(0.02)
        self._ngen_circ = GenaradorRuido(0.02)
        self._tamanho_cache = CacheFotograma()
        self._iniciar_posicion()
        self._randomizar_posicion()
     
    def procesar_fotograma(self, factory):
        self._randomizar_posicion()
        self._dibujar()
        self._cansarse(factory)
    
    def conectar(self, hermana):
        self._hermana_actual = hermana
        self._dibujar_conexion(self.hermana_actual)
        self.hermana_actual.alimentar()
    
    def alimentar(self): self._vitalidad += random(.2, 1)
    
    @property
    def hermana_actual(self): return self._hermana_actual
    @property
    def tiene_hermana(self): return self._hermana_actual is not None
    
    @property
    def tamanho(self):
        if self._tamanho_cache.valor is None or self._tamanho_cache.fotograma != self.c.fotograma:
            self._tamanho_cache.set_valor(self._ngen_circ()*30+self._vitalidad)
            self._tamanho_cache.set_fotograma(self.c.fotograma)
        return self._tamanho_cache.valor
    
    # Privados ----------------
    def _iniciar_posicion(self):
        x = random(0+self.c.ancho*self._ngen_x(), self.c.ancho-self.c.ancho*self._ngen_x())
        y = random(0+self.c.ancho*self._ngen_y(), self.c.alto-self.c.ancho*self._ngen_y())
        self._posicion = Posicion(x, y)
        
    def _randomizar_posicion(self):
        r_x = (self.posicion.x + (self._ngen_x()*self._amplitud_ruido*2 -self._amplitud_ruido)) % self.c.ancho
        r_y = (self.posicion.y + (self._ngen_y()*self._amplitud_ruido*2 -self._amplitud_ruido)) % self.c.alto
        self.posicion.reasignar(r_x, r_y)
    
    def _dibujar(self):
        self._dibujar_cuerpo()
        
    
    def _dibujar_cuerpo(self):
        color_linea_base = 220
        alpha_linea_base = 20
        pushStyle()
        stroke(color_linea_base, alpha_linea_base)
        colorMode(HSB)
        fill(120+self.tamanho*.1%360, 220, 200, 10)
        strokeWeight(5)
        circle(self.posicion.x+random(-2, 2), self.posicion.y+random(-2, 2), self.tamanho)
        for i in range(10):
            stroke(color_linea_base, alpha_linea_base+random(-80, 20))
            ellipse(self.posicion.x+random(-2, 2),
                    self.posicion.y+random(-2, 2),
                    self.tamanho - 3*((-i) +random(-2, 2)),
                    self.tamanho - 3*((-i) +random(-2, 2)))
        popStyle()
    
    def _dibujar_conexion(self, hermana):
        amplitud_rdm = 4
        pushStyle()
        colorMode(HSB)
        stroke(200-self.tamanho*.1%360, 200, 200, 100)
        strokeWeight(5)
        line(self.posicion.x+random(-amplitud_rdm, amplitud_rdm),
              self.posicion.y+random(-amplitud_rdm, amplitud_rdm),
              hermana.posicion.x+random(-amplitud_rdm, amplitud_rdm),
              hermana.posicion.y+random(-amplitud_rdm, amplitud_rdm))
        popStyle()
        
    def _cansarse(self, factory):
        self._vitalidad -= random(.2, .9) + self.tamanho * .001
        if self._vitalidad < 0:
            factory._particulas.remove(self)



class ParticulaFactory(Dibujo):
    _particulas = []
    
    def __init__(self, cantidad=1):
        self._generar_particulas(cantidad)
    
    def procesar_fotograma(self):
        if len(self._particulas) > 1:
            for particula in self._particulas:
                particula.procesar_fotograma(self)
                particula.conectar(self._particula_a_conectar(particula))
        else:
            exit()
                
    # Privados ----------------
    def _generar_particulas(self, cantidad):
        for _ in range(cantidad):
            self._particulas.append(Particula())
    
    def _particula_a_conectar(self, buscadora):
        cercana = None
        menor_distancia = float("inf")
        
        for particula in self._particulas:
            if particula != buscadora:
                distancia_absoluta = dist(buscadora.posicion.x,buscadora.posicion.y,
                                        particula.posicion.x,particula.posicion.y)
                distancia_relativa = distancia_absoluta - (particula.tamanho * 0.3)
                if buscadora.tiene_hermana and particula == buscadora.hermana_actual:
                    distancia_relativa = distancia_relativa * .4
                                        
                if distancia_relativa <= menor_distancia:
                    menor_distancia = distancia_relativa
                    cercana = particula
        return cercana
