
import pathway as pw
from pathway.xpacks.llm.embedders import OpenAIEmbedder
from pathway.xpacks.llm.splitters import TokenCountSplitter
from pathway.xpacks.llm.vector_store import VectorStoreClient, VectorStoreServer
from pathway.xpacks.llm import parsers
from dotenv import load_dotenv 
import os
# Here we show how to configure a server that uses LangChain document processing components

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter


PATHWAY_PORT = 8765

# Load .env file
load_dotenv()





if __name__ == "__main__":
    # Assuming `data_sources` is a list to store your data sources
    data_sources = []

    # This creates a connector that tracks files in Google Drive.
    # # Please follow the instructions at /developers/user-guide/connectors/gdrive-connector/ to get credentials.
    data_sources.append(
        pw.io.gdrive.read(
            object_id="13JLxItvzVcCnDs-JV1yrR_QMDf3sFvNv", # Change this to your own google drive object
            service_user_credentials_file="credentials.json", # Make sure the google cloud `credentials.json` is in the same directory
            with_metadata=True,
            # mode="static",  # Uncomment if static mode is required
            refresh_interval = 30,
            )
    )

    

    # Choose document transformers
    text_splitter = TokenCountSplitter(min_tokens = 300, max_tokens= 1200)
    embedder = OpenAIEmbedder(api_key=os.environ["OPENAI_API_KEY"]) # TODO: create a local embedder with lepton ai

    # The `PathwayVectorServer` is a wrapper over `pathway.xpacks.llm.vector_store` to accept LangChain transformers.
    # Fell free to fork it to develop bespoke document processing pipelines.
    vector_server = VectorStoreServer(
        *data_sources,
        parser=parsers.ParseUnstructured(mode="paged"),
        embedder=embedder,
        splitter=text_splitter,
    )

    vector_server.run_server(host="127.0.0.1", port=PATHWAY_PORT, threaded=False, with_cache=False)
    