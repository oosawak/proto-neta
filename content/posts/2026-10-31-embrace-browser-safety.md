---
title: 'EMBRACE：AI開発ツールの「内蔵ブラウザ」の安全問題を点検する'
date: '2026-10-31'
status: stock
source: 'https://x.com/omurice_brand/status/2116072420704694435'
entry: 'チャット'
summary: 'Codexアプリ、Claude Desktop、VS Code、Cursor、GitHub Copilotの5製品について、内蔵ブラウザが通常のブラウザの安全前提（ページはコマンドを実行できない／ローカルファイルは他を読めない／アドレスバーはページが書き換えられない）を崩している…'
type: proto
---

- 元の情報: X投稿 @omurice_brand（おむらいす、2026-10-30 16:39） https://x.com/omurice_brand/status/2116072420704694435 ／ 一次情報: Forever Securityの研究「EMBRACE」（2026-10-29公開、報道例 https://hackread.com/embrace-flaws-ai-coding-tools-code-execution-theft/ ）
- 要点: Codexアプリ、Claude Desktop、VS Code、Cursor、GitHub Copilotの5製品について、内蔵ブラウザが通常のブラウザの安全前提（ページはコマンドを実行できない／ローカルファイルは他を読めない／アドレスバーはページが書き換えられない）を崩している、という研究の整理投稿。製品によっては、プロジェクト内のHTMLを開くことでフォルダ外のファイルを読まれる、隠れた指示でコマンド実行につながる、アドレスバー偽装ができる、といった問題が報告されている。2026-10-29時点の状況として、CursorとGitHub Copilotは修正済み、他は対応中／修正予定なし／時期未公表とされ、実悪用の報告はなし、と投稿・報道とも伝えている（各社の最新状況は未確認）。なおCLI版（Claude Code CLI／Codex CLI）は内蔵ブラウザがないため対象外とされている。
- 面白いところ: 「AIが出したリンクだから安全とは限らない」という、エージェント時代の新しい前提。自分が日常使う道具（VS Code＋Codex等）が対象に含まれている点。
- 作れそうなもの: 自分の作業環境向けの点検チェックリストの試作（各ツールのバージョンと修正状況の確認、知らないリポをセットアップ丸投げしない、プロジェクト内HTMLを内蔵ブラウザで開かない、.envやSSH鍵の扱い等を1枚にまとめる）。試作というより安全確認の種として、最新の修正状況は始める段で各社の公式情報を調べ直す。
- 入口: チャット
