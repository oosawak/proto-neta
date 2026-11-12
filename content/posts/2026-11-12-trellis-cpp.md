---
title: "trellis.cpp：画像1枚からテクスチャ付きGLBを作る、Python不要のC++／GGML実装（TRELLIS.2移植）"
date: 2026-11-12
status: stock
source: https://x.com/dextune/status/2120375968627888340
entry: チャット
summary: "Microsoftの画像→3Dモデル生成TRELLIS.2-4Bを、C++とGGMLへ移植した実装。実行時にPythonが要らず、背景除去からメッシュ化、UVテクスチャ付きGLB書き出しまでネイティブで走る。CLIと常駐HTTPサーバー、Tauri製デスクトップアプリ付き。"
type: proto
---

- 元の情報: DEXTUNE（@dextune）のX投稿（2026-11-11）。画像をテクスチャ付き3Dモデルに変える trellis.cpp の紹介。
- 一次情報（GitHub pwilkin/trellis.cpp のREADMEで確認）: ライセンスはMIT。Microsoftの TRELLIS.2-4B（画像から3Dを作るパイプライン）を GGML ベースのC++へ移植したもので、背景除去・画像条件付け・メッシュ抽出・UVテクスチャ付きGLB書き出しまで、実行時にPythonなしで動く。重みは約16.5GB。ビルド済みバイナリはLinuxとWindows向けに Vulkan／ROCm／CUDA の各版があり、解像度は512／1024／1536から選べる。任意で stable-diffusion.cpp とつないで、文章→画像→3Dの通しもできる。
- 使い方の形: CLI（画像ファイル→GLB）、常駐HTTPサーバー（POST /generate に画像を送るとGLBが返る）、そして Trellis Studio というデスクトップアプリ（Tauri製。GPUを自動判定して合うサーバーと重みを落とし、ドラッグ＆ドロップで生成、プレビューとギャラリー付き）。
- 面白いところ: 「重い生成はPythonの実験環境で」という前提を外して、単体のバイナリとサーバーに落としてあるところ。本人の自宅サーバー（RTX 3090、VRAM 24GB）ならCUDA版がそのまま乗り、HTTPサーバーとして常駐させれば、ブラウザ側や他の道具から「画像を渡してGLBを受け取る」部品として呼べる。作例の実演は Radeon 8060S 上で行われていて、NVIDIA以外でも動く作り。
- 作れそうなもの: 登録済みの Google Three-Live（文章・コードからGLB）と並ぶ「画像からGLB」の経路。城や建物、アイテムの絵からGLBを作って、Hugging Faceの3Dギャラリーに置く、本の付属3Dマップやゲームで使う、という流れが組める。画像からGaussian Splatを作る idol とは、出力形式（メッシュかスプラットか）の違いで使い分け。
- 入口: チャット
