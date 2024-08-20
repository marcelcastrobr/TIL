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



# Example

PDF: https://www.tesla.com/ownersmanual/modely/en_us/Owners_Manual.pdf

### Creating a pdf test file

```bash
#Decrypt pdf
qpdf tesla-y-manual.pdf --decrypt tesla-y-manual-decrypted.pdf
Tips: Reducing amount of page for test

pdftk A=tesla-y-manual-decrypted.pdf cat A1-20 output tesla-y-manual-mod.pdf
```



### Extracting content

```python
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import GrobidParser

loader = GenericLoader.from_filesystem(
    "../resources/test_pdf/mod/",
    glob="*",
    suffixes=[".pdf"],
    parser=GrobidParser(segment_sentences=False),
)
docs = loader.load()

#print(docs)

#print(docs[3].page_content)
for doc in docs:
    print(doc)
    print("\n")
```



### Result

```json
page_content='Illustrations are provided to improve conceptual understanding only.Depending on vehicle options, software version, market region and regional and language settings, the details displayed on the screen will differ.' metadata={'text': 'Illustrations are provided to improve conceptual understanding only.Depending on vehicle options, software version, market region and regional and language settings, the details displayed on the screen will differ.', 'para': '1', 'bboxes': "[[{'page': '7', 'x': '82.29', 'y': '231.88', 'h': '281.91', 'w': '10.71'}], [{'page': '7', 'x': '366.42', 'y': '231.88', 'h': '199.15', 'w': '10.71'}, {'page': '7', 'x': '54.00', 'y': '242.68', 'h': '395.84', 'w': '10.71'}]]", 'pages': "('7', '7')", 'section_title': 'NOTE:', 'section_number': 'None', 'paper_title': '', 'file_path': '../resources/test_pdf/mod/tesla-y-manual-mod.pdf'}


page_content='When full self-driving is enabled (if equipped), the car status area displays visualizations of the road and your vehicle's surroundings.You can expand/condense the visualization by dragging the car status area from side to side.Expanding the visualization displays more details about the roadway and its surroundings, including road markings, stop lights, and objects (such as trash cans and poles).' metadata={'text': "When full self-driving is enabled (if equipped), the car status area displays visualizations of the road and your vehicle's surroundings.You can expand/condense the visualization by dragging the car status area from side to side.Expanding the visualization displays more details about the roadway and its surroundings, including road markings, stop lights, and objects (such as trash cans and poles).", 'para': '2', 'bboxes': "[[{'page': '8', 'x': '49.50', 'y': '62.04', 'h': '486.97', 'w': '10.71'}, {'page': '8', 'x': '49.50', 'y': '72.84', 'h': '57.31', 'w': '10.71'}], [{'page': '8', 'x': '109.04', 'y': '72.84', 'h': '381.78', 'w': '10.71'}], [{'page': '8', 'x': '493.04', 'y': '72.84', 'h': '59.28', 'w': '10.71'}, {'page': '8', 'x': '49.50', 'y': '83.64', 'h': '477.73', 'w': '10.71'}, {'page': '8', 'x': '49.50', 'y': '94.44', 'h': '160.17', 'w': '10.71'}]]", 'pages': "('8', '8')", 'section_title': 'Touchscreen', 'section_number': 'None', 'paper_title': '', 'file_path': '../resources/test_pdf/mod/tesla-y-manual-mod.pdf'}

```

