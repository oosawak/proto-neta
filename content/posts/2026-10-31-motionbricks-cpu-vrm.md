---
title: 'MotionBricksをCPUだけで動かして、ちびキャラVRMへ移す'
date: '2026-10-31'
status: stock
source: 'https://x.com/Kashiko_AIart/status/2116000629021946024'
entry: 'チャット'
summary: 'MotionBricks（人間版）を、ゲームエンジンなし・GPUなしのノートPCで動かし、生成モーションを3頭身のVRMキャラへ移した、という動画付きの投稿。'
type: proto
---

- 元の情報: X投稿 @Kashiko_AIart（かし子、2026-10-30 11:53） https://x.com/Kashiko_AIart/status/2116000629021946024 （KANA @KanaWorks_AI のMotionBricksをGodotで動かした投稿の引用） ／ 一次情報: NVIDIA MotionBricks公式 https://nvlabs.github.io/motionbricks/ （ストック1件目と同じ技術）
- 要点: MotionBricks（人間版）を、ゲームエンジンなし・GPUなしのノートPCで動かし、生成モーションを3頭身のVRMキャラへ移した、という動画付きの投稿。本人の返信によると、仕組みは「現在の姿勢数コマ＋ゴールの姿勢」から間の短い動きを生成してつないでいく形で、公式が前提とするTensorRT（GPU）ではなく、同梱のONNXモデルをCPUのONNX Runtimeで実行し、1回の生成は約60ミリ秒（Ryzen 5 7535HSのノートPC）、書き出しはVRM用モーション（VRMA）だったとのこと。ちびキャラへの移植では、顔の向きや手とスカートの干渉に手を入れたという工夫や、モデルは商用可だが付属のお手本モーション（BVH）は評価用ライセンスなので使い方を限定した、という注意も添えられている。
- 面白いところ: GPUがなくてもCPUだけで約60ミリ秒なら、ブラウザ／軽い環境での応用の幅が広がる点。等身の違うキャラへ移すときの具体的なつまずきと手当てが書かれている点。
- 作れそうなもの: ONNXモデル＋ONNX Runtime（CPU）でMotionBricksを動かし、ゴール姿勢をつないで歩行・着席などの動きを作り、VRMAで書き出して自作のVRM／ちびキャラに当ててみる試作。ストック1件目（WebGPU版）と合わせて、実行環境の違い（WebGPU／CPU）を比べる材料にもなる。
- 入口: チャット
