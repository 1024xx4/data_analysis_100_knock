# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] pycharm={"name": "#%% md\n"}
# # 9章 潜在顧客を把握するための画像認識
#
# ここでは、カメラから取得した映像を用いて画像認識を行い、
# 必要な情報を取得するための流れを学ぶことで、
# 画像認識をビジネス現場で応用するイメージをつかみます。

# %% pycharm={"name": "#%%\n", "is_executing": true}
import cv2
img = cv2.imread('sample_code/chapter_9/img/img01.jpg')
height, width = img.shape[:2]
print(f'画像幅: {str(width)}')
print(f'画像高さ: {str(height)}')
cv2.imshow("img",img)
cv2.waitKey(0)
