from csv import reader #importa o leitor de csv
from os import walk #importa a propriedade walk do módulo OS, permtindo percorrer o sistema de arquivos
import pygame.image #importa a biblioteca do pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',') #lê o arquivo csv
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list=[]
    for _,__, img_files in walk(path): #lê o arquivo CSV com as listas de gramas, ignorando os 2 primeiros valores
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
        return surface_list