# import win32api
# import win32con
# import pywintypes
# devmode = pywintypes.DEVMODEType()
#
# # screenSize = [1280,800]
# screenSize = [1920,1080]
#
# devmode.PelsWidth = screenSize[0]
# devmode.PelsHeight = screenSize[1]
# devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
# win32api.ChangeDisplaySettings(devmode,0)


import win32api
dm = win32api.EnumDisplaySettings(None, 0)
dm.PelsHeight = 1080
dm.PelsWidth = 1920
dm.BitsPerPel = 32
dm.DisplayFixedOutput = 0
win32api.ChangeDisplaySettings(dm, 0)




# # -*- coding: utf-8 -*-
# """
# 功能：识别两块显示器各自的分辨率
# """
# """模块导入"""
# from win32api import GetSystemMetrics
# from win32con import SM_CMONITORS, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN
#
# def Display_Detection():
#     # 显示器数量检测
#     MonitorNumber = GetSystemMetrics(SM_CMONITORS)
#     # 主屏幕尺寸检测
#     MajorScreenWidth = GetSystemMetrics(0)  # 主屏幕宽
#     MajorScreenHeight = GetSystemMetrics(1)  # 主屏幕高
#     # print("主屏幕尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
#     # 屏幕最大尺寸
#     aScreenWidth = GetSystemMetrics(SM_CXVIRTUALSCREEN)  # 屏幕最大宽度
#     aScreenHeight = GetSystemMetrics(SM_CYVIRTUALSCREEN)  # 屏幕最大高度
#     AllScreen=(aScreenWidth, aScreenHeight)
#     # print("屏幕总尺寸:", aScreenWidth, "*", aScreenHeight)
#     # 当前主流的分辨率基数是宽，偶数是高
#     ResolvingPower = [1280, 720, 1920, 1080, 2560, 1440, 3840, 2160, 4096, 2160, 7680, 4320]
#
#     if MonitorNumber > 1:  # 屏幕数量判断print(MonitorNumber)就可以知道有多少块屏幕
#         SecondaryScreenWidth = aScreenWidth - MajorScreenWidth  # 副屏宽=总屏幕宽-当前屏幕宽
#         # print("副屏宽",SecondaryScreenWidth)
#
#         # 主屏横竖屏检测
#         if GetSystemMetrics(0) > GetSystemMetrics(1):
#             MianScreen = (GetSystemMetrics(0), GetSystemMetrics(1))
#             # print("主屏(横屏)尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
#         else:
#             MianScreen = (GetSystemMetrics(0), GetSystemMetrics(1))
#             # print("主屏(竖屏)尺寸：", GetSystemMetrics(0), "*", GetSystemMetrics(1))
#
#         # 横屏状态
#         for i in range(0, len(ResolvingPower) - 1, 2):
#             # print("i",ResolvingPower[i])
#             if SecondaryScreenWidth == ResolvingPower[i]:
#                 SecondaryScreen = (ResolvingPower[i], ResolvingPower[i + 1])
#                 # print("副屏(横屏)尺寸：", ResolvingPower[i], ResolvingPower[i + 1])
#                 # return "副屏(竖屏)尺寸：",SecondaryScreen
#                 break
#         # 竖屏状态
#         for i in range(1, len(ResolvingPower) - 1, 2):
#             # print("i",ResolvingPower[i])
#             if SecondaryScreenWidth == ResolvingPower[i]:
#                 SecondaryScreen = (ResolvingPower[i], ResolvingPower[i + 1])
#                 # print("副屏(竖屏)尺寸：", ResolvingPower[i], ResolvingPower[i - 1])
#                 # return "副屏(竖屏)尺寸",SecondaryScreen
#                 break
#     return MonitorNumber,AllScreen,MianScreen,SecondaryScreen
#
# #调用
# a=Display_Detection()
# print(a)#a可以任意遍历其中的内容a[0]代表屏幕数量等等...

#(2, (4480, 1440), (2560, 1440), (1920, 1080))#运行结果：屏幕数量、总屏幕尺寸、主屏幕尺寸、副屏尺寸
