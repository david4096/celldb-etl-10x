"""
CLI entrypoint to ten etl commands
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse

def main(args=None):
    parser = argparse.ArgumentParser(
        description='Add 10xgenomics data to celldb')
    parser.add_argument(
        "--port", "-P", default=8000, type=int,
        help="The port to listen on")
    print(parser.parse_args(args))
