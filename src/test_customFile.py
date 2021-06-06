# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:34:52 2021

"""
#import libraries
from fuzzysearch import find_near_matches
import time

#extract answer from return value
def extract_answer(string):
    s_idx = -2
    e_idx = -2
    
    while(string[s_idx] != '='):
        s_idx -= 1
    
    return string[s_idx+2 : e_idx]

#extract word position in text
def extract_position(string):
    
    idx = 13
    s_idx = string[12]
    while string[idx] != ',':
        s_idx += string[idx]
        idx += 1
    
    idx = idx+6
    e_idx = string[idx]
    idx = idx+1
    while string[idx] != ',':
        e_idx += string[idx]
        idx += 1
    
    
    return s_idx, e_idx

#print answer in a readable format
def print_answer(ans):
    
    n = len(ans)
    for i in range(0,n):
        
        x = extract_answer(str(ans[i]))
        s, e = extract_position(str(ans[i]))
        
        print(str(i+1) + ".", x, "\tPosition: ", s + "->" + e)
        
#perform fuzzy search over variable levenshtein distance(l)
def fuzzy_search(keyword, src_path):
    
    tic = time.perf_counter()
    #define a variable l distance
    l = 0
    
    src = open(src_path, 'r').read()
    
    answer = find_near_matches(keyword, src, max_l_dist=l)
    
    while(len(answer) == 0 and l <= 5):
        l = l+1
        answer = find_near_matches(keyword, src, max_l_dist=l)
    
    if l > 5:
        print("No suitable matches found!")
        exit()
    
    toc = time.perf_counter()
        
    print("############################")
    print("Printing Matched queries for: ", keyword, )
    print("Levenshtein Distance = ", l, )
    print("Total characters scanned: ", len(src), )
    print(f"Time taken for execution: {toc - tic:0.2f} seconds", )
    print("############################")
    print_answer(answer)
    print("############################")

#############################################################
#execution
#fuzzy_search(keyword_string, path of text file)

filename = input("Enter the filename (eg: largeText.txt): ")

keyword = input("Enter the keyword: ")

fuzzy_search(keyword, filename)

############################################################
############################################################
############################################################
############################################################