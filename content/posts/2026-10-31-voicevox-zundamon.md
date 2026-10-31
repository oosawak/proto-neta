---
title: 'Museの音声をVOICEVOX（ずんだもん）に替える'
date: '2026-10-31'
status: stock
source: 'https://x.com/sakura_beers/status/2115996248448909630'
entry: 'チャット'
summary: 'Museの作業環境（中身はUbuntu）にVOICEVOX Engineを入れて動かし、Museの音声読み上げを「ずんだもん」の声に替えた、という動画付きの投稿。'
type: proto
---

- 元の情報: X投稿 @sakura_beers（山桜ぱぱ、2026-10-30 11:36） https://x.com/sakura_beers/status/2115996248448909630 ／ 一次情報: VOICEVOX公式サイト https://voicevox.hiroshiba.jp/
- 要点: Museの作業環境（中身はUbuntu）にVOICEVOX Engineを入れて動かし、Museの音声読み上げを「ずんだもん」の声に替えた、という動画付きの投稿。動画ではVOICEVOX Engine v0.26.0（Linux CPU版）のインストールや、ずんだもん（ノーマル）でのサンプル作成が確認できる。本人の返信では、VM再配置でエンジンが消える／止まる場合に備え、仕様を出してもらい、止まっていたら自動起動する仕組みも入れてもらった、とされている。VOICEVOX EngineはHTTP APIで呼べる音声合成エンジンで、LinuxでもCPU版が動く。
- 面白いところ: 自前でサーバーを立てず、Muse自身のVMの中でエンジンが完結する点。声を替えるだけで相棒感が大きく変わる点。
- 作れそうなもの: こちらのMuse環境でもVOICEVOX Engine（Linux CPU版）を入れ、音声メモ／読み上げの声をずんだもん等に替える試作。あわせて、VM再配置後にエンジンが消える問題への備えとして、仕様メモと自動起動の仕組みもセットで作る。ずんだもん等のキャラクター音声を使う場合はクレジット表記（例: VOICEVOX:ずんだもん）が必要な点に注意。
- 入口: チャット
