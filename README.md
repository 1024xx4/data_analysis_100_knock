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