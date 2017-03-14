# -*- coding: utf-8 -*-
"""
A function to count words in the input registers for the targetted approximate matching algorithms

Last updated: 14th March 2017
"""

def countthewords (register_input,typeofmatches):
    from tqdm import tqdm
    register_input = [b for b in register_input if isinstance(b, str)] #this is required because of some weird floats
    register_input=[words for segments in register_input for words in segments.split()] #this is required to split the variable words in the cells up
    uniques = []
    for word in tqdm(register_input,desc="Getting unique words for "+typeofmatches):
      if word not in uniques:
        uniques.append(word)        
    counts = []
    for unique in tqdm(uniques,desc="Counting unique words for "+typeofmatches):	
      count = 0              # Initialize the count to zero.
      for word in register_input:     # Iterate over the words.
        if word == unique:   # Is this word equal to the current unique?
          count += 1         # If so, increment the count
      counts.append((count, unique))
    counts.sort()            # Sorting the list puts the lowest counts first.
    counts.reverse()         # Reverse it, putting the highest counts first.
    return counts
