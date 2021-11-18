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

pd.merge(main_data_frame, data_frame[['data_col', 'data_2']], on='Join_key', how='join_method')
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

一般的に Data 分析では、商品毎、顧客属性など、様々な切り口で集計を行っていく。 ある値が 10万 だと分かっても、分母の規模が10億なのか100万なのかによって意味が大きく変わってくるので全体の数時感を掴むのが重要になってくる。

**全体感を把握するための Method**

```python
import pandas as pd

# 各種統計量を出力
data_frame.describe()
```

- count(Data 件数)
- mean(平均値)
- std(標準偏差)
- 最小値(min)
- 四分位数(25% 75%)
- 中央値(50%)

最大値を簡単に出力できる。

### 集計

全体の数字感が把握できたら、時系列で状況を確認してみる。その際に、半年程度の Data であれば影響がでることはないが過去数年間の Data 等を扱う場合 など一纏めに分析するとビジネスモデルの変化等により見誤る Case
があるので、Data 範囲を絞る Case もある。

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

pd.pivot_table(data_frame, index='column', columns='column', values=['column_1', 'column_2'],
               aggfunc='aggregation methods')

```

pivot_table

- 行と列を指定することができる。
- index: 行
- columns: 列
- values: 集計したい数字列
- aggfunc: 集計方法

### Data の可視化

表形式の Data は、細かい数字が把握できるが Data の推移が一目ではわからない。 分析のゴールは  
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

Data の揺れを解消し、整合性を担保する事が Data 分析を行うのに基礎となるべき重要なこと。Data 加工が分析の前処理として重要になる。 Data のもつ属性や意味を理解する。Data の揺れを把握することから始める。

### 名前項目の Data の揺れ

- 全角・半角 Space 有無の混在
- 誤変換

など複雑な揺れが存在することが多い。

単純な Program で補正することができないことが多い為

- 現場の運用 Staff 等からの Hearing.
- 同姓同名の Data が存在する場合、登録日や生年月日等、他情報を用いての区別

など地道な名寄せ作業を行う必要がある。

### Excel 日付 Data と Python 日付 Data のズレ

２日ずれる。

**原因**

Excel | Python
--- | ---
最小日付は1900/01/01だが、Serial 値は「１」 | 1900/01/01 は当日のため、Serial 値は「０」と認識する
本来うるう年ではない「1900/02/29」を有効な日付として Serial 値に加算している | 本来うるう年ではない「1900/02/29」は無効の日付として、１日と Count しない。

言語や環境、App の仕様などにより同じ Data をそのまま扱えない Case も存在するので注意が必要。

### Cleansing(クレジンジグ)

Data の加工により、分析に適した Data のかたちにすること。

### Data を Dump する理由

Data 分析の際に Cleansing している Program からそのまま Data を利用すると何かしらの理由で Program を中断した際に全てをやり直す必要がでてしまう。 その為、Cleansing した Data は
Dump(出力)して、分析の際は、Dump した File から読み込み分析を行うと良い。  
※ 元の Data に変更があった場合は、再度 Data 加工処理を行い直す必要はある。

### Join 後は、欠損値の確認を

Join する際に、Key が見つからないなど、うまく Join できないと欠損値が自動で入る。  
Join 後は、欠損値の確認をするようにする。

## まとめ

- Data の状態を見極め、どのように加工するか現場 Staff と連携をとりながら進める。
- Data の Cleansing を疎かにすると後で痛い目にあう。

# 機械学習

Data 数が急激に増加している昨今、Computer の力を借りながら対話的に分析を進めてい手段。  
Computer に Data を学習させ特徴を導き出し、さらにその特徴を用いて未来への予測・判断などに活用する。

- 機械学習による分析
- 将来予測に関する技術

これらを現場で適切に活用していくことができれば、現場で「結果を出す」ことができる。

機械学習は、Data をもとに Computer が推論を行う。そのため、どのような Data で学習させるか、という部分がとても重要になる。  
人間もできる限り Data を理解し、特徴となりそうな変数を掴んでおくのが重要になる。

機械学習は、Data を必要とし、統計学が基礎にある。しかし、

機械学習 | 未来の予測が主軸
--- | ---
統計学 | 現象を説明する目的に使用することが多い

Data 数が急激に増加している昨今、機械(Computer)の力を借りながら対話的に分析を進めていく手段である機械学習は必須 Skill になりつつある。

## Data 分析の醍醐味

- 現在の Data から未来の予測が可能になること。
- 現状を分析することで問題点を把握し、より良い未来に変える最適な施策を実施できるようになること。

# 機械学習による予測

## Data 分析を駆使することで可能になること

- 可視化
- 相関関係を掴む
- **ある出来事の原因を半自動的に特定**  
  => Business を現場の勘や経験に頼ることのない Data を用いた Elegant で最適な意思決定に繋がる。

## Categorical 変数
Campaign 区分、会員区分、性別、などの文字列の Category 関連の Data のこと。  
機械学習ををやる上で重要な変数となってくる。活用するためには、 Flag 化する。

### Dummy 変数化
Categorical 変数を機械学習で活用できるように Flag 化すること。  
**利用できる Method**  
```python
import pandas as pd

pd.get_dummies(data_frame)

# 一括で Dummy変数化が可能。
# Cleaning が必要。
# 例). 男性と女性を表現しようと思った時に片方が 1 であれば 0 が残った性別、
# となるのでもう片方の変数は必要ない。
```




## 機械学習の大分類

- 教師あり学習
- 教師なし学習
- 強化学習

の３つに大きく分けられ、それぞれの学習方法ごとに、複数の Algorithm が存在する。

## 教師あり学習

既に正解の分かっている Data(教師 Data)を Computer に学習させる方法

- 分類
- 回帰

がある。

### 分類と回帰の違い

答えのかたちにある。

教師あり学習 | 答え | 線の引き方 | Algorithm
--- | --- | --- | ---
分類 | 離散値(ex. 退会する/しない) | 綺麗に分割できる線を引く | 決定木、Logistic 回帰、Random forest, etc...
回帰 | 連続値(ex. 利用回数) | 綺麗に説明できる線を引く | 重回帰、etc...

どちらも学習させるということは、線を引くことに当たり、線を学習により引いておくことで未知な Data が来た時に、**予測**が可能になる。

### 説明変数

予測に使う変数のこと

### 目的変数

予測したい変数のこと

### 学習用 Data と評価用 Data に分割する理由

**過学習状態**を防ぐため。  
<small>※ **過学習状態**: 機械学習はあくまでも未知の Data を予測するのが目的なのに。学習に用いた Data に過剰適合してしまい未知な Data に対応できなくなる状態。</small>

### 教師あり学習の Algorithm

線を引くための Algorithm は数多く存在している 特に分類は、数が多く日進月歩で技術が向上している。 最近は、勾配 Boosting 法などがよく利用されてきているが、直観的に理解(説明)しやすい決定木などの Simple な
Algorithm も数多く活用されている。

### 決定木
Simple な手法ではあるが、わかりやすく原因の分析を行うことができることから Business の現場で頻繁に用いられる。   
最も綺麗に 0 と 1 を分割できる説明変数およびその条件を探す作業を、木構造状に派生させていく手法。分割していく木構造の深さを浅くすると Model を簡易化できる。

## 教師なし学習

教師 Data を学習させずに与えられた Data から規則性などの意味のある情報を見つけ出す手法。 代表的なものとして **Clustering** がある。  
教師 Data が用意できない場面で非常に効果的。**探索的な Data 解析**で多く使用されている。ただし、正解 Data がないため、 Model の精度が決められず、 その Group
の分類が正しいかの判断ができず、より人間の知見が重要になる。

### 次元削除

教師なし学習の一種。  
情報をなるべく失わないように変数を削減して、新しい軸を作り出す。これにより多次元の変数を２つの変数で表現し Graph 化が可能になる。  
※ 代表的な手法･･･ 主成分分析

### Clustering

ある集団を Grouping していくことができ、それぞれの Group の行動 Pattern を掴むことで、将来予測を精度よく行うことが可能になる。

使い方次第で数多くの可能性がある。行動 Pattern を予測して事前に施策を講じる、ということも可能になる。

Clustering方法名 | 内容
--- | ---
K-means法 | 最もオーソドックスなクラスタリング手法。 変数間の距離を Base に Group 化を行う。

## 強化学習

**一連の行動**に対して報酬などの環境情報を Computer に与えて、どのような行動が最も報酬が高くなるかを学習していく手法。 Computer 自身が１つの行動に対する評価を行う。

ex). AlphaGo などの囲碁や Chess の AI

### 教師あり学習との違い

機械学習 | 違い
--- | ---
教師あり学習 | １つの行動に対して、正解・不正解を与える
**強化学習** | 一連の行動に対する評価を行う

ex). Chess: 勝利という報酬を得るために最も効果的な行動を自己学習していく。

### 強化学習が有効な Case

行動が多岐に亘り、行動に対する正解がはっきりしない場合に有効。  
勝敗という明確な報酬を与えるだけで、最終的に勝利のための行動を学習させることができる。

### 強化学習の注意点

- 行動の組み合わせが膨大に存在する。
- 学習に時間がかかる。
- 人間では理解できない非合理的な行動を選択する Case がある。

## Model の精度と説明

精度の高い Model を構築しても、それがどのような Model なのか説明できないと相手が納得できずに導入が見送られることがある。  
精度が高いが Black box な Model より、精度が低くても説明可能な Model が使用されることが多々ある。
