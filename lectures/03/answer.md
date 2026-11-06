# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
- `--trace` で見えたツール呼び出し（ツール名と引数）：
- 1つの質問での LLM 呼び出し回数（`requests`）：
- 追加したツールと、docstring に書いた説明：

## 宿題

- 取り組んだレベル：発展A
- やったこと：Pydantic AIで実装した学習支援エージェントを、Google ADKを用いて再実装した。モデル、INSTRUCTIONS、検索ツールは共通とし、エージェントの構築方法のみ変更した。
- 結果：「lecNN-start タグとは何ですか？」という質問に対し、Pydantic AIとGoogle ADKの両方で、各回の演習開始時点を示すGitタグであるという回答が得られた。

また、Google ADK版ではLoRAとQLoRAの違いについても適切に説明され、関連する講義として第2回が提示された。

質問：「AIE2026の講座で使う『lecNN-start タグ』とは何ですか？」, 「LoRAとQLoRAの違いを説明してください。」
Pydantic AIの出力
    [model] gemini-3.5-flash-lite
    「lecNN-start タグ」とは、AIE2026の講座リポジトリにおいて、各回の演習開始時点のコードに付けられているGitタグのことです（例: `lec03-start`）。

    このタグのメリットは、前の回の進捗が完了していなくても、このタグの位置から新しくブランチを切ることで、いつでもその回の演習をスムーズに始められるようになっている点です。

    （関連：第1回）

    --- trace ---
    [tool call]   search_glossary({'query': 'lecNN-start タグ'})
    [tool return] search_glossary -> [{"term": "lecNN-start タグ", "lecture": 1, "definition": "AIE2026の講座repoで、各回の演習開始時点のコードに付けているGitタグ（例：lec03-start）。前の回が終わっ…
    [usage] RunUsage(cost=Decimal('0.0006695'), details={'text_prompt_tokens': 1215}, input_text_tokens=1215, input_tokens=1215, output_tokens=122, requests=2, tool_calls=1)

  [model] gemini-3.5-flash-lite
  **LoRA**と**QLoRA**の主な違いは、ベースモデルの重みを量子化するかどうか、そしてそれに伴うメモリ消費量にあります。

  * **LoRA（Low-Rank Adaptation）**
    * 事前学習済みモデルの重みを固定したまま、重みの更新分を小さな低ランク行列で近似し、その部分だけを学習するPEFT（Parameter-Efficient Fine-Tuning）の手法です。
    * 学習パラメータ数や保存するファイルサイズを大幅に削減できます。

  * **QLoRA（Quantized LoRA）**
    * LoRAの仕組みをベースにしつつ、**ベースモデルの重みを4ビットなどの低ビットに量子化**してメモリ消費量をさらに劇的に抑える手法です。
    * これにより、限られたGPUメモリ環境でも、より大きなモデルを効率的にファインチューニングできるようになります。

  （第2回）

    --- trace ---
    [tool call]   search_glossary({'query': 'LoRA'})
    [tool call]   search_glossary({'query': 'QLoRA'})
    [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
    [tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
    [usage] RunUsage(cost=Decimal('0.0010746'), details={'text_prompt_tokens': 1632}, input_text_tokens=1632, input_tokens=1632, output_tokens=234, requests=2, tool_calls=2)



Google ADKの出力
    [user]: AIE2026の講座で使う「lecNN-start タグ」とは何ですか？
    [glossary_agent]: 「lecNN-start タグ」とは、AIE2026の講座リポジトリにおいて、各回の演習開始時点のコードに付けられているGitタグ（例：`lec03-start`）のことです。

    前の回がまだ終わっていなかったり、途中から復習を始めたりする場合でも、このタグを指定してブランチを作成すれば、その回の演習をスムーズに開始できるようになっています。

    関連する回：第1回
    列だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習するパラメータを大幅に削減できます。

    [user]: LoRAとQLoRAの違いを説明してください。
    [glossary_agent]: LoRAとQLoRAの違いは以下の通りです。

    * **LoRA（Low-Rank Adaptation）**
    事前学習済みの重みは固定したまま、重みの更新分を低ランク行列（2つの小さな行列の積）で近似し、その小さな行列だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習するパラメータを大幅に削減できます。

    * **QLoRA（Quantized LoRA）**
  ベースモデルの重みを4ビットなどの低ビットに量子化してメモリを大幅に節約した状態で固定し、その上でLoRAによるファインチューニングを行う手法です。これにより、より大きなモデルを限られたGPUメモリでも効率よく学習できるようになります。

    関連する回：第2回


    ベースモデルの重みを4ビットなどの低ビットに量子化してメモリを大幅に節約した状態で固定し、その上でLoRAによるファインチューニングを行う手法です。これにより、より大きなモデルを限られたGPUメモリでも効率よく学習できるようになります。
    
    （関連する回：第1回）

- 気づき・疑問：
実装方法の違い
  Pydantic AIでは、Agent(instructions=INSTRUCTIONS) によってエージェントを生成し、agent.tool_plain() によってツールを個別に登録する。一方、Google ADKでは、Agent(instruction=INSTRUCTIONS, tools=[...]) のように、エージェントの生成時にツールをまとめて指定する。

回答内容の比較
  2問とも、Pydantic AIとGoogle ADKでほぼ同じ内容の回答が得られた。特に、lecNN-start タグの用途、LoRAとQLoRAの技術的な違い、関連する講義回については一致していた。
  一方、文章の構成や表現には違いが見られた。Pydantic AIではLoRAとQLoRAの違いを冒頭で要約してから説明していたのに対し、Google ADKでは各手法の定義を中心に説明していた。

ツール呼び出しの比較
  Pydantic AIでは、質問①で search_glossary が1回、質問②で2回呼び出されたことを確認できた。質問②では、LoRAとQLoRAをそれぞれ独立した検索引数として指定していた。
  Google ADKでは今回ツール呼び出し履歴を取得していないため、検索回数や引数の一致については判断できない。

まとめ
  今回の実験から、同じモデル・指示・ツールを用いれば、異なるエージェントフレームワークでも内容的に近い回答を得られることを確認した。ただし、回答内容が類似していることは、内部のツール実行過程が同一であることを意味しない。