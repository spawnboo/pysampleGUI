# coding=utf-8
import PySimpleGUI as sg

import Function

# 綠底介面
sg.theme('GreenTan')
#============================================== Tab 多個分頁  ====================================================
# 基礎設定
Tab_basic_layout = [
    [sg.T("影像檔案位置"),sg.In(key='ImagePath'), sg.FolderBrowse()],
    [sg.T("Epoch"),sg.In(key='Epoch')],
    [sg.T("Batch"),sg.In(key='Batch')],
    ]
# 進階參數設定
Tab_paramater_layout = [
    [sg.T("Model"),sg.In(key='Model')],
    [sg.T("Input_Weight"),sg.In(key='Input_Weight')],
    [sg.T("Input_Height"),sg.In(key='Input_Height')]
    ]
# 資料擴增 Augmentation
Tab_Augmentation_layout = [
    [sg.T("放大縮小"),]
    ]

# Recipe Group
tab_group_layout = [[
                     sg.Tab('基本設定', Tab_basic_layout, key='-Basic_tip-'),
                     sg.Tab('參數設定', Tab_paramater_layout, key='-Paramater_tip-'),
                     sg.Tab('設定', Tab_Augmentation_layout, key='-Augmentation_tip-'),
                    ]]
#==============================================  Recipe ListBox  ================================================
# ToDo  指定特定Recipe位置, 加入所有.ini Recipe檔案
# [Recipe.ini]
RecipePath = r"D:\PycharmProjects\new_ML_Flask_Server\ML_Flask_Server\DL_Train\RecipeConfig"
RecipeList = Function.GetRecipeList(RecipePath)

Recipe_ListBox = [sg.LBox(RecipeList,size=(50,20), key='-Recipe_ListBox-', enable_events=True)]



#==============================================  Layout  ========================================================
layout = [
    [
        sg.Frame('Recipe', layout=[[

        sg.Column([Recipe_ListBox], vertical_alignment='top'),
        sg.Column([[sg.TabGroup(tab_group_layout, enable_events=True, key='-RECIPE_TABGROUP-')]], vertical_alignment='top')

        ]])
    ],
    [
        sg.Button("Start Train", key='_StratTrainBtn_', disabled=True)
    ]
          ]


#==============================================  Output Windows  ================================================

window = sg.Window('Deep Learning By Croc', layout, default_element_size=(12, 1), finalize=True, size=(800,600))


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:  # 永遠不能刪除, 關閉時 關閉程式
        break
    
    # Recipe ListBox 被選擇 事件
    if event == '-Recipe_ListBox-' and len(values['-Recipe_ListBox-']):
        sg.popup('Selected ', values['-Recipe_ListBox-'])


window.close()