# semparse-core-python

This repository contains a Python wrapper to call VerbNet Parser which was written in Java. See `python_call_java.py` for details.

Before running, make sure you 
 - download and unzip the pre-trained models and mapping files from [here](https://drive.google.com/file/d/1GL0N5DCOPTBnyU-028405AM5RjwszPgM)
 - download `semparse-core.jar` from [here](https://drive.google.com/file/d/1f-3bm_uCC3ThA83CIcEjg5JL01vdaBj2)

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

### Usage

```
python python_call_java.py
```
