"""This module provides the functions to work with the forlder in Monedero"""
# monedero/functions/folders_handler.py

# comprobar si env.spr existe
# si no existe, crearlo
# si existe, ver si esta vacio
# si esta vacio, pasar el path que vino por CLI
# si no vino path, usar el default
# devolver path de carpetas


import os.path


ENV_FILE = ".env"
DEFAULT = ''

def environment(path:str=None) -> str: # deberia ser un path

    if not os.path.isfile(ENV_FILE):
        create_env(ENV_FILE)
    
    carpeta=read_path_from_env(ENV_FILE)

    if carpeta == None:
        if path == None :
            carpeta=DEFAULT
        else :
            carpeta=path
            write_path_to_env(ENV_FILE)
            
    return carpeta


def create_env(env):
    pass


def read_path_from_env(env):
    return None


def write_path_to_env(env):
    pass
