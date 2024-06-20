#!/bin/bash

# Define the data directory
DATA_DIR="data"

# Function to create a directory if it doesn't exist
create_directory() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Directory $dir created."
    else
        echo "Directory $dir already exists."
    fi
}

# Function to download a file if it doesn't exist
download_file() {
    local url=$1
    local output_dir=$2
    local file_name=$(basename "$url")
    if [ ! -f "$output_dir/$file_name" ]; then
        wget -P "$output_dir" "$url"
        echo "Downloaded $file_name."
    else
        echo "$file_name already exists in $output_dir."
    fi
}

# Function to unzip a file if it hasn't been unzipped
unzip_file() {
    local zip_file=$1
    local output_dir=$2
    if [ -f "$zip_file" ]; then
        unzip -n "$zip_file" -d "$output_dir"
        echo "Unzipped $zip_file into $output_dir."
    else
        echo "$zip_file does not exist."
    fi
}

# Create the data directory
create_directory "$DATA_DIR"

# Download the datasets
download_file "http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz" "$DATA_DIR"
download_file "http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/nerf_example_data.zip" "$DATA_DIR"

# Unzip the example data
unzip_file "$DATA_DIR/nerf_example_data.zip" "$DATA_DIR"
