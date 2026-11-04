---
title: 'SculptForge：ZBrushの無料オープンソース代替（AIとMCP内蔵）'
date: '2026-11-04'
status: stock
source: 'https://x.com/Ryrenz/status/2117558671286616452'
entry: 'チャット'
summary: 'デジタル彫刻の道具を、ライセンス料なしで。動的トポロジーや再メッシュなどの核の機能に加え、AIブラシ生成と画像／文章からの3D生成を無料で内蔵し、MCPサーバーでエージェントから彫刻もできる。GPL-3.0、現在はv0.8の早期版。'
type: proto
---

- 元の情報: X投稿 @Ryrenz（Ren、2026-11-03 19:05、中国語） https://x.com/Ryrenz/status/2117558671286616452 ／ 一次情報: GitHub https://github.com/islandmed/SculptForge （GPL-3.0、2026-10-21公開、スター約530）
- 要点: 「ZBrushのオープンソース代替が来た」という紹介投稿。一次情報で確認できた骨子は次のとおり。Linux／macOS／Windows対応で、テレメトリなし・アカウントなし・機能の有料壁なし。彫刻の核として、動的トポロジー、マスク、ボクセル再メッシュ、四角形再トポロジー、階層細分化などを備え、書き出しはFBX／glTF／OpenUSDほか、Unreal Engineへ直接送る機能とBlender橋渡しアドオンがある。AIは2系統内蔵される。①Brush Lab: ブラシを言葉で注文するとAIが生成する。既定は無料ホストの開放モデル（GPT-OSS 20B）で鍵不要、オフライン時はローカルOllamaへ切り替え、Claude等の自前接続も可。②画像／文章から3D生成: Hunyuan3D 2／2.1、TRELLIS.2、Stable Fast 3DのHugging Faceデモ経由なら無料で下絵のモデルが作れ、自前のComfyUIにもつながる。さらにMCPサーバー（sculptforge-cli --mcp）を内蔵し、Claude Code等から彫刻・変換・書き出しを操作できる。Gaussian Splatの読み込み（スマホ撮影の取り込み、メッシュ化）にも対応。現状はv0.8の早期版で、ZBrushの.ZTLは直接読めない（GoZ互換の交換は可）。
- 面白いところ: 「高額な専用ソフトの代替」を、単なる模倣でなく、AI生成（下絵作り）とMCP（エージェント操作）まで内蔵して出してきた点。自分の道具立てとの接点も多い。glTF書き出しはThree.jsのブラウザゲームへ持ち込む道になり、Gaussian Splat対応は idol の件（1枚の画像から3D生成）と地続き。自宅GPUサーバー＋ComfyUI／Ollamaという既存の環境にもそのまま乗る。
- 作れそうなもの: 自宅のUbuntuサーバー（GPU搭載）かMacに入れて、画像から3D生成で下絵を作り、少し彫って glTF で書き出し、Three.jsの試作へ置くところまでを通す試作。あわせて、MCP経由でClaude Codeから「変換と書き出しだけ」を自動化できるかも見る。
- 入口: チャット
