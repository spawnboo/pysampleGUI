# coding=utf-8
import os
import sys
import PySimpleGUI as sg

import Function

# 綠底介面
sg.theme('GreenTan')
#============================================== Tab 多個分頁  ====================================================
# 基礎設定
Tab_basic_layout = [
    [sg.T("影像檔案位置", size=(15,1), justification='l'),sg.In(key='-IMAGE_PATH-', size=(50,1), default_text = ".\DataSet\Images"), sg.FolderBrowse()],
    [sg.T("資料集清單", size=(15,1), justification='l'),sg.In(key='-ANNOTATION_FILE-', size=(50,1), default_text = ".\DataSet\Annotation"), sg.FileBrowse()],
    [sg.T("類別清單", size=(15,1), justification='l'),sg.In(key='-CLASSES_FILE-', size=(50,1), default_text = ".\DataSet\Classes"), sg.FileBrowse()],
    [sg.T("錨點清單", size=(15,1), justification='l'),sg.In(key='-ANCHORS_FILE-', size=(50,1), default_text = ".\DataSet\Anchors\yolo_anchors.txt"), sg.FileBrowse()],
    [sg.T("預載權重(.h5)", size=(15,1), justification='l'),sg.In(key='-WEIGHT_FILE-', size=(50,1)), sg.FileBrowse()],
    [sg.T("預訓練權重(.h5)", size=(15,1), justification='l'),sg.In(key='-BASIC_WEIGHT_FILE-', size=(50,1)), sg.FileBrowse()],
    [sg.T("LOG PATH", size=(15,1), justification='l'),sg.In(key='-LOG_PATH-', size=(50,1), default_text = ".\LOG"), sg.FolderBrowse()],
    ]
# 進階參數設定classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus",
#         "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
#         "motorbike", "person", "pottedplant", "sheep", "sofa", "train",
#         "tvmonitor"]
Tab_paramater_layout = [
    [sg.T("Model", size=(15,1), justification='l'),sg.In(key='-MODEL-', size=(15, 1))],
    [sg.T("Input_Weight", size=(15,1), justification='l'),sg.In(key='-INPUT_WEIGHT-', size=(15, 1))],
    [sg.T("Input_Height", size=(15,1), justification='l'),sg.In(key='-INPUT_HEIGHT-', size=(15, 1))],
    [sg.T("Validation Split", size=(15,1), justification='l'),sg.In(key='-VAL_SPLIT-', size=(15, 1))],
    [sg.T("Label Smoothing", size=(15,1), justification='l'),sg.In(key='-LABEL_SMOOTHING-', size=(15, 1))],
    [sg.T("Normalize", size=(15,1), justification='l'),sg.In(key='-NORMALIZE-', size=(15, 1))],
    [sg.T("Model Summary", size=(15,1), justification='l'),sg.In(key='-MODEL_SUMMARY-', size=(15, 1))],
    [sg.T("Mosaic", size=(15,1), justification='l'),sg.In(key='-MOSAIC-', size=(15, 1))],
    [sg.T("-----------------------------------------------------------", size=(15,1), justification='c')],
    [sg.T("Init Epoch", size=(15,1), justification='l'),sg.In(key='-INIT_EPOCH-', size=(15, 1))],
    [sg.T("Freeze Epoch", size=(15,1), justification='l'),sg.In(key='-FREEZE_EPOCH-', size=(15, 1))],
    [sg.T("Epoch", size=(15, 1), justification='l'), sg.In(key='-EPOCH-', size=(15, 1))],
    [sg.T("Batch", size=(15, 1), justification='l'), sg.In(key='-BATCH-', size=(15, 1))],
    [sg.T("-----------------------------------------------------------", size=(15,1), justification='c')],
    [sg.T("LearningRate Base", size=(15, 1), justification='l'), sg.In(key='-LR_BASE-', size=(15, 1))],
    [sg.T("Min LearnRate", size=(15, 1), justification='l'), sg.In(key='-LR_MIN-', size=(15, 1))],
    [sg.T("Freeze Layers", size=(15, 1), justification='l'), sg.In(key='-FREEZE_LAYER-', size=(15, 1))],
    [sg.T("ModelSaveName", size=(15, 1), justification='l'), sg.In(key='-MODEL_SAVE_NAME-', size=(15, 1))],
    ]
# 資料擴增 Augmentation
Tab_Augmentation_layout = [
    [sg.T("放大縮小"),]
    ]

# Recipe Group
tab_group_layout = [[
                     sg.Tab('基本設定', Tab_basic_layout, key='-BASIC_TIP-'),
                     sg.Tab('參數設定', Tab_paramater_layout, key='-PARAMATER_TIP-'),
                     sg.Tab('設定', Tab_Augmentation_layout, key='-AUGMANTATION_TIP-'),
                    ]]
#==============================================  Recipe ListBox  ================================================
# ToDo  指定特定Recipe位置, 加入所有.ini Recipe檔案
# [Recipe.ini]

RecipePath = r".\RecipeFunction"
RecipeList = Function.GetRecipeList(RecipePath)

Recipe_ListBox = [sg.LBox(RecipeList,size=(20,20), key='-RECIPE_LISTBOX-', enable_events=True)]

# show ConsoleBox
console_ListBox = [sg.LBox([],size=(200,20), key='-Console_ListBox-')]

#==============================================  Text Status   ==================================================
Status_Layout = [sg.Text("adadasdadada", key= '-Status_Text-'),sg.In(key='Model')]

#==============================================  Layout  ========================================================
layout = [
    [
        sg.Frame('Recipe', layout=[[

        sg.Column([Recipe_ListBox], vertical_alignment='top'),
        sg.Column([[sg.TabGroup(tab_group_layout, enable_events=True, key='-RECIPE_TABGROUP-')]], vertical_alignment='top')

        ]])
    ],
    [
        sg.Button("Start Train", key='-STARTTRAIN_BTN-', disabled=True)
    ],
    [
        sg.Column([console_ListBox], vertical_alignment='top'),
    ]
          ]


#==============================================  Output Windows  ================================================

window = sg.Window('Deep Learning By Croc', layout, default_element_size=(12, 1), finalize=True, size=(1000,700))


while True:
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED:  # 永遠不能刪除, 關閉時 關閉程式
        break

    # Recipe ListBox 被選擇 事件
    if event == '-RECIPE_LISTBOX-' and len(values['-RECIPE_LISTBOX-']):
        print (len(values['-RECIPE_LISTBOX-']))
        # 跳出是否載入該Recipe
        recipeYN = sg.popup_yes_no('Recipe Load? ')
        # 載入對應的Recipe
        if recipeYN == "Yes":
            # ToDo 未來這邊要檢查 Recipe 是否有缺失

            recipeRead = Function.LoadRecipe(os.path.join(RecipePath,values['-RECIPE_LISTBOX-'][0]+'.ini'))
            # basic
            window['-ANNOTATION_FILE-'].update(recipeRead['AnnotationPath'])
            window['-CLASSES_FILE-'].update(recipeRead['ClassesPath'])
            window['-ANCHORS_FILE-'].update(recipeRead['AnchorsPath'])
            window['-WEIGHT_FILE-'].update(recipeRead['WeightsPath'])
            window['-BASIC_WEIGHT_FILE-'].update(recipeRead['BasicWeightsPath'])
            window['-LOG_PATH-'].update(recipeRead['LogDir'])
            # PARAMATER
            window['-MODEL-'].update(recipeRead['Model'])
            window['-INPUT_WEIGHT-'].update(recipeRead['InputSizeW'])
            window['-INPUT_HEIGHT-'].update(recipeRead['InputSizeH'])
            window['-VAL_SPLIT-'].update(recipeRead['ValSplit'])
            window['-LABEL_SMOOTHING-'].update(recipeRead['LabelSmoothing'])
            window['-NORMALIZE-'].update(recipeRead['Normalize'])
            window['-MODEL_SUMMARY-'].update(recipeRead['ModelSummary'])
            window['-MOSAIC-'].update(recipeRead['Mosaic'])
            window['-INIT_EPOCH-'].update(recipeRead['InitEpoch'])
            window['-FREEZE_EPOCH-'].update(recipeRead['FreezeEpoch'])
            window['-EPOCH-'].update(recipeRead['Epoch'])
            window['-BATCH-'].update(recipeRead['BatchSize'])
            window['-LR_BASE-'].update(recipeRead['LearningRateBase'])
            window['-LR_MIN-'].update(recipeRead['MinLearnRate'])
            window['-FREEZE_LAYER-'].update(recipeRead['FreezeLayers'])
            window['-MODEL_SAVE_NAME-'].update(recipeRead['ModelSaveName'])






window.close()