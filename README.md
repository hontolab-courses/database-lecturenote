# 科目「データベース」

## Jupyter Bookの使い方
### インストール
```
pip install jupyter-book
```

### 作業方法
基本的に作成するファイルは`md`ファイルか`ipynb`ファイルのいずれか．
後者の場合，Jupyter Notebookで作成すればよい．
どちらのファイルも作成後，以下の`build`コマンドで最終ファイルを生成できる．

### コマンド
#### プロジェクト生成
```
jb create lecture_hogehoge
```

#### ビルド
対象プロジェクトのディレクトリに移動して`jb build`コマンドを実行．

```
$ cd lecture_hogehoge
$ jb build --all .
```

`jb build .`のように`--all`オプションを入れない場合，変更・追加したページしか更新されない．目次を含めてビルドしたい場合は，更新していないページから追加したページへのリンクも更新する必要がある．そのため，`--all`オプションを入れてJupyter Book全体を再構成するようにする．


### MyST Markdown
使用頻度の高いのは[Directives](https://qiita.com/magolors/items/620860558661b527f267)（コンテンツブロック作成機能）．
