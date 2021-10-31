# Python 実践データ分析100本ノック

---
# Web からの注文数を分析する
## Data を読み込んでみよう。
分析業務の目的にも寄るが
- 抽象的なお題
- 具体的なお題

どちらででも、まず**Data の全体像を把握**することが大事。

全 Data の先頭５行を表示させることで、どのような Data が存在するのか、それぞれの Data 列の関係性など、 Data の大枠を掴むことができる。
複数に渡って存在する Data をかき集め、Data の概要を捉え**分析に適した形に加工**することから始める。

## Data を結合( Union )してみよう

**Union を行う Method**
```python
import pandas as pd
pd.concat([data_frame_1, data_frame_2], ignore_index=True)
```

### Union
Data 数を行方向に増やす（縦に結合する）こと。

## 売上 Data 同士を結合（Join）してみよう
**主軸になる Data** を考えつつ、どの列を Key に Join するか考えていく。

### ex). 
主軸になる Data : 最も粒度が細かい Data
1. 足りない（付加したい）Data 列は何か？
2. 共通する Data 列は何か？

※ 結合する Data 間で片方により粒度が細かい Data 等がある場合は付加してしまうと二重計上になってしまうので注意する。

**Join を行う Method**
```python
import pandas as pd
pd.merge(main_data_frame, data_frame[['data列', 'data列_2', '･･･',]], on='Join key にする Data列', how='Join 方法')
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

![IMG_1530](https://user-images.githubusercontent.com/7993391/139601124-cfb84f75-2015-42aa-ab5f-cda45bff8977.jpg)

**注意点**  
正しく結合条件を設定しないと、Data の欠落が起こる。  
<small>ex). 売上 Data と商品 Master を Inner join 。商品 Master に未登録商品があった場合に売上 Data かその売上が除外され集計に影響がでる。</small>

### Outer join
- ２つのどちらか片方にでも Data が存在すれば対象とる。
- 単純に Data を結合した場合の結合方法。

![File](https://user-images.githubusercontent.com/7993391/139601207-a22d2f86-8099-4e6c-92db-77e076153a68.jpg)

**注意点**  
- Data①にしか Data がない行の Data②にはすべて NULL が代入される。
- Record 件数が不用意に増える

### Left(Right) join
どちら片方の Data を主としたい場合に有効な結合方法
 
- Left join: 結合される側の Data がすべて使われる。
- Right join: 結合する側の Data がすべて使われる。

![File (1)](https://user-images.githubusercontent.com/7993391/139601215-5736f0b9-ad13-43c2-8467-211d7321fa75.jpg)

**注意点**
主軸にする Data 側に Data が存在しない場合、抽出 Data に NULL が入るので欠損地の確認や補完が必要になる。

## 結合の注意
kb結合 Data に重複などが存在する場合、Data が増えてしまう Case があり集計に影響する。
