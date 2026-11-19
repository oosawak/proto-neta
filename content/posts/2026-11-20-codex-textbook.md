---
title: "初心者向けCodexの教科書：Codex×GPT-5.5の全体像を1本にまとめた保存版X記事"
date: 2026-11-20
status: stock
source: https://x.com/Codestudiopjbk/status/2049638285019132304
entry: チャット
summary: "Codex StudioによるX記事（長文）。Codexの3つの使い方、設定ファイル、料金、画像生成との連携、IDE連携までを初心者向けに整理し、指示の書き方として Goal／Context／Constraints／Done when の4要素を推している。"
type: proto
---

- 元の情報: Codex Studio（@Codestudiopjbk）のX記事「【保存版】初心者向けCodexの教科書」（2026-04-30公開、読了時間16分）。2026年4月29日時点のOpenAI公式資料・システムカード・APIドキュメント・開発者ガイドを読み込んでまとめた、と本文に明記されている。
- 要点（記事の記載をもとにした要約。数値は記事時点のもので、一次資料での再確認はしていない）: Codexは「会話するAI（ChatGPT）」ではなく「作業するAI」で、使い方はデスクトップアプリ／CLI／Cloud の3つ。設定は ~/.codex/config.toml で、初心者向けの推奨は approval_policy が on-request、sandbox_mode が workspace-write。裏側のモデル GPT-5.5 はコンテキスト約105万トークン・最大出力12.8万トークンとされ、普段は下位モデル、複雑な処理だけ 5.5 という使い分けと、Batch／Flex の5割引が紹介されている。画像生成 gpt-image-2 との連携（日本語の文字描画が正確、Codexからそのまま呼んでファイル保存まで）も1章ある。
- 面白いところ: 指示の書き方として挙げている4要素「Goal（目的）／Context（文脈）／Constraints（制約）／Done when（完了条件）」が、本人の指示書の型（件名／目的／背景／やってほしいこと／守ること／完了の条件）とほぼ同じ発想になっているところ。他人の実務でも同じ型に収束している、という裏付けとして読める。
- 作れそうなもの: 本人の Codex 運用（常駐Codexへの指示書、ハーネスの読み解き）の参照資料。あわせて、執筆中のミューズ実用ガイド本や Codex ガイド側で「初心者にどう説明するか」の構成の参考にもなる。試作というより手元に置く教科書枠。
- 入口: チャット
