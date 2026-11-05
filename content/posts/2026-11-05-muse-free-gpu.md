---
title: "GPUを持たないClaudeに無料GPUを与える：Modal・Kaggle・Colabの無料枠でSDXL生成とLoRA学習"
date: 2026-11-05
status: stock
source: https://x.com/Eris_Create_Lab/status/2118155326981816718
entry: チャット
summary: "GPUのないClaudeに、Modal・Kaggle・Colabの無料枠を使わせて、SDXLの生成環境構築から自作LoRAでの画像生成、LoRA学習まで任せるというX記事。環境構築そのものをエージェントにやらせる発想の実例。"
type: proto
---

- 元の情報: Eris Create Lab（@Eris_Create_Lab）のX記事「GPUを持たないClaudeに、無料GPUを与えて最強にする」（2026-11-05、読了時間8分表示）。同じ投稿者の11月3日の記事（学習用画像の作成からPixAIでのLoRA学習までをClaudeに任せる話）の続編という位置づけ。
- 要点: GPUを持たないClaudeに、Modal・Kaggle・Google Colabの無料枠を渡し、SDXLの画像生成環境の構築そのものからClaudeにやらせる。前回作った自作LoRAをその環境で使って生成し、LoRA学習まで無料GPU上で行う流れ。Claudeへ貼る相談用プロンプトと図解付きで、動画生成への展望にも触れている。
- 面白いところ: 「高性能PCも環境構築の知識も不要」で、足りない計算資源を無料枠から調達して自分で組み立てるエージェント、という構図。本人の環境だと、MuseのVMにはGPUが無く、自宅サーバーのGPU（VRAM 24GB）にはMuseを接続しない決め方をしているので、その間を埋める選択肢として形が合う。
- 作れそうなもの: ブログやゲームの挿絵用に、画風を寄せた自作LoRAを無料枠で学習・生成する試作。記事内の各サービスの無料枠や利用条件、費用の注意点は、試作開始時に現行条件を再確認すること（この登録では未確認）。
- 入口: チャット
