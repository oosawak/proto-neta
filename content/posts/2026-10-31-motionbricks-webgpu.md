---
title: 'MotionBricksをブラウザのWebGPUで動かす（VRMアバター）'
date: '2026-10-31'
status: stock
source: 'https://x.com/monoradio102/status/2116102225705730249'
entry: 'チャット'
summary: 'モーション生成のNVIDIA MotionBricksを、ブラウザのWebGPUで動かしたというデモ動画付きの投稿。'
type: proto
---

- 元の情報: X投稿 @monoradio102（monoradio、2026-10-30 18:37） https://x.com/monoradio102/status/2116102225705730249 ／ 一次情報: NVIDIA MotionBricks公式プロジェクトページ https://nvlabs.github.io/motionbricks/
- 要点: モーション生成のNVIDIA MotionBricksを、ブラウザのWebGPUで動かしたというデモ動画付きの投稿。矢印キー／WASD等の操作に合わせてその場で動きを生成し、VRM風アバターを動かしている（動画サムネイルに「生成 142 ms（14トークン）」等の表示あり）。公式のMotionBricks自体は、直近のポーズと到達したいポーズから間の動きをリアルタイム生成する仕組みで、コードと学習済みモデルが公開されている。
- 面白いところ: 同じ動きのループではなく、操作に合わせて生成されるので動きが生々しく見える点。本来はゲームエンジンやロボット向けの技術が、ブラウザの中でそのまま動いている点。
- 作れそうなもの: ブラウザで開いて、キー操作に合わせてVRMアバターの動きがその場で生成される小さな試作。なお、投稿者がWebGPUへどう移植したかの実装詳細は投稿内に外部リンクがなく未確認（試作を始める段で調べる）。
- 入口: チャット
