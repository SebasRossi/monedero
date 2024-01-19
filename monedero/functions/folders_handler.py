"""This module provides the functions to work with the forlder in Monedero"""
# monedero/functions/folders_handler.py

# TODO:
#   comprobar si .env existe - DONE
#   si no existe, crearlo - DONE
#   si existe, ver si esta vacio - DONE
#   si esta vacio, pasar el path que vino por CLI - DONE
#   si no vino path, usar el default - DONE
#   devolver path de carpetas - DONE


from os import path
from pathlib import Path


ENV_FILE = "monedero/_data_env/.env"  # para hacerlo configurable, pasar a clase todo esto
DATA_SAVING_FOLDER_DEFAULT = f"{str(Path.home())}/Documents/"

def environment(saving_path:str=None) -> str: # deberia ser un path
    """
        lee si existe o crea si no el archivo con configuraciones, en este caso de la carpeta de 
        guardado de archivos.
    """

    if not path.isfile(ENV_FILE): 
        create_env(ENV_FILE) # innecesaria la funcion pero queda para despues
    
    carpeta=read_data_from_env(ENV_FILE)["carpeta"] # algo no me gusta de esto

    if carpeta == 'None':
        if saving_path == None:
            carpeta=DATA_SAVING_FOLDER_DEFAULT
        else :
            carpeta=saving_path
            write_path_to_env(ENV_FILE, carpeta)
    
    return  carpeta


def create_env(env):
    with open(env, "a+") as f:
        f.write(f'carpeta:None')


def read_data_from_env(env):
    with open(env) as f:
        dictionary = dict (string.split(":") for string in f.read().splitlines() )
    return dictionary


def write_path_to_env(env, folder):
    # esto esta feo, pero para el caso esta bien
    with open(env,'r') as file: 
        data = file.readlines() 
    data[0] = f"carpeta:{folder}"
    with open(env,'w') as file: 
        file.writelines(data) 

