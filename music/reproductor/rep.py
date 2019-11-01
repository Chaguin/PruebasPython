# -*- coding: utf-8 -*-

import sys
import reload
import pygame.mixer
import pygame.cdrom

pygame.mixer.init(44100, -16, 2, 4096)
reload()
sys.setdefaultencoding()
pygame.mixer.music.load('E:\Documentos\PRUEBAS PYTHON\music\reproductor')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)