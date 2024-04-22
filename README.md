# NMR metadata schema using LinkML

This repository contains [LinkML](https://linkml.io/) description of metadata description of NMR data.

For more information about the workflow, check out this [gitlab](https://gitlab.desy.de/ric/opendata-metadata) tutorial.

## Overview
The file nmr.yaml defines the classes NMRDataset. This contains all metadata that is common for 1D NMR data, which includes:
- owner
- email
- instrument_name
- principal_investigator
- proposal
- acquisition_date
- sample
- nuclide
- sepctrometer_frequency
- magnetic_field
- concentration
- solvent
- pulse_program
- gradient_list

## Getting started

You need to install LinkML if you wish to work directly with these files. The [Quick Install Guide](https://linkml.io/linkml/intro/install.html) page describes how to do this.

### 1. Schemasheets

Schemasheets is part of the LinkML toolset that allows a LinkML data description to be converted to a spreadsheet and vice versa. See install guide [here](https://github.com/linkml/schemasheets).

Generation of spreadsheet through linkml schemasheets

```
linkml2schemasheets-template -i nmr.yaml -o nmr_concise.tsv -s concise
```
or
```
linkml2schemasheets-template -i nmr.yaml -o nmr_exhaustive.tsv -s exhaustive
```

### 2. Generate json schema

Generating a corresponding (closed world) JSON-Schema definition (`nmr.schema.json`) for the NMR datasets:

```
gen-json-schema --closed nmr.yaml  >nmr.schema.json
```

### 3. Simple worked examples to validate the csv input metadata

Check ("valdate") that some csv metadata (`my-nmr-metadata.csv`) complies with the SFX metadata defintion (`nmr.yaml`):

```
linkml-validate -s nmr.yaml my-nmr-metadata.csv
```

### 4. Convert validated csv file to json
Specify the input csv file an output json file.
```
python script.py my-nmr-metadata.csv output.json
```

## Next Step
- schema for 2d NMR data
- github action that generate the json schema and puts it in a public location -> github page