---
title: 'ChatGPT Sites：中身はCloudflare Workersで、D1とR2が厚めに付いてくるという話'
date: '2026-10-31'
status: stock
source: 'https://x.com/nakasyou0/status/2116176314621460594'
entry: 'チャット'
summary: '無料のCloudflare Workersの代わりにChatGPT Sitesを使っている、という実践報告。Plus以上でサイトを作り放題、中身はWorkersで、サイトごとに10GBのD1とほぼ無制限のR2が付くという。自分のCloudflare基盤との比較材料として。ただし各上限は投稿者の主張で、公式仕様は未確認。'
type: proto
---

- 元の情報: X投稿 @nakasyou0（nakasyou、2026-10-30 23:32） https://x.com/nakasyou0/status/2116176314621460594 ／ 投稿内にURLなし。ChatGPT Sitesの公式情報は今回は未確認
- 要点: 投稿者の実践報告。最近は無料のCloudflare Workersの代わりに ChatGPT Sites を使っている。主張の骨子は次のとおり。Plus以上のプランなら Sites を作り放題で、中身は Cloudflare Workers。そのうえで、Workers Paid相当の10GBの D1（SQLiteデータベース）がサイトごとに付き、オブジェクトストレージの R2 がほぼ使い放題（リミットは明記されていない、とのこと）なのでファイルを置きまくっている。単純な D1＋R2 の Worker なら、ChatGPT Sitesへデプロイした方が「めっちゃ強化されたの」が付いてくるのでおすすめ。一方で Durable Objects や Vectorize は使えない。いずれも投稿者の主張であり、ChatGPT Sitesの提供条件・上限の公式な裏付けは今回取っていない。
- 面白いところ: 自分の商用版Markdown CMSは Workers／R2（＋Queues）で組んでおり、まさに同じ部品の話である点。「自前アカウントで素直に組む」と「ChatGPT側の枠に乗る」の差がどこに出るか（上限、継続性、持ち出し可否）は、基盤選びの判断材料になる。本人のCloudflare OSへの評価（既存の道具立てで足りているので当面放置）と並ぶ、「外の枠を借りる」選択肢の観察として置ける。
- 作れそうなもの: まず公式情報で提供条件と上限を確認するのが先。そのうえで、小さな D1＋R2 の Worker 1本（例: 管理画面まわりの試作）を ChatGPT Sites 側と自前Cloudflare 側の両方に置き、付けられる上限・手間・運用の自由度を比べる試作。本番の置き場を移す話ではなく、あくまで比較実験として。
- 入口: チャット
