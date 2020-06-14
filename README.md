# Book of Abstracts of the IPMU 2020
[IPMU 2020](https://ipmu2020.inesc-id.pt) -- 18th International Conference on Information Processing and Management of Uncertainty in Knowledge-Based Systems.
Lisbon, Portugal, June 15th – 19th 2020


## Extracting the content of the Abstracts for each paper

The Abstracts, as well as the Keywords, are extracted directly from the original TEX files provided by the authors, and available at EasyChair. 

Please download the proceedings from EasyChair to a local directory, and provide the correct directory to the script `scripts/collect_info.sh`. It uses the README_EASYCHAIR file, available at each paper's directory, to obtain the name of the main TEX file to use. In then extracts the `abstract` content to a file.

Non-latex files must be processed manually. I stored them into `metadata/abstracts_manually`


## Generating TEX files for each abstract

You have to create the file `metadata/toc.tsv`, containing information about each paper:

    * `reference` (one for each abstract file name)
    * `title` paper title
    * `authors` paper authors

The following command can be used to generate a TEX file for each abstract, based on the abstract content, previously extracted form the original TEX or manually provided.

    ./scripts/meta2tex.py -outdir abstracts ./metadata/abstracts/*.tex ./metadata/abstracts_manually/*.tex

The script also words with a single file

    ./scripts/meta2tex.py ./metadata/abstracts/12372005.tex

