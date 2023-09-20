# coding=utf-8
import os


# 取得該資料夾下所有Recipe檔案
def GetRecipeList(path):
    RL = []
    for _, folder, files in os.walk(path):
        ALLfiles = files

    for f in ALLfiles:
        if f.split('.')[1] == 'ini':
            RL.append(f.split('.')[0])
    return RL





if __name__ == "__main__":
    path = r"D:\PycharmProjects\new_ML_Flask_Server\ML_Flask_Server\DL_Train\RecipeConfig"

    RL =GetRecipeList(path)
    print (RL)