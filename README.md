# semparse-core-python

This repository contains a Python wrapper to call VerbNet Parser which was written in Java. See `python_call_java.py` for details. Before running, make sure you download and unzip (1) the pre-trained models and mapping files from [here](https://drive.google.com/open?id=1qESz4tlviIjsAYzb8qlUg1ps3o37i6l3) (2) `semparse-core.jar` from [here]().

The root directory should look like this:

```
.
├── python_call_java.py
├── README.md
├── semparse-core.jar
└── semparse
    ├── lvm.tsv
    ├── nlp4j-verbnet-3.3.bin
    ├── pbvn-mappings.json
    ├── propbank-srl
    └── unified-frames.bin
```
