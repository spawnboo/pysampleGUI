# coding=utf-8
"""
    用以讀取Recipe.ini 的txt檔案

    *   節點名稱需依樣
"""
import configparser
from easydict import EasyDict as edict



def load_ini_YOLOV4(configFilePath):
    #   讀入 設定檔(.ini) 並把參數丟入config中
    configParser = configparser.RawConfigParser()
    configParser.read(configFilePath)
    #   顯示所有節點[sections]
    sections = configParser.sections()
    #   指定節點的option
    options = configParser.options("PATH")
    #   指定節點的對應值
    cnn   = configParser.items("PATH")

    __C                             = edict()
    # Consumers can get config by: from config import cfg
    recipe                          = __C


    # [PATH]
    __C.PATH                        = edict()

    __C.PATH.annotation_path        = configParser.get("PATH", "annotation_path")
    __C.PATH.verified_data_start    = configParser.get("PATH", "verified_data_start")
    __C.PATH.verified_data_end      = configParser.get("PATH", "verified_data_end")
    __C.PATH.classes_path           = configParser.get("PATH", "classes_path")
    __C.PATH.anchors_path           = configParser.get("PATH", "anchors_path")
    __C.PATH.weights_path           = configParser.get("PATH", "weights_path")
    __C.PATH.basic_weights_path     = configParser.get("PATH", "basic_weights_path")
    __C.PATH.log_dir                = configParser.get("PATH", "log_dir")

    # [TRAIN]
    __C.TRAIN = edict()

    __C.TRAIN.input_shape            = (int(configParser.get("TRAIN", "input_shape_W")), int(configParser.get("TRAIN", "input_shape_H")))
    __C.TRAIN.label_smoothing        = int(configParser.get("TRAIN", "label_smoothing"))
    __C.TRAIN.normalize              = int(configParser.get("TRAIN", "label_smoothing"))
    __C.TRAIN.Modelsummary           = int(configParser.get("TRAIN", "Modelsummary"))
    __C.TRAIN.mosaic                 = int(configParser.get("TRAIN", "mosaic"))

    __C.TRAIN.val_split              = float(configParser.get("TRAIN", "val_split"))
    __C.TRAIN.Init_epoch             = int(configParser.get("TRAIN", "Init_epoch"))
    __C.TRAIN.Freeze_epoch           = int(configParser.get("TRAIN", "Freeze_epoch"))
    __C.TRAIN.epoch                  = int(configParser.get("TRAIN", "epoch"))
    __C.TRAIN.batch_size             = int(configParser.get("TRAIN", "batch_size"))
    __C.TRAIN.learning_rate_base     = float(configParser.get("TRAIN", "learning_rate_base"))
    __C.TRAIN.min_learn_rate         = float(configParser.get("TRAIN", "min_learn_rate"))
    __C.TRAIN.freeze_layers          = int(configParser.get("TRAIN", "freeze_layers"))

    __C.TRAIN.model_save_name         = configParser.get("TRAIN", "model_save_name")

    return recipe

if __name__ == "__main__":
    configFilePath = r'.\Recipe.ini'

    a = load_ini_YOLOV4(configFilePath)

    print(a.PATH.annotation_path)