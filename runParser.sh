#!/bin/bash
rm *.dat
python3 auction_parser.py ebay_data/items-*.json
