# Document Parsing using Grobid

[Grobid](https://grobid.readthedocs.io/en/latest/) means GeneRation Of BIbliographic Data.

GROBID is a machine learning library for extracting, parsing and re-structuring raw documents such as PDF into structured XML/TEI encoded documents with a particular focus on technical and scientific publications. 

In RAG (retrieval agumented generation), it helps to extract structure text from PDFs for better retrieval (ref.  [RAG vs Fine-Tunning: Pipelines, Tradeoffs and a Case Study on Agriculture](https://arxiv.org/abs/2401.08406) )



## Grobid Installation

It required Java. 

```bash
#Prerequisite Java
sudo apt install default-jdk

#Download
> wget https://github.com/kermitt2/grobid/archive/0.8.0.zip
> unzip 0.8.0.zip

#Install
./gradlew clean install	

```



## Running Grobid

```bash
#Run
./gradlew run
```



## Using Grobid - command line

```bash
grobid_client --input out.pdf --output output processFulltextDocument
```



## Using Grobid Client 

### Single File

```python
from grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="./config.json")

service_name = "processFulltextDocument"

pdf_file = "../resources/test_pdf/out.pdf"

rsp = client.process_pdf(service_name, pdf_file, 
                         generateIDs=True, 
                         consolidate_header=True, 
                         consolidate_citations=True, 
                         include_raw_citations=True, 
                         include_raw_affiliations=True, 
                         tei_coordinates=True, 
                         segment_sentences=True)

print(rsp)
```



### Folder

```python
from grobid_client.grobid_client import GrobidClient

client = GrobidClient(config_path="./config.json")


client.process("processFulltextDocument",
     "../resources/test_pdf",
 output="../resources/test_out/",
 consolidate_citations=True,
 tei_coordinates=False,
 force=True)

```



## Using Grobid - Langchain

Ref. https://python.langchain.com/v0.2/docs/integrations/document_loaders/grobid/

```python
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import GrobidParser

loader = GenericLoader.from_filesystem(
    "../resources/test_pdf/",
    glob="*",
    suffixes=[".pdf"],
    parser=GrobidParser(segment_sentences=False),
)
docs = loader.load()

#print(docs)

#Metadata
for doc in docs:
    print(doc.metadata)
    print("\n")
```

Note: Make sure server is running. Normally in http://localhost:8070/.