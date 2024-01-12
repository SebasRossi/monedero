"""This module provides the functions to work with the forlder in Monedero"""
# monedero/functions/folders_handler.py

# TODO:
#   comprobar si .env existe - DONE
#   si no existe, crearlo
#   si existe, ver si esta vacio
#   si esta vacio, pasar el path que vino por CLI
#   si no vino path, usar el default
#   devolver path de carpetas


from os import path, getcwd
from pathlib import Path
#import os


ENV_FILE = "monedero/_data_env/.env"  # para hacerlo configurable, pasar a clase todo esto
DATA_SAVING_FOLDER_DEFAULT = f"{str(Path.home())}/Documents"

def environment(saving_path:str=None) -> str: # deberia ser un path

    # https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/work-with-files-directories-paths-in-python/set-working-directory-os-package/

    if not path.isfile(ENV_FILE): 
        create_env(ENV_FILE)
    
    carpeta=read_data_from_env(ENV_FILE)["carpeta"]

    if carpeta == 'None':
        if saving_path == None:
            carpeta=DATA_SAVING_FOLDER_DEFAULT
        else :
            carpeta=saving_path
            write_path_to_env(ENV_FILE)
    
    return  carpeta #getcwd() # carpeta


def create_env(env):
    with open(env, "a+") as f:
        f.write(f'carpeta:None')


def read_data_from_env(env):
    with open(env) as f:
        dictionary = dict (string.split(":") for string in f.read().splitlines() )
    return dictionary


def write_path_to_env(env):
    #encontrar la linea carpeta y reemplazarla 
    #con json es facil, hagamosla con txtg
    pass
