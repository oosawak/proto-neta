---
title: 'Kanvas：AIエージェントと人が同じボードを見るタスク管理'
date: '2026-10-31'
status: stock
source: 'https://x.com/AiAircle34052/status/2116063805641986140'
entry: 'チャット'
summary: 'Claude CodeやCodexに頼んだ作業の進み具合を、AIと人が同じタスクボードで確かめられる無料ツール（MIT）。エージェントが計画と進捗をボードへ書き込み、人はブラウザで眺めて承認・軌道修正する。'
type: proto
---

- 元の情報: X投稿 @AiAircle34052（Aircle｜AIコミュニティ、2026-10-30 16:05） https://x.com/AiAircle34052/status/2116063805641986140 ／ 元の投稿: @XMihura（Mihura）の紹介動画付き投稿 https://x.com/XMihura/status/2115110716629987376 ／ 一次情報: GitHub https://github.com/XMihura/Kanvas 、PyPI「kanvas-board」
- 要点: Claude CodeやCodexに頼んだ作業が今どこまで進んでいるかを、AIと人が同じボードで見られる無料ツール「Kanvas」が公開された、という紹介投稿。一次情報によると、計画と進捗はプロジェクト内の `kanvas.json` 1ファイルに置かれ、エージェントは `kanvas.py` というCLI経由でだけ書き込む（手順に合わない変更は弾かれる）。人はブラウザでボードを開き、承認・軌道修正・レビューをする。導入はプロジェクトのフォルダで `uvx kanvas-board init` と打つだけで、ボード一式と「AI向けの使い方スキル」が `.agents/skills/kanvas/`（Claude Code用は `.claude/skills/` にも）入る。実体はJSON 1つ＋Pythonスクリプト1つ＋HTML 1枚で、アカウントもビルドも依存追加もなし。Claude Code／Codex／Cursor／Gemini CLI／OpenCode／GitHub Copilotなど、コマンドを実行できるAIなら複数を同時に使える。なお同名の別サービス（getkanvas.ai等）とは別物。
- 面白いところ: 「頼んだ仕事の進捗はチャットを遡らないと分からない」という、自分のCodex運用でも起きている問題への答えになっている点。進捗の置き場がクラウドのボードではなく、コードの隣のJSONファイル1つで、エージェント側の書き込み口（CLIとスキル）までセットで配っている点。
- 作れそうなもの: 自分のどれか1リポ（例: neta-cho や小さなゲーム試作）で `uvx kanvas-board init` を入れ、Codexへの指示書運用と並行して、計画と進捗をボードに書かせてみる試作。今の「指示書Markdown＋報告Markdown」の往復と比べて、進み具合の見え方と手間がどう変わるかを見る。自分の処理量の記録（work-log）の置き換え・連携先としても考えられる。
- 入口: チャット
