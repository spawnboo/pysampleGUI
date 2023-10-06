# coding=utf-8
import os

import RecipeFunction.RecipeReader as Recipe_Load

# 取得該資料夾下所有Recipe檔案
def GetRecipeList(path):
    ALLfiles = []
    RL = []
    for _, folder, files in os.walk(path):
        ALLfiles.extend(files)

    for f in ALLfiles:
        if f.split('.')[1] == 'ini':
            RL.append(f.split('.')[0])
    return RL

def LoadRecipe(ini_path):
    recipe_read = Recipe_Load.load_ini_YOLOV4_new(ini_path)
    return recipe_read




if __name__ == "__main__":
    path = r"RecipeFunction\Recipe.ini"

    LoadRecipe(path)
