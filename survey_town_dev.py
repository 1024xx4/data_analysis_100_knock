# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] pycharm={"name": "#%% md\n"}
# # 前提条件
#
# | 項目   | 内容                           |
# |------|------------------------------|
# | 概要   | 顧客満足度アンケートの Data             |
# | 対象期間 | 2019年１月 ~ ４月                 |
# | 保存方法 | Database                     |
# | 目的   | 顧客満足度の向上                     |
# | 変数   | アンケートの取得日, Comment, 満足度（５段階） |

# %% pycharm={"name": "#%%\n"}
import pandas as pd

survey = pd.read_csv('sample_code/chapter_10/survey.csv')
print(len(survey))
survey.head()

# %% pycharm={"name": "#%%\n"}
survey.isna().sum()
