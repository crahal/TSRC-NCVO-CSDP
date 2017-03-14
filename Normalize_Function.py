# -*- coding: utf-8 -*-
"""
A function to normalize string names: apply to both registers and suppliers both.

Last updated: 14th March 2017
"""

def normaliseName(str,df_wordremove,df_wordreplace,df_grammar,df_stopwords):
	import re
	str = str or "Na"
	str = str.lower()                           
    ################################ Here we do the word replacers ################################ 
	for index, row in df_wordreplace.iterrows(): #should probably be df.apply() or df.map()?
		if row['replacethis'] in str: 
			str=str.replace(row['replacethis'], row['withthis'])

    ################################ Here we do the word removers ################################
	for index, row in df_wordremove.iterrows():
		if row['removethis'] in str: 
			str=str.replace(row['removethis'],"")
			
	################################ Here we do the grammar################################
	for index, row in df_grammar.iterrows():
		if row['replacethis'] in str: 
			str=str.replace(row['replacethis'],"")
	
	################################ Here we do the stopword removers ################################
	for index, row in df_stopwords.iterrows():
		if row['replacethis'] in str: 
			str=str.replace(row['replacethis']," ")
			
    ################################ Here we do some last minute regex stuff ################################
	str = str.replace('\n', ' ').replace('\r', '')
	preg_brackets = r'\([^)]*\)'                # regex expression for brackets
	str = re.sub( preg_brackets, "", str)       # replace any text in the brackets    
	str = str.replace("'","")                   # replace any apostrophes
	preg_nonalpha = r'[^a-zA-Z0-9 ]'            # regex expression to be sure we've removed any remaining non-alphabetic characters
	str = re.sub( preg_nonalpha, "", str)       # replace any non-alphanumeric characters with a space    
	str = str.strip()                           # trim to remove any trailing spaces left over from the word removal
	str = str.replace("  "," ")                  # remove any double spaces 
	str = ' '.join(str.split())	
	str=str or "Na"                             # if its a blank string output then it should spit out an Na
	return str                                  # return the normalised string
    
# A function to parse a company number into one that can be searched
# coynoText - the text to be parsed
def parseCoyno( coynoText ):
    coynoText = str( coynoText)
    if(coynoText=="" or coynoText=="0"):
        return ""
    coynoText = coynoText.strip()
    coynoText = coynoText.lstrip("0")
    coynoText = coynoText.rjust(8, "0")
    coynoText = coynoText[0:8]
    coynoText = coynoText.replace("000000NA","NA")
    coynoText = coynoText.replace("000000na","NA")
    coynoText = coynoText.replace("00000N/A","NA")
    coynoText = coynoText.replace("00000n/a","NA")
    return coynoText	