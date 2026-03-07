#!/usr/bin/env bash

set -euo pipefail

SOURCE_DIR="${1:-}"
OUTPUT_FILE="${2:-}"

if [[ -z "$SOURCE_DIR" || -z "$OUTPUT_FILE" ]]; then
    echo "Usage: $0 <source_dir> <output_file>" >&2
    exit 1
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
    echo "Source directory '$SOURCE_DIR' not found, skipping."
    exit 0
fi

OUTPUT_DIR="$(dirname "$OUTPUT_FILE")"
if [[ ! -d "$OUTPUT_DIR" ]]; then
    mkdir -p "$OUTPUT_DIR"
    echo "Created directory: $OUTPUT_DIR"
fi

find "$SOURCE_DIR" -maxdepth 1 -type f -printf "%f\n" | sort > "$OUTPUT_FILE"

echo "Done. File list written to: $OUTPUT_FILE"
