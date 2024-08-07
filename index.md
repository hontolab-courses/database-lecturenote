# データベース

* 開講時期: 2年次 前期
* 担当教員：[山本 祐輔](https://hontolab.org/)（名古屋市立大学データサイエンス学部 准教授）

この資料は，名古屋市立大学データサイエンス学部において開講されている講義「データベース」用に作成されたものです．

<!--
本資料はオンライン上でも閲覧できますし，PDF資料として保存することも可能です．
PDF資料が欲しい方は[コチラ]()からダウンロードしてください．
-->


## この講義で学ぶこと，学ばないこと
本講義は，データサイエンスを学ぶ方を対象にしたデータベース講義です．
一般に，データベースの講義はデータベースを使ったシステムの研究・開発を志向する学生，つまりコンピュータサイエンスを専門とする学生に提供されるものです．
しかし，本講義が想定している受講者はデータサイエンス学部の学生であり，その大半はデータ分析のためにデータベースを活用することが想定されます．
そのため，本講義では一般的なデータベースの講義で教授する内容のうち，
- 関係データベースの設計
- 関係データベース用いたデータの検索・分析

を行う上で必要となる知識・スキルに焦点をしぼって授業を行います．

以下，本講義で学ぶこと，学ばないことです．


### 学ぶこと
* データベースの概念
* 関係データモデル
* SQL
* 実体関連モデル
* 正規化
* 索引づけ
* NoSQL

### 学ばないこと
* 関係代数
* 関係論理
* データ格納方式
* 問い合わせ最適化
* トランザクション
* 障害回復


## 授業計画とコンテンツ
| |  日時  | トピック | 講義ノート | スライド資料 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | 04/15 | ガイダンス & データベースを使わない世界 | [Here](content/introduction/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-01) |
| 2 | 04/22 | データベースの概念 | [Here](content/concept-of-database/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-02) |
| 3 | 04/29 | 関係データモデル | [Here](content/relational-data-model/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-03) |
| 4 | 05/13 | SQL（1/3） | [Here](content/sql/01.ipynb) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-04) |
| 5 | 05/20 | SQL（2/3） | [Here](content/sql/02.ipynb) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-05) |
| 6 | 05/27 | SQL（3/3） | [Here](content/sql/03.ipynb) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-06) |
| 7 | 06/03 | SQL演習 - レポート課題1 | [Here](content/exercise/sql.ipynb) |  |
| 8 | 06/10 | 実体関連モデル（1/3） | [Here](content/er-model/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-08) |
| 9 | 06/17 | 実体関連モデル（2/3）| [Here](content/er-model/02.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-09) |
| 10 | 06/24 | 実体関連モデル（3/3） | [Here](content/er-model/03.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-10) |
| 11 | 07/01 | 正規化（1/2） | [Here](content/db-design/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-11) |
| 12 | 07/08 | 正規化（2/2） | [Here](content/db-design/02.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-12) |
| 13 | 07/15 | データベース設計演習 - レポート課題2 | [Here](content/exercise/db-design.md) |  |
| 14 | 07/22 | 索引づけ | [Here](content/indexing/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-14) |
| 15 | 07/29 | NoSQL | [Here](content/nosql/01.md) | [SpeakerDeck](https://speakerdeck.com/trycycle/database-lecture-15) |
| 16 | 08/05 | 期末試験 |  |  |


## レポート課題
### レポート課題1（SQL）
[コチラのページ](content/exercise/sql.ipynb)で出題されているすべての課題を解きなさい．
解答期日，解答方法等については下記を参照すること．

- 設問数：25
- 成績評価における本課題の割合：20％（20点）
- 評価方法：SQL文の実行結果をもとに，1問1点で採点します．ただし，20点以上のスコアは20点とカウントします
<!-- 簡単すぎたので，来年度は問題を難しくするか，10問目以降を採点対象とするとかにする必要がある -->
- 解答〆切り：2024年6月16日 （日）23:59（ **解答は締め切りました** ）
- 解答提出方法：解答用サイト[SQL Autograder](https://sql-autograder.hontolab.org/)経由
- 備考：〆切り以降に提出された解答は，本人の責めに帰さない限り，別途受理します．

### レポート課題2（データベース設計）
[コチラのページ](content/exercise/db-design.md)で出題されているすべての課題を解きなさい．
解答期日，解答方法等については下記を参照すること．

- 設問数：4
- 成績評価における本課題の割合：20％（20点）
- 評価方法：提出物をもとに担当教員が採点します．配点は各設問に記載しています
- 解答〆切り：2024年7月28日 （日）23:59（ **解答は締め切りました** ）
- 解答作成方法
	* [コチラのURL](https://bit.ly/45K0rVI)から入手できるWordテンプレート`report-template.docx`を使用すること（図はPowerPointやdrawioで作成したものをWordに貼り付けるのが楽かと思います）
	* 解答提出時にはWordファイルを`PDFファイル`に変換すること．またファイル名は`学籍番号.pdf`とすること
- 提出方法：[こちら（要大学Microsoft 365アカウント）](https://forms.office.com/r/hMnnDrKEXg)経由
- 備考
	* 読めないものは採点しません
	* 指定されたフォーマット（PDFファイル）以外で提出された場合は採点対象としません
	* 〆切り以降に提出された解答は，本人の責めに帰さない限り，別途受理します．
