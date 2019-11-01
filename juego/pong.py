# -*- coding: utf-8 -*-
# ============================================================================
# =========================== MODULOS ========================================
# ============================================================================
import pygame
import random
import sys
# ============================================================================

# ============================================================================
# =========================== CONSTANTES =====================================
# ============================================================================
ANCHO = 800
ALTO = 480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
FPS = 60
# ============================================================================

# ============================================================================
# ======================== FUNCIONES DE AYUDA ================================
# ============================================================================
def texto(texto, tam=20, color=(0, 0, 0)):
    fuente = pygame.font.Font(None, tam)
    return fuente.render(texto, True, color)
# ============================================================================

# ============================================================================
# =========================== CLASES =========================================
# ============================================================================
class Bola():
    def __init__(self):
        self.pos = [ANCHO / 2, ALTO / 2]
        self.radio = 20
        self.velocidad = [4, 4 * random.random() + 4]
        self.incremento_velocidad = 1.1
        self.lado_impacto = ""
        self.sonido_rebote = pygame.mixer.Sound("rebote.wav")

    def hayImpacto(self):
        return self.lado_impacto

    def reiniciar(self):
        self.pos = [ANCHO / 2, ALTO / 2]
        self.velocidad = [4, 4 * random.random() + 4]
        if self.lado_impacto == "derecho":
            self.velocidad[0] *= -1
        self.lado_impacto = ""

    def actualizar(self, barra1, barra2):
        self.pos[0] += int(self.velocidad[0])
        self.pos[1] += int(self.velocidad[1])

        if self.pos[1] <= self.radio or self.pos[1] >= ALTO - self.radio:
            self.velocidad[1] *= -1

        elif self.pos[0] < self.radio + barra1.ancho():
            if self.pos[1] > barra1.posicion() and self.pos[1] < barra1.posicion() + barra1.largo():
                self.sonido_rebote.play()
                self.pos[0] = barra1.ancho() + self.radio
                self.velocidad[0] *= -1 * self.incremento_velocidad
            else:
                self.lado_impacto = "izquierdo"

        elif self.pos[0] >= ANCHO - self.radio - barra2.ancho():
            if self.pos[1] > barra2.posicion() and self.pos[1] < barra2.posicion() + barra2.largo():
                self.sonido_rebote.play()
                self.pos[0] = ANCHO - barra2.ancho() - self.radio
                self.velocidad[0] *= -1 * self.incremento_velocidad
            else:
                self.lado_impacto = "derecho"

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, BLANCO, self.pos, self.radio)

class Barra():
    def __init__(self, jugador):
        self.dimension = [15, 100]
        pos_vertical = ALTO / 2 - self.dimension[1] / 2

        if jugador == 1:
            self.pos = [0, pos_vertical]
        elif jugador == 2:
            self.pos = [ANCHO - self.dimension[0], pos_vertical]

        self.velocidad = 0
        self.aceleracion = 4

    def ancho(self):
        return self.dimension[0]

    def largo(self):
        return self.dimension[1]

    def posicion(self):
        return self.pos[1]

    def mover(self, direccion):
        if direccion == "no":
            self.velocidad = 0
        elif direccion == "arriba":
            self.velocidad = -self.aceleracion
        elif direccion == "abajo":
            self.velocidad = self.aceleracion

    def actualizar(self):
        self.pos[1] += self.velocidad

        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] + self.largo() > ALTO:
            self.pos[1] = ALTO - self.largo()

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, BLANCO, [self.pos, self.dimension])

# ============================================================================

# ============================================================================
# =========================== FUNCION PRINCIPAL ==============================
# ============================================================================
def main():
    # Iniciamos PyGame
    pygame.init()

    # Dimensiones y etiqueta de la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("PONG")

   # Se usa para establecer cuan rápido se actualiza la pantalla
    reloj = pygame.time.Clock()

    barra1 = Barra(1)
    barra2 = Barra(2)
    bola = Bola()

    sonido_pierdes = pygame.mixer.Sound("pierdes.wav")
    pausa = True
    texto_inicio = texto("Presione ESPACIO para continuar...", 40, ROJO)
    puntuacion = [0, 0]

    marcha = True
    while marcha:
        # establece los frames por segundo
        reloj.tick(FPS)

        # ============ INICIO MANEJADORES DE EVENTOS ====================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                marcha = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    marcha = False

                elif pausa and event.key == pygame.K_SPACE:
                    pausa = False

                if event.key == pygame.K_w:
                    barra1.mover("arriba")
                elif event.key == pygame.K_s:
                    barra1.mover("abajo")

                if event.key == pygame.K_UP:
                    barra2.mover("arriba")
                elif event.key == pygame.K_DOWN:
                    barra2.mover("abajo")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    barra1.mover("no")
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    barra2.mover("no")
        # =============== FIN MANEJADORES DE EVENTOS==========================

        # ============= AQUI VA LOGICA DEL JUEGO =============================
        barra1.actualizar()
        barra2.actualizar()

        if not pausa:
            bola.actualizar(barra1, barra2)
            if bola.hayImpacto():
                sonido_pierdes.play()
                pausa = True
                if bola.hayImpacto() == "izquierdo":
                    puntuacion[1] += 1
                else:
                    puntuacion[0] += 1

                bola.reiniciar()
        # ====================================================================

        # ============= AQUI VA LO QUE SE VA A DIBUJAR EN LA PANTALLA ========
        pantalla.fill(NEGRO) # pintamos la pantalla de negro

        # dibujar cancha
        pygame.draw.line(pantalla, BLANCO, (barra1.ancho(), 0), (barra1.ancho(), ALTO))
        pygame.draw.line(pantalla, BLANCO, (ANCHO - barra2.ancho(), 0), (ANCHO - barra2.ancho(),  ALTO))
        pygame.draw.line(pantalla, BLANCO, (ANCHO / 2, 0), (ANCHO / 2, ALTO))

        # dibujar puntuacion
        pantalla.blit(texto(str(puntuacion[0]), 100, BLANCO), (ANCHO / 4, 10))
        pantalla.blit(texto(str(puntuacion[1]), 100, BLANCO), ((ANCHO * 3 / 4) - 20, 10))

        # dibujar barras
        barra1.dibujar(pantalla)
        barra2.dibujar(pantalla)

        # dibujar bola
        bola.dibujar(pantalla)

        if pausa:
            pantalla.blit(texto_inicio, (ANCHO / 4, 100))

        # ====================================================================

        # Avanza y actualiza la pantalla con lo que hemos dibujado
        pygame.display.flip()
# ============================================================================

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()