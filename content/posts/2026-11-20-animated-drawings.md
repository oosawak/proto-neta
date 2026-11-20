---
title: "AnimatedDrawings：手描きの人型イラストを自動でリグ付けして踊らせる（Metaの研究実装、MIT）"
date: 2026-11-20
status: stock
source: https://github.com/facebookresearch/AnimatedDrawings
entry: チャット
summary: "子供が描いたような人型の絵をアップすると、人物検出と姿勢推定で関節を自動推定し、BVHのモーションで踊らせるMeta（FAIR）の研究実装。MP4と透過GIFで書き出せる。リポジトリは2025年9月にアーカイブ済み。"
type: proto
---

- 元の情報: 本人がGitHubリポジトリを直接共有（facebookresearch/AnimatedDrawings）。論文「A Method for Animating Children's Drawings of the Human Figure」に付随するコード。
- 一次情報（READMEで確認）: ライセンスはMIT。流れは、絵を学習済みモデル（描画人型の検出器と姿勢推定器、TorchServeで提供）で解析してマスクと関節のアノテーションを自動生成し、実写由来のBVHモーションをリターゲットしてアニメ化する。出力はMP4と透過GIF。関節の推定が外れた場合は、ブラウザの修正画面で関節をドラッグして直してから再生成できる。複数キャラの合成や背景画像の指定も設定ファイル（YAML）で可能。自分の動きを使いたい場合は、スマホ動画からRokoko等でBVHを作って差し込む手順がREADMEにある。
- 注意点: 2025年9月3日付けで作者がリポジトリをアーカイブ済み（今後の保守なし）。検証環境も macOS Ventura／Ubuntu 18.04、Python 3.8系と古い。検出側はDocker＋TorchServeの用意が要る。
- 面白いところ: 「1枚の絵に骨を自動で入れて、既存のモーションで動かす」という発想が、登録済みの StandRig や Rigby2D（パーツ分けPSD前提のリギング）と対になっているところ。こちらはパーツ分け不要で、落書きのような絵でも関節推定で押し切る代わりに、動きはBVHの流し込みになる。登録したばかりの「コードで作る図解アニメ」（部品分けベクター人形）とも、絵を動かす経路の違いで並ぶ。
- 作れそうなもの: 手描きキャラや本の挿絵を、そのまま踊る・歩くGIFや短い動画にする用途。Kimodo（文章→BVH）で作ったモーションをBVHとして差し込む組み合わせも考えられる。アーカイブ済みなので、試すなら動くうちに一度通しておく価値がある。
- 入口: チャット
