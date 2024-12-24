# ■ APR-Resources
## ディレクトリ構成
- datasets: 研究に用いた誤用事例
- prompt: 単純なLLM利用，2種類の構成のRAG手法についてのプロンプトテンプレート
- result: 適用結果

### `/datasets`構成
- fitbit: Fitbit APIに関するデータセット
- switchbot: SwitchBot APIに関するデータセット
- url: 公開されているREST API仕様へのリンク
    - latest.txt: 最新仕様へのリンク
    - outdated.txt: 非推奨仕様へのリンク

> [!NOTE]
> datasets の中には，複数のエンドポイントに関する誤用が含まれています．
> その場合は，エンドポイントごとに分けて計算しています．


### `/propmt`構成
- llm.txt: 単純なLLM利用で使用したプロンプト
- rag.txt: RAG手法で使用したプロンプト
- db_extended_rag.txt: DBを拡張したRAG手法で使用したプロンプト


### `/result`構成
- llm: 単純なLLM利用に適用した結果
- rag: RAG手法に適用した結果
- db_extended_rag: DBを拡張したRAG手法に適用した結果
