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
    [sg.T("影像檔案位置"),sg.In(key='ImagePath', size=(20,500)), sg.FolderBrowse()],
    [sg.T("Epoch"),sg.In(key='-EPOCH-')],
    [sg.T("Batch"),sg.In(key='-BATCH-')],
    ]
# 進階參數設定
Tab_paramater_layout = [
    [sg.T("Model"),sg.In(key='-MODEL-')],
    [sg.T("Input_Weight"),sg.In(key='-INPUT_WEIGHT-')],
    [sg.T("Input_Height"),sg.In(key='-INPUT_HEIGHT-')]
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

Recipe_ListBox = [sg.LBox(RecipeList,size=(20,20), key='-Recipe_ListBox-', enable_events=True)]

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
    if event == '-Recipe_ListBox-' and len(values['-Recipe_ListBox-']):
        print (os.path.join(RecipePath,values['-Recipe_ListBox-'][0]))
        # 跳出是否載入該Recipe
        recipeYN = sg.popup_yes_no('Recipe Load? ')
        # 載入對應的Recipe
        if recipeYN == "Yes":
            recipeRead = Function.LoadRecipe(os.path.join(RecipePath,values['-Recipe_ListBox-'][0]+'.ini'))
            # basic
            window['-EPOCH-'].update(recipeRead['TRAIN']['epoch'])
            window['-BATCH-'].update(recipeRead['TRAIN']['batch_size'])
            # PARAMATER
            window['-INPUT_WEIGHT-'].update(recipeRead['TRAIN']['input_shape'][0])
            window['-INPUT_HEIGHT-'].update(recipeRead['TRAIN']['input_shape'][1])
            window['-MODEL-'].update(recipeRead['TRAIN']['model'])



window.close()