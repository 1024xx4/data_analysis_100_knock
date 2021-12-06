# Python 実践データ分析100本ノック

---

## Data の分析

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

| Excel                                           | Python                                         |
|-------------------------------------------------|------------------------------------------------|
| 最小日付は1900/01/01だが、Serial 値は「１」                  | 1900/01/01 は当日のため、Serial 値は「０」と認識する            |
| 本来うるう年ではない「1900/02/29」を有効な日付として Serial 値に加算している | 本来うるう年ではない「1900/02/29」は無効の日付として、１日と Count しない。 |

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
Computer に Data を学習させ特徴を導き出し、さらにその特徴を用いて未来への・判断などに活用する。

- 機械学習による分析
- 将来予測に関する技術

これらを現場で適切に活用していくことができれば、現場で「結果を出す」ことができる。

機械学習は、Data をもとに Computer が推論を行う。そのため、どのような Data で学習させるか、という部分がとても重要になる。  
人間もできる限り Data を理解し、特徴となりそうな変数を掴んでおくのが重要になる。

機械学習は、Data を必要とし、統計学が基礎にある。しかし、

| 機械学習 | 未来の予測が主軸            |
|------|---------------------|
| 統計学  | 現象を説明する目的に使用することが多い |

Data 数が急激に増加している昨今、機械(Computer)の力を借りながら対話的に分析を進めていく手段である機械学習は必須 Skill になりつつある。

予測 Model を構築することは

- 迅速かつ自動的に未来を見つけ出す。
- 人間の感覚だけではなく、より Data Driven な判断を可能とさせる。

あくまでの最後の判断は人間が行っていくべきだが、予測 Model の予測結果を賢く活用していくことで、自社 Business を劇的に変える可能性を秘めている。

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

| 教師あり学習 | 答え                | 線の引き方        | Algorithm                             |
|--------|-------------------|--------------|---------------------------------------|
| 分類     | 離散値(ex. 退会する/しない) | 綺麗に分割できる線を引く | 決定木、Logistic 回帰、Random forest, etc... |
| 回帰     | 連続値(ex. 利用回数)     | 綺麗に説明できる線を引く | 重回帰、etc...                            |

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
**木構造の可視化**も行うことが可能で、直観的に Model を理解し説明しやすくできる。

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

| Clustering方法名 | 内容                                              |
|---------------|-------------------------------------------------|
| K-means法      | 最もオーソドックスなクラスタリング手法。 変数間の距離を Base に Group 化を行う。 |

## 強化学習

**一連の行動**に対して報酬などの環境情報を Computer に与えて、どのような行動が最も報酬が高くなるかを学習していく手法。 Computer 自身が１つの行動に対する評価を行う。

ex). AlphaGo などの囲碁や Chess の AI

### 教師あり学習との違い

| 機械学習     | 違い                   |
|----------|----------------------|
| 教師あり学習   | １つの行動に対して、正解・不正解を与える |
| **強化学習** | 一連の行動に対する評価を行う       |

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

# Data science の現場

実際の現場では綺麗な Data が用意されていることはほとんどなく、多くの Data 加工とブレ分析が待ち構えている。

1. Data の確認
2. Data の Cleaning
3. Data の分析
4. Data を活用した機械学習いよる未来予測

という一連の流れを理解する。

- 適切な Data を集め
- それらを読み込んだうえで、相関分析による原因分析
- 将来予測（Simulation）

などの技術を適切に活用して現場で「結果」を出していく。

# 最適化問題

定められた制約条件のもとで、目的関数を最小化（または最大化）する問題。  
最適化問題を解く Image は、変数の値やその組み合わせを変えていきながら、目的関数を最小（または最大）にする地点（最適解）を探すようなもの。

- 物流などの最適 Root を発見するための**最適化経路検索**
- 会社の経営の改善などにも応用できる、最適な Resource **配分の計算**
- **将来予測（Simulation）**

様々な状況において適用し「応用力」を身に着ける。

## 目的関数

最小化（または最大化）したいものを関数として定義すること

## 制約条件

最小化（または最大化）を行うにあたって守るべき条件を定義すること

考えられるあらゆる組み合わせの中から、**成約条件**を満たしたうえで**目的関数**を最小化（最大化）する組み合わせを選択する、というのが、 最適化問題の大きな流れ。

目的関数と制約条件さえ明確にできれば、最適化計算 Tool によって手計算よりも遥かに楽に解を求めることが可能。 最適化問題の中でも**線形最適化**に定型化できるものは比較的短時間に解を求めれることができるとわかっている。  
**※ 線形最適化  
ex). 輸送最適化問題など**

## 社会の中の最適化問題

- 「もっと効率よく作業をしたい」と感じるところすべてで用いられている Image.
- 人や機械が仕事や作業をしている場所であれば、至るところで見つかる。

### 鉄道

- 運行 Scheduling 問題（複雑な Pattern の中から適したダイヤを選ぶ。最適化問題の典型）
- 乗務員の Scheduling
- 乗り換え経路案内
- Multi-agent simulation（改札の待ち行列の解決）

### Office Building

- Demand response（空調の自動調整）
- Elevator の制御
- それぞれの Project に関する人員の Scheduling

### Convenience store

- Shift scheduling
- 顧客の動線を予測したうえで商品の陳列を最適化する問題
- Supply chain management（商品の配送最適化や在庫管理）
- POS system による需要予測

