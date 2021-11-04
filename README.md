# Python 実践データ分析100本ノック

---
# Web からの注文数を分析する

## Data の読み込み

分析業務の目的にも寄るが

- 抽象的なお題
- 具体的なお題

どちらででも、まず**Data の全体像を把握**することが大事。

全 Data の先頭５行を表示させることで、どのような Data が存在するのか、それぞれの Data 列の関係性など、 Data の大枠を掴むことができる。 複数に渡って存在する Data をかき集め、Data の概要を捉え**
分析に適した形に加工**することから始める。

## Data の結合( Union )

**Union を行う Method**

```python
import pandas as pd

pd.concat([data_frame_1, data_frame_2], ignore_index=True)
```

### Union

Data 数を行方向に増やす（縦に結合する）こと。

## Data 同士の結合（Join）

**主軸になる Data** を考えつつ、どの列を Key に Join するか考えていく。

ex). 主軸になる Data : 最も粒度が細かい Data

1. 足りない（付加したい）Data 列は何か？
2. 共通する Data 列は何か？

※ 結合する Data 間で片方により粒度が細かい Data 等がある場合は付加してしまうと二重計上になってしまうので注意する。

**Join を行う Method**

```python
import pandas as pd

pd.merge(main_data_frame, data_frame[['data_col', 'data_2', '･･･', ]], on='Join_key', how='join_method')
```

# Data 結合と正規化

## Data 結合

複数の Data を１つの Data にまとめて処理することで、処理の時間短縮や可読性の向上を図る。  
Data の整合性を担保する為に Data が分かれていて１つの Data では必要な情報が揃わないものを結合する。

## Data の正規化

**Data の整合性**を担保する設計思想。

### Data の冗長性

同じ Data が繰り返し重複して保持されていたりして、同じ Data の更新を行う際に何度も処理を行わないといけない状態の Data

## Data 結合の種類

### Inner join

２つの Data で共通の Data のみを抽出したい場合。

**注意点**  
正しく結合条件を設定しないと、Data の欠落が起こる。  
<small>ex). 売上 Data と商品 Master を Inner join 。商品 Master に未登録商品があった場合に売上 Data かその売上が除外され集計に影響がでる。</small>

### Outer join

- ２つのどちらか片方にでも Data が存在すれば対象とる。
- 単純に Data を結合した場合の結合方法。

**注意点**

- Data①にしか Data がない行の Data②にはすべて NULL が代入される。
- Record 件数が不用意に増える

### Left(Right) join

どちら片方の Data を主としたい場合に有効な結合方法

- Left join: 結合される側の Data がすべて使われる。
- Right join: 結合する側の Data がすべて使われる。

**注意点**
主軸にする Data 側に Data が存在しない場合、抽出 Data に NULL が入るので欠損地の確認や補完が必要になる。

## 結合の注意

kb結合 Data に重複などが存在する場合、Data が増えてしまう Case があり集計に影響する。

## Data 加工

一歩間違えると集計 Miss が起き、数字のズレを生む。間違った Data を提供することは

- 会社の経営に大きな影響を及ぼし、最悪の場合、会社が傾く。
- Data で語る Data Scientist が誤った Data を出す、というのは信頼を失う。

Data の結合など加工を行う度に「**件数の確認を心がけ**」て「**検算を実行**」する。

## 各種統計量の把握

Data 分析を進めていく上で、まず大きく２つの数字を知る必要がある。

1. 欠損している値の状況
2. 全体の数時感

### 欠損値
- 多くの Data に含まれる可能性がある。
- 集計や機械学習に大きく影響する

よって、除去や補間をする必要がでてくる。

**欠損値の確認ができる Method**
```python
import pandas as pd

# 欠損値を True / False で返す
data_frame.isnull()

# True の数をそれぞれの列毎に計算する
data_frame.isnull().sum()
```

### 全体の数時感
一般的に Data 分析では、商品毎、顧客属性など、様々な切り口で集計を行っていく。
ある値が 10万 だと分かっても、分母の規模が10億なのか100万なのかによって意味が大きく変わってくるので全体の数時感を掴むのが重要になってくる。

**全体感を把握するための Method**
```python
import pandas as pd

# 各種統計量を出力
data_frame.describe()
```

### 集計
全体の数字感が把握できたら、時系列で状況を確認してみる。その際に、半年程度の Data であれば影響がでることはないが過去数年間の Data 等を扱う場合
など一纏めに分析するとビジネスモデルの変化等により見誤る Case があるので、Data 範囲を絞る Case もある。

**集計で利用できる Methods**
```python
import pandas as pd

data_frame.groupby('column').sum()['display_column']
data_frame.groupby(['column_1', 'column_2']).sum()[['display_column_1', 'display_column_2']]
```
groupby
- まとめたい列
- 集計方法
- 表示させる列
 
を指定する。  
まとめたい列が複数ある場合、List 型で指定する。

```python
import pandas as pd

pd.pivot_table(data_frame, index='column', columns='column', values=['column_1', 'column_2'], aggfunc='集計方法')

```
pivot_table
- 行と列を指定することができる。
- index: 行
- columns: 列
- values: 集計したい数字列
- aggfunc: 集計方法

### Data の可視化
表形式の Data は、細かい数字が把握できるが Data の推移が一目ではわからない。
分析のゴールは  
「**現場で適切に運用され施策をまわしていくこと**」  
現場では、数字が苦手な人もいるので伝え方も重要になる。

**Data の可視化で利用できる Methods**
```python
import matplotlib.pyplot as plt

plt.plot('list', 'list', label='string')
```
matplotlib の Graph 描画は、  
1. 横軸
2. 縦軸

順番で指定する。  
<small>※ label を表記することで凡例に表示することができる。</small>

## Data の揺れ
Data 等で顕在する入力 Miss や表記方法の違い等が混在し、不整合を起こしている状態。

- 人間は Data の揺れを補完して Data を理解するが System は理解できない。
- Data が揺れたまま分析しても結果の信憑性や信頼性は担保できない。

Data の揺れが残ったまま集計・分析しても、**全く意味のない結果**となる。


### Data の揺れの解消・整合方法
Data の揺れを解消し、整合性を担保する事が Data 分析を行うのに基礎となるべき重要なこと。Data 加工が分析の前処理として重要になる。
Data のもつ属性や意味を理解する。Data の揺れを把握することから始める。
