# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:13:31 2019

@author: alexn
"""
import pandas as pd
import numpy as np
import sys

"""
review.json file:
    685900 Lines
    
    columns = ['business_id', 'cool', 'date', 'funny', 'review_id', 'stars', 'text',
       'useful', 'user_id']
"""

def transform_data(filename, output,  iterations=10):
    data = pd.read_json(filename)
    convert_data = data[['stars', 'text']].dropna().sort_index()

    size =  convert_data.shape[0] / iterations    
    for i in range(iterations):
        convert_data[int(i*size):int((i+1)*size)].to_json(output + str(i) + '.json')
        

def chunk_data(filename, output):
    data = pd.read_json(filename, lines=True, chunksize = 100000)
    i = 0
    for chunks in data:
        chunks.to_json(output + str(i) + '.json')
        i += 1

def main():
    transform_data('review-0.json', 'review-0-')
    
if __name__ == "__main__":
    main()
    