### 工場

- 最適制御、起動停止計画問題（Energy の供給や配分）
- 生産計画
- Scheduling

### 行政

- 避難計画や防災（Multi-agent simulation）
- 施設の配置などの都市計画
- Infra 整備計画

### Business の最適化問題

古くから研究されていることもあり、手法が確率されているということが大きな Merit。自分が解こうとしている問題についてどの手法に該当するか検討がつけ られれば、それぞれの問題の専門書や、先人の作った Source code
お使って比較的短時間で解くことが可能になる。

- Logistics network 設計問題  
  情報や倉庫などの拠点の配置や削減、生産 Line 能力、生産量、在庫量、輸送量などを決定する問題。
- 勤務 Scheduling 問題  
  乗務員や従業員、アルバイトなどの Scheduling を求める問題。
- 最小費用流問題  
  時刻ごとの需要を満たすように、船舶や車両を用いて、物資が余っているところから不足するところへ最小の輸送費用で配送を行う問題。
- 安全在庫問題  
  需要のばらつきに備えて、在庫費用と品切れ Risk の Balance をとる問題。
- Lot size 決定問題  
  製品をまとめて製造すると効率がよい場合に、在庫費用との Balance を考慮して、製造する製品の数を決定する問題。
- Packing 問題  
  Container などの入れ物に荷物を効率よく詰め込む問題。Layout を決める際などにも用いられる。
- 収益管理問題  
  時間経過により陳腐化する商品に対して、価格の操作を行うことで、収益の最大化を行う問題。

## 最適化問題のさまざまな解き方
初期値と微分値を見て、微分値が０であれば最適化したと考えれる。微分値が０のものが複数ある場合は、すべての値を比較して「最適」であるものを選択すればよい。
大きく３つの Pattern に分けられる。

### 線形最適化

行列演算の形式に落とし込めるもの。それぞれの要素が複雑に関係せず、要素間の「足し算」で表現できる。  
Simplex 法（制約条件の「端点」を追いかけていく方法）が用いられる。

### 非線形最適化

行列演算の形にはできない、関数の形で表現されるもの。個々の要素が複雑に絡み合う。  
Lagrange の未定乗数法（微分値が０になる点を求める方法）が用いられる。

### 組み合わせ最適化

アルバイトの Schedule のように要素と要素の組み合わせ Pattern のうちから最適なものを選択する。  
問題によっては「組み合わせ爆発」が生じ、すべての組み合わせ Pattern を計算することが原理的に不可能なものが多いため、Heuristic
（経験的に最適解が導き出されやすい方法）が問題ごとに考案されている。（問題の複雑さから、P、NP、NP完全、NP困難という４つの Class に分けられる。）  
計算が単純かつ、応用範囲も広い方法として、「動的計画法」（問題を小さな問題に分けながら、最適な組み合わせを徐々に探していく方法）というものもある。

## 実際の Business の現場で役立てるために

### Point

- 最適化 Program が導き出した答えが正しいかどうか
- その Plan を採用するかどうか

上記は、現場の意思決定者が納得できるかどうかにかかっている。そこで重要になるのが

- 最適化 Program によって導き出された Plan を可視化する Process
- 条件を実際に満たしていることを確認する Process

が現場では必要になる。

最適化計算の Library は、協力な Tool ではあるが鵜呑みにしない。何を調査し、確認すべきはかは、現場によって異なるが常に疑う姿勢を持って現場の
業務改善に臨む。

## Network 可視化

最適 Route を可視化する手法  
有用な Library としては**NetworkX**がある。

Network を可視化する際に Label などを表示したり、と効果的な見せ方を考え、その為に必要な機能を追加していくと良い可視化に近づける。

## Network 構造
| 種類            | 説明                                                        | 分布の傾向          |
|---------------|-----------------------------------------------------------|----------------|
| Small world 型 | わずかな Step で全員につながる                                        | 「べき分布」に近いものとなる |
| Scale free 型  | 少数のつながりを極めて多くもつ人が Hub になる。Link を持つ Hub が機能しないと途端に広がらなくなる。 | 「べき分布」に近いものとなる |

# 数値 Simulation
想像力を Support し、将来予測を行なうことで選択肢を広げていく手法。

最適化手法は強力だが、与えた条件のみから最適解を導きだす方法のため、条件に抜け、漏れがあると、現実離れした解を導き出すことがある。
そのため最適化計算によって導き出された解が現実的なものなのかどうかを、様々な角度から検証し、必要に応じて条件を追加して再計算する必要がある。
しかしながら、人間の想像力には限界があり、必ずしもうまく条件設定でき、また導き出された解の検証がうまくいくとは限らないため。

数値 Simulation は、実 Data の分析と併用することで、より威力を発揮する。

# 画像処理 / 言語処理
## 人の認識
人の顔の認識を簡潔に行なうには**「HOG 特微量」というものを持ちいる。  
単純には「ヒトのシルエットを見て、そのシルエットの形の特徴を、位置や角度で表現する」もの。
### HOG
Histogram of Oriented Gradients の略称。  
**輝度勾配**とも訳される。

### Timelapse
数 frame から１frame のみを取り出した「早送り動画」
- 目で簡単に傾向を掴める。
- Demo 映像として利用すれば分析結果に説得力をつけれる
- 