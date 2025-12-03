# TIL

Today-I-Learned snippets. Inspired by [vidyabhandary](https://github.com/vidyabhandary), which was inspired by the post [Building a self-updating profile README for GitHub](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/) by [Simon Willison](https://github.com/simonw) 



### Pre-requisites

To reproduce this TIL you can install the requirements using uv.

```python
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt

  # The workflow remains the same:
  # 1. Run python build_database.py to update the SQLite database with both .md and .ipynb files
  # 2. Run python update_readme.py --rewrite to update the README.md
  
  python build_database.py
  python update_readme.py
```



<!-- count starts -->12<!-- count ends --> TILs so far. 
<!-- index starts -->

## scripts

* [Mini scripts bat file](https://github.com/marcelcastrobr/til/blob/main/scripts/script_create_open_folders.md) - 2022-10-12
* [Visual Studio Code using your Browser](https://github.com/marcelcastrobr/til/blob/main/scripts/vscode-server-remote.md) - 2024-06-19

## ml

* [Random Cut Forest](https://github.com/marcelcastrobr/til/blob/main/ml/random_cut_forest.md) - 2022-10-12
* [Run your own LLM on your macOS using Llama.cpp](https://github.com/marcelcastrobr/til/blob/main/ml/llamacpp-macos.md) - 2024-06-19

## data-application

* [Encoding and Decoding](https://github.com/marcelcastrobr/til/blob/main/data-application/encoding.md) - 2022-10-17
* [Document Parsing using Grobid](https://github.com/marcelcastrobr/til/blob/main/data-application/doc_parsing.md) - 2024-08-20

## python

* [PIPENV](https://github.com/marcelcastrobr/til/blob/main/python/pipenv.md) - 2022-11-25
* [Windows File System](https://github.com/marcelcastrobr/til/blob/main/python/wfs.md) - 2024-08-06
* [Conda and Miniconda](https://github.com/marcelcastrobr/til/blob/main/python/conda.md) - 2024-08-14
* [Variable in Python: short recap](https://github.com/marcelcastrobr/til/blob/main/python/python_variables.md) - 2024-11-11

## snowflake

* [snowcd - snowflake connectivity diagnostic tool](https://github.com/marcelcastrobr/til/blob/main/snowflake/snowcd.md) - 2025-02-14

## notebooks

* [One hot encodding Implementations](https://github.com/marcelcastrobr/til/blob/main/onehot.ipynb) - 2025-12-03
<!-- index ends -->

---

[![Build README](https://github.com/marcelcastrobr/til/workflows/Build%20README/badge.svg)](https://github.com/marcelcastrobr/TIL/actions)
