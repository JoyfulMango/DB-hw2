#!/bin/bash
rm *.dat
python3 parser.py ebay_data/items-*.json
