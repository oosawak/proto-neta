---
title: "Astryx：Metaが社内で8年育てたUIデザインシステムをOSS公開、AIエージェントが扱う前提の設計"
date: 2026-11-09
status: stock
source: https://x.com/vibe_walking/status/2119625011128619323
entry: チャット
summary: "Metaが社内で8年使ってきたデザインシステムAstryxをMITで公開。UI部品150種以上、React 19とStyleXが土台で、人とAIエージェントが同じ道具立てで組めるようAPI・ドキュメント・CLIを設計してある。"
type: proto
---

- 元の情報: りも（Limo、@vibe_walking）のX投稿（2026-11-09）。Metaが社内で8年開発してきたUIデザインシステム「Astryx」をOSSで公開した、という紹介で、投稿者本人も試し始めているところ。
- 一次情報（GitHub meta/astryx のREADMEで確認）: ライセンスはMIT、現在はBeta。土台はReact 19とStyleX。アクセシビリティ対応のUI部品が150種以上、テーマはCSSカスタムプロパティの上書きで差し替えでき、ダークモード、テンプレート、CLI（@astryxdesign/cli）まで一式。部品のソースを自分のプロジェクトへ取り出す「swizzle」もできる。Meta社内では13,000以上のアプリで使われてきたという。
- 面白いところ: 「AIエージェントが扱うことも想定した設計」が売りで、API・ドキュメント・CLIを、人とAIアシスタントが同じやり方で組めるように揃えてある（リポジトリにもCLAUDE.mdやAGENTS.mdが入っている）。本人の「AI運用前提で道具を設計する」という考え方と真っ直ぐ重なる実例。登録済みの emilkowalski/skills や unslop（エージェントにデザインの目を持たせる系）とも並べて見られる。
- 作れそうなもの: React前提なので、本人の単一HTML中心の作りには直接は乗らない。商用版Markdown CMSの編集アプリなど、画面部品の多い管理系UIを作る段での部品基盤の候補。それ以上に、エージェント向けにドキュメントとCLIを揃える設計の進め方自体が、自分の道具設計の参照になる。
- 入口: チャット
