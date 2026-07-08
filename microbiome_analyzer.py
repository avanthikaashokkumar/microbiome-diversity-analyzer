import argparse
import csv
import math
from pathlib import Path


def read_abundance_table(file_path):
    """
    Reads a microbiome abundance table.

    Expected format:
    taxon,sample_A,sample_B,sample_C
    Bacteroides,120,80,10
    Lactobacillus,20,100,60
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if "taxon" not in reader.fieldnames:
            raise ValueError("CSV must include a 'taxon' column.")

        sample_names = [name for name in reader.fieldnames if name != "taxon"]

        data = []
        for row in reader:
            taxon = row["taxon"].strip()

            counts = {}
            for sample in sample_names:
                try:
                    counts[sample] = int(row[sample])
                except ValueError:
                    counts[sample] = 0

            data.append({
                "taxon": taxon,
                "counts": counts
            })

    return data, sample_names


def calculate_sample_metrics(data, sample_name):
    counts = [record["counts"][sample_name] for record in data]
    total_reads = sum(counts)

    if total_reads == 0:
        return {
            "sample": sample_name,
            "total_reads": 0,
            "observed_taxa": 0,
            "shannon_index": 0,
            "simpson_index": 0,
            "evenness": 0,
            "top_taxon": "None",
            "top_taxon_percent": 0
        }

    observed_taxa = sum(1 for count in counts if count > 0)

    proportions = [
        count / total_reads
        for count in counts
        if count > 0
    ]

    shannon_index = -sum(p * math.log(p) for p in proportions)
    simpson_index = 1 - sum(p ** 2 for p in proportions)

    if observed_taxa > 1:
        evenness = shannon_index / math.log(observed_taxa)
    else:
        evenness = 0

    top_record = max(data, key=lambda record: record["counts"][sample_name])
    top_taxon_count = top_record["counts"][sample_name]
    top_taxon_percent = (top_taxon_count / total_reads) * 100

    return {
        "sample": sample_name,
        "total_reads": total_reads,
        "observed_taxa": observed_taxa,
        "shannon_index": round(shannon_index, 4),
        "simpson_index": round(simpson_index, 4),
        "evenness": round(evenness, 4),
        "top_taxon": top_record["taxon"],
        "top_taxon_percent": round(top_taxon_percent, 2)
    }


def calculate_relative_abundance(data, sample_names):
    relative_rows = []

    sample_totals = {
        sample: sum(record["counts"][sample] for record in data)
        for sample in sample_names
    }

    for record in data:
        row = {"taxon": record["taxon"]}

        for sample in sample_names:
            total = sample_totals[sample]

            if total == 0:
                row[sample] = 0
            else:
                row[sample] = round((record["counts"][sample] / total) * 100, 4)

        relative_rows.append(row)

    return relative_rows


def write_metrics_csv(metrics, output_path):
    fieldnames = [
        "sample",
        "total_reads",
        "observed_taxa",
        "shannon_index",
        "simpson_index",
        "evenness",
        "top_taxon",
        "top_taxon_percent"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics)


def write_relative_abundance_csv(relative_rows, sample_names, output_path):
    fieldnames = ["taxon"] + sample_names

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(relative_rows)


def print_report(metrics):
    print("\nMicrobiome Diversity Analysis Report")
    print("=" * 45)

    for result in metrics:
        print(f"\nSample: {result['sample']}")
        print("-" * 45)
        print(f"Total Reads: {result['total_reads']}")
        print(f"Observed Taxa: {result['observed_taxa']}")
        print(f"Shannon Diversity Index: {result['shannon_index']}")
        print(f"Simpson Diversity Index: {result['simpson_index']}")
        print(f"Evenness: {result['evenness']}")
        print(f"Most Abundant Taxon: {result['top_taxon']}")
        print(f"Most Abundant Taxon Percent: {result['top_taxon_percent']}%")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze microbiome abundance data from a CSV file."
    )

    parser.add_argument(
        "input",
        help="Path to microbiome abundance CSV file."
    )

    parser.add_argument(
        "--metrics-output",
        default="diversity_metrics.csv",
        help="Output CSV file for sample diversity metrics."
    )

    parser.add_argument(
        "--relative-output",
        default="relative_abundance.csv",
        help="Output CSV file for relative abundance values."
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Error: Could not find input file: {input_path}")
        return

    try:
        data, sample_names = read_abundance_table(input_path)
    except ValueError as error:
        print(f"Error: {error}")
        return

    if not data:
        print("Error: No taxon rows found in the input file.")
        return

    metrics = [
        calculate_sample_metrics(data, sample)
        for sample in sample_names
    ]

    relative_rows = calculate_relative_abundance(data, sample_names)

    print_report(metrics)

    write_metrics_csv(metrics, args.metrics_output)
    write_relative_abundance_csv(relative_rows, sample_names, args.relative_output)

    print(f"\nDiversity metrics saved to: {args.metrics_output}")
    print(f"Relative abundance table saved to: {args.relative_output}")


if __name__ == "__main__":
    main()
