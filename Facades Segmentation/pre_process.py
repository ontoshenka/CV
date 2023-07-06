import os
import shutil

from tqdm import tqdm
from PIL import Image
from paths import *

for file in tqdm(os.listdir(CMP_DB_PATH)):
    file_name = file.split(r'/')[-1]
    if file.endswith('.jpg'):
        shutil.move(f'{CMP_DB_PATH}/{file}', f'{CMP_FACADES_PATH}/{file_name}')
    elif file.endswith('.png'):
        rgb_path = file[:-4] + '.jpg'
        im = Image.open(f'{CMP_DB_PATH}/{file}')
        rgb_im = im.convert('RGB')
        rgb_im.save(f'{CMP_MASKS_PATH}/{rgb_path}')
    
shutil.rmtree(CMP_DB_PATH) 

for PATH in [TMBUD_FACADES_PATH, TMBUD_MASKS_PATH, TMBUD_EDGES_PATH]:
    for file in tqdm(os.listdir(PATH)):
        file_name = file.split(r'/')[-1]
        full_path = f'{PATH}/{file}'
        im = Image.open(f'{full_path}')
        rgb_im = im.convert('RGB')

        new_path = full_path[:-4] + '.jpg'
        rgb_im.save(f'{new_path}')

        os.remove(f'{full_path}')

for file in tqdm(os.listdir(KG_FACADES_PATH)):
    if '_A' in file:
        new_file = file.replace('_A', '_B')
        os.rename(f'{KG_FACADES_PATH}/{file}', f'{KG_FACADES_PATH}/{new_file}')

for file in tqdm(os.listdir(KG_MASKS_PATH)):
    if '_B' in file:
        new_file = file.replace('_B', '')
        os.rename(f'{KG_MASKS_PATH}/{file}', f'{KG_MASKS_PATH}/{new_file}')