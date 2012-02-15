## No longer developed

## Description ==

Script parses Apache's access_log for specific method URL,
finds duplicate entries and sort them in the most frequent order.
Useful when you need to get all URLs from access_log.

## Usage

    ./script.py METHOD ORIGIN OUTPUT [REPETITION]

        == Parameters ==
    METHOD        which HTTP method to look for.
    ORIGIN        original file to parse.
    OUTPUT        output file to print to.
    REPETITION    optional. If set, script prints number of occurence before URL.

        == Example ==
    ./script.py GET access_log output_file TRUE
