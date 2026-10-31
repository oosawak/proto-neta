# 試作ネタ帳（proto-neta）

「この先、試作してみたいもの」の種を貯める場所。発信のネタ帳（neta-cho リポの neta.md）と分けて、作る方のネタはここに置く。

公開ページ: https://oosawak.github.io/proto-neta/

Markdown CMS と同じ作りの静的サイト:

- 正本: `content/posts/` の Markdown（1件＝1ファイル、frontmatter 付き）
  - frontmatter: title／date／status（stock＝ストック、doing＝試作中、done＝試作済み・見送り）／source／entry／summary
  - 本文: 「元の情報／要点／面白いところ／作れそうなもの」の箇条書き
- `python3 scripts/build.py` で `data.json` を生成
- `index.html`＋`assets/app.js` が data.json を読み、状態フィルタ付きの一覧と個別ページを表示

## 登録のしかた

1. `content/posts/YYYY-MM-DD-<slug>.md` を1件追加する
2. `python3 scripts/build.py` を実行する
3. まとめて commit・push する

収集は専用チャット「試作ネタ：収集」で行い、XやWebで見つけたURLを Muse が軽く確認して登録する。深い調査は試作を始める段で行う。
