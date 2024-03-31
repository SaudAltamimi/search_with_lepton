<div align="center">
<h1 align="center">Search with Lepton - Locally</h1>
Build your own conversational search engine for local files using less than 500 lines of code.
<img width="70%" src="https://github.com/leptonai/search_with_lepton/assets/1506722/845d7057-02cd-404e-bbc7-60f4bae89680">
</div>

## Features
- Built-in support for Large Language Models (LLM)
- Built-in support for local search engine
- Customizable pretty UI interface
- Shareable, cached search results

## Setup Google Drive Real Time Search Engine API

### Pathway Real Time Search - Google Drive
Follow this [tutorial](https://pathway.com/developers/user-guide/connectors/gdrive-connector) to guide you through connecting Pathway to your data stored on Google Drive. Make sure to place `credentials.json` in the same directory as `pathway_retriever.py`.

## Setup LLM and KV

> [!NOTE]
> We recommend using the built-in llm and kv functions with Lepton. 
> Run the following commands to set them up automatically.

```shell
pip install -U leptonai && lep login
```

## Build

1. Run Pathway’s vector store for up-to-date knowledge and information retrieval for your Google Drive.
```shell
export OPENAI_API_KEY=YOUR_OPENAI_API_KEY # temporary
python pathway_retriever.py
```
2. Build the web interface.
```shell
cd web && npm install && npm run build
```
3. Run the server.
```shell
BACKEND=LOCAL python search_with_lepton.py
```

## TODO: Deploy Locally