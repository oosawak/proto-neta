---
title: "Google Three-Live：AIが書いたThree.jsをサンドボックスでGLB／USDZに変換し、Web・Android・iOSで3D／AR／WebXR表示"
date: 2026-11-05
status: stock
source: https://opensource.googleblog.com/2026/11/introducing-three-live-ai-generated-3d-ar-webxr.html
entry: チャット
summary: "Google公開のオープンソース（Apache 2.0、v1.0.0 Developer Preview）。AI生成のThree.jsコードをサンドボックス実行してGLBとUSDZにコンパイルする仕組み。本人がThree.jsの書き方からPyxel 3で使えるGLBを作れることを実証済み。"
type: proto
---

- 元の情報: Google Open Source Blogの公式記事（2026-11公開）。リポジトリは github.com/google/three-live 。なお記事には「Googleの公式サポート製品ではない」と明記されている。
- 要点: AIが生成したThree.jsコードをサンドボックスで実行し、GLB（glTF 2.0）とUSDZにコンパイルして、Web・Android・iOSの各プラットフォームで3D／AR／WebXR表示する仕組み。ネイティブ側のコンパイラはRust製（Boa ECMAScriptエンジン）で、Web側はWeb Worker等の隔離実行。実行時間やジオメトリ量に上限があり、暴走するスクリプトでもホストを止めない作り。
- 本人の実証（2026-11-05）: Three-Liveで、Three.jsの書き方で作って toGLB() で書き出すと、Pyxel 3で使える形のGLBが作れた。
- 面白いところ: 「3Dモデルをモデリングソフトで作る」のではなく「コード（テキスト）で書いて資産化する」流れで、本人のテキスト定義→エンジンが描く、という作り方と噛み合う。サンドボックス＋上限付きの実行は、HTMLプレイヤーの隔離実行の考え方とも近い。
- 使い道の見立て: 城や建物のモデルをテキスト（Three.jsコード）から生成してGLB化し、本の付属3Dマップ・戦国ガイド・奥羽一生録で共用する。HTMLプレイヤーの3Dカセットや、Pyxel 3への素材供給にも回せる。試作モデルの制作は別途、新しい専用サイドチャットで進める。
- 入口: チャット
