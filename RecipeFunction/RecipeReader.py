# coding=utf-8
"""
    用以讀取Recipe.ini 的txt檔案

    *   節點名稱需依樣
"""
import configparser
from easydict import EasyDict as edict

# 老方法
# def load_ini_YOLOV4(configFilePath):
#     #   讀入 設定檔(.ini) 並把參數丟入config中
#     configParser = configparser.RawConfigParser()
#     configParser.read(configFilePath)
#     #   顯示所有節點[sections]
#     sections = configParser.sections()
#     #   指定節點的option
#     options = configParser.options("PATH")
#     #   指定節點的對應值
#     cnn   = configParser.items("PATH")
#
#     __C                             = edict()
#     # Consumers can get config by: from config import cfg
#     recipe                          = __C
#
#
#     # [PATH]
#     __C.PATH                        = edict()
#
#     __C.PATH.annotation_path        = configParser.get("PATH", "annotation_path")
#     __C.PATH.verified_data_start    = configParser.get("PATH", "verified_data_start")
#     __C.PATH.verified_data_end      = configParser.get("PATH", "verified_data_end")
#     __C.PATH.classes_path           = configParser.get("PATH", "classes_path")
#     __C.PATH.anchors_path           = configParser.get("PATH", "anchors_path")
#     __C.PATH.weights_path           = configParser.get("PATH", "weights_path")
#     __C.PATH.basic_weights_path     = configParser.get("PATH", "basic_weights_path")
#     __C.PATH.log_dir                = configParser.get("PATH", "log_dir")
#
#     # [TRAIN]
#     __C.TRAIN = edict()
#
#     __C.TRAIN.model                  = configParser.get("TRAIN", "model")
#     __C.TRAIN.input_shape            = (int(configParser.get("TRAIN", "input_shape_W")), int(configParser.get("TRAIN", "input_shape_H")))
#     __C.TRAIN.label_smoothing        = int(configParser.get("TRAIN", "label_smoothing"))
#     __C.TRAIN.normalize              = int(configParser.get("TRAIN", "label_smoothing"))
#     __C.TRAIN.Modelsummary           = int(configParser.get("TRAIN", "Modelsummary"))
#     __C.TRAIN.mosaic                 = int(configParser.get("TRAIN", "mosaic"))
#
#     __C.TRAIN.val_split              = float(configParser.get("TRAIN", "val_split"))
#     __C.TRAIN.Init_epoch             = int(configParser.get("TRAIN", "Init_epoch"))
#     __C.TRAIN.Freeze_epoch           = int(configParser.get("TRAIN", "Freeze_epoch"))
#     __C.TRAIN.epoch                  = int(configParser.get("TRAIN", "epoch"))
#     __C.TRAIN.batch_size             = int(configParser.get("TRAIN", "batch_size"))
#     __C.TRAIN.learning_rate_base     = float(configParser.get("TRAIN", "learning_rate_base"))
#     __C.TRAIN.min_learn_rate         = float(configParser.get("TRAIN", "min_learn_rate"))
#     __C.TRAIN.freeze_layers          = int(configParser.get("TRAIN", "freeze_layers"))
#
#     __C.TRAIN.model_save_name         = configParser.get("TRAIN", "model_save_name")
#
#     return recipe

def load_ini_YOLOV4_new(configFilePath):
    #   讀入 設定檔(.ini) 並把參數丟入config中
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    sections = configParser.sections()
    #  指定節點的option
    options = configParser.options("RECIPE")

    recipe                          = edict()
    # Consumers can get config by: from config import cfg
    recipe.SQLAnnotation            = configParser.get("RECIPE","SQLAnnotation")
    recipe.Model                    = configParser.get("RECIPE","Model")

    recipe.AnnotationPath           = configParser.get("RECIPE","AnnotationPath")
    recipe.ClassesPath              = configParser.get("RECIPE","ClassesPath")
    recipe.AnchorsPath              = configParser.get("RECIPE","AnchorsPath")
    recipe.WeightsPath              = configParser.get("RECIPE","WeightsPath")
    recipe.BasicWeightsPath         = configParser.get("RECIPE","BasicWeightsPath")
    recipe.LogDir                   = configParser.get("RECIPE","LogDir")

    recipe.Kfold                    = int(configParser.get("RECIPE","Kfold"))
    recipe.InputSizeW               = int(configParser.get("RECIPE","InputSizeW"))
    recipe.InputSizeH               = int(configParser.get("RECIPE","InputSizeH"))

    recipe.LabelSmoothing           = int(configParser.get("RECIPE","LabelSmoothing"))
    recipe.Normalize                = int(configParser.get("RECIPE","Normalize"))
    recipe.ModelSummary             = int(configParser.get("RECIPE","ModelSummary"))
    recipe.Mosaic                   = int(configParser.get("RECIPE","Mosaic"))
    recipe.ValSplit                 = float(configParser.get("RECIPE","ValSplit"))
    recipe.InitEpoch                = int(configParser.get("RECIPE","InitEpoch"))
    recipe.FreezeEpoch                = int(configParser.get("RECIPE","FreezeEpoch"))
    recipe.Epoch                    = int(configParser.get("RECIPE","epoch"))
    recipe.BatchSize                = int(configParser.get("RECIPE","BatchSize"))
    recipe.LearningRateBase         = (configParser.get("RECIPE","LearningRateBase"))
    recipe.MinLearnRate             = (configParser.get("RECIPE","MinLearnRate"))
    recipe.FreezeLayers             = int(configParser.get("RECIPE","FreezeLayers"))

    recipe.ModelSaveName            = configParser.get("RECIPE","ModelSaveName")
    recipe.VerifiedDataStart        = configParser.get("RECIPE","VerifiedDataStart")
    recipe.VerifiedDataEnd          = configParser.get("RECIPE","VerifiedDataEnd")

    return recipe





if __name__ == "__main__":
    import json

    recipe = {
        'SQLAnnotation': "False",
        'Kfold': 1,
        'AnnotationPath': r'C:\Users\spawnboo\PycharmProjects\new_ML_Flask_Server\ML_Flask_Server\DL_Train\model_date\2007_train.txt',
        'ClassesPath': 'model_date/KN_defectCode20220927.txt',
        'AnchorsPath': 'model_date/yolo_anchors.txt',
        # 'WeightsPath': r'D:\ML\ML_Flask_Server\ML_Flask_Server\logs\Kfold-1\ep010-loss16.130-val_loss24.524.h5',  #'D:\DL_Model\Yolo\All_Defect_model 7\weightsOnlyAll_Defect_model 7.h5',
        'WeightsPath': r"D:\ML\ML_Flask_Server\ML_Flask_Server\logs\Kfold0All_Defect_model8.h5",
        'BasicWeightsPath': 'model_date/yolo4_weight.h5',
        'LogDir': '../logs',
        'InputSizeW': 608,
        'InputSizeH': 608,
        'LabelSmoothing': 1,
        'Normalize': 0,
        'ModelSummary': 1,
        'Mosaic': 0,
        'ValSplit': 0.2,

        'InitEpoch': 0,
        'FreezeEpoch': 0,
        'Epoch': 100,
        'BatchSize': 2,
        'LearningRateBase': 1e-5,
        'MinLearnRate': 1e-6,
        'FreezeLayers': 249,
        'ModelSaveName': 'All_Defect_model8_2',
        'VerifiedDataStart': '',
        'VerifiedDataEnd': ''
    }

    configFilePath = r'.\Recipe_new.ini'

    a = load_ini_YOLOV4_new(configFilePath)
    print (recipe)
    print(a)
    print (a['SQLAnnotation'] == recipe['SQLAnnotation'])