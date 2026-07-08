# Microbiome Diversity Analyzer

A Python-based bioinformatics project for analyzing microbiome abundance data from CSV files.

## Project Overview

This project analyzes microbiome abundance tables by calculating diversity metrics, identifying dominant taxa, and exporting results to CSV files.

Microbiome datasets often contain counts of bacterial taxa across different biological or environmental samples. This tool helps summarize those counts into interpretable metrics such as total reads, observed taxa, Shannon diversity, Simpson diversity, evenness, and relative abundance.

This project was built to practice Python programming, biological data analysis, CSV parsing, and beginner microbiome bioinformatics.

## Features

- Reads microbiome abundance data from CSV files
- Supports multiple samples in one table
- Calculates total reads per sample
- Calculates observed taxa per sample
- Calculates Shannon diversity index
- Calculates Simpson diversity index
- Calculates evenness
- Identifies the most abundant taxon in each sample
- Creates a relative abundance table
- Exports diversity metrics to CSV
- Exports relative abundance results to CSV

## Input CSV Format

The input file should have one `taxon` column and one or more sample columns.

```csv
taxon,sample_A,sample_B,sample_C
Bacteroides,120,45,15
Lactobacillus,20,130,55
Prevotella,80,25,160
```

## How to Run

Clone the repo and run:

```bash
python microbiome_analyzer.py sample_abundance_table.csv
```

To choose your own output file names:

```bash
python microbiome_analyzer.py sample_abundance_table.csv --metrics-output metrics.csv --relative-output relative.csv
```

## Output

The program prints a terminal report and creates two CSV files:

```text
diversity_metrics.csv
relative_abundance.csv
```

The diversity metrics file includes:

```csv
sample,total_reads,observed_taxa,shannon_index,simpson_index,evenness,top_taxon,top_taxon_percent
```

## Biological Concepts Used

Microbiomes are communities of microorganisms found in environments such as the gut, soil, water, and other biological systems.

Taxa are groups of organisms, such as bacterial genera or species, depending on the level of classification used in the dataset.

Observed taxa measures how many taxa are present in a sample.

Shannon diversity considers both richness and evenness. A higher Shannon index usually suggests a more diverse community.

Simpson diversity measures the probability that two randomly selected reads belong to different taxa. Higher values usually suggest higher diversity.

Relative abundance shows what percentage of a sample is made up by each taxon.

## Why I Built This

I built this project to connect Python programming with microbiome bioinformatics and biological data analysis.

Microbiome datasets are often organized as abundance tables, so learning how to parse, summarize, and export this type of data is useful for computational biology and environmental biotechnology.

This project shows that I can use Python to turn raw biological count data into interpretable metrics.

## How It Works

The program follows this workflow:

1. Reads a microbiome abundance CSV file
2. Identifies the sample columns
3. Calculates total read counts for each sample
4. Counts how many taxa are present in each sample
5. Calculates Shannon diversity
6. Calculates Simpson diversity
7. Calculates evenness
8. Identifies the most abundant taxon
9. Converts raw counts into relative abundance percentages
10. Exports the results to CSV files

## Files in This Repository

```text
microbiome-diversity-analyzer/
├── microbiome_analyzer.py
├── sample_abundance_table.csv
└── README.md
```

## Limitations

This is a beginner-friendly microbiome analysis tool and not a full professional microbiome pipeline.

It does not perform quality control, taxonomic classification, rarefaction, statistical testing, or differential abundance analysis.

The input data is assumed to already be cleaned and formatted as a taxon abundance table.

## Future Improvements

- Add visualization of relative abundance
- Add stacked bar charts
- Add rarefaction curves
- Add beta diversity calculations
- Add distance matrix output
- Add group comparison statistics
- Add support for metadata files
- Add Streamlit dashboard version

## Resume Bullet

Built a Python microbiome analysis tool to parse abundance tables, calculate Shannon and Simpson diversity metrics, identify dominant taxa, compute relative abundance, and export reproducible CSV outputs.

## GitHub Description

A Python bioinformatics tool for microbiome abundance analysis, diversity metrics, relative abundance calculation, and CSV export.
