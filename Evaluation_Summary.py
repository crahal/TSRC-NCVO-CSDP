# -*- coding: utf-8 -*-
"""
Evaluates the performance of the matching script

Last updated: 14th March 2017
"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
#import time
import sys
#import os.path
sys.path.append('Code\\Approximate\\')
base_dir = '\\Data'
fastorfull = 'fast'
dicecoefficientcutoff=0.85
minnamelength=4

if __name__ == "__main__":
	suppliermatched=pd.read_csv("Data\ForAnalysis\MatchedUniqueSuppliers.csv",sep=',',encoding='latin-1')
	columns=['Matched Individual Payments','Matched Unique Suppliers','Total Amount Matched','Average Matched Payment']
	rows=['Company','Charity','Health','Public','Education','Sport','Individ','Unmatched']
	outputdf=pd.DataFrame(index=rows,columns=columns)

	outputdf['Matched Unique Suppliers']['Company']=len(suppliermatched[suppliermatched['Exact Company'].notnull() | suppliermatched['Norm Company'].notnull() | suppliermatched['Approx_Education'].notnull() | suppliermatched['OpenCorporates_Match'].notnull()])
	outputdf['Matched Unique Suppliers']['Charity']=len(suppliermatched[suppliermatched['Exact Charity'].notnull() | suppliermatched['Norm Charity'].notnull() | suppliermatched['Approx_Charity'].notnull()])
	outputdf['Matched Unique Suppliers']['Health']=len(suppliermatched[suppliermatched['Exact Health'].notnull() | suppliermatched['Norm Health'].notnull() | suppliermatched['Approx_Health'].notnull()])
	outputdf['Matched Unique Suppliers']['Public']=len(suppliermatched[suppliermatched['Exact Public'].notnull() | suppliermatched['Norm Public'].notnull() | suppliermatched['Approx_Public'].notnull()])
	outputdf['Matched Unique Suppliers']['Education']=len(suppliermatched[suppliermatched['Exact Education'].notnull() | suppliermatched['Norm Education'].notnull() | suppliermatched['Approx_Education'].notnull()])
	outputdf['Matched Unique Suppliers']['Sport']=len(suppliermatched[suppliermatched['Exact Sport'].notnull() | suppliermatched['Norm Sport'].notnull() | suppliermatched['Approx_Sport'].notnull()])
	outputdf['Matched Unique Suppliers']['Individ']=len(suppliermatched[suppliermatched['Forename'].notnull() | suppliermatched['Title'].notnull()])
	outputdf['Matched Unique Suppliers']['Unmatched']=len(suppliermatched[suppliermatched['Exact Company'].isnull() & 
	suppliermatched['Norm Company'].isnull() &  
	suppliermatched['Exact Charity'].isnull() &  
	suppliermatched['Norm Charity'].isnull() &  
	suppliermatched['Exact Health'].isnull() &  
	suppliermatched['Norm Health'].isnull() &  
	suppliermatched['Exact Education'].isnull() &  
	suppliermatched['Norm Education'].isnull() &  
	suppliermatched['Exact Sport'].isnull() &  
	suppliermatched['Norm Sport'].isnull() &  
	suppliermatched['Exact Public'].isnull() &  
	suppliermatched['Norm Public'].isnull() &  
	suppliermatched['OpenCorporates_Match'].isnull() &  
	suppliermatched['Forename'].isnull() &  
	suppliermatched['Title'].isnull() &  
	suppliermatched['Approx_Company'].isnull() &  
	suppliermatched['Approx_Charity'].isnull() &  
	suppliermatched['Approx_Health'].isnull() &  
	suppliermatched['Approx_Education'].isnull() &  
	suppliermatched['Approx_Public'].isnull() &  
	suppliermatched['Approx_Sport'].isnull() &  
	suppliermatched['Approx_Education'].isnull()])

	payments=pd.read_csv("allpayments.tsv",sep='\t',encoding='latin-1')
	payments=pd.merge(payments,suppliermatched, on=['raw_beneficiary'], how='left', indicator=False)

	tempdf=payments[payments['Exact Company'].notnull() | payments['Norm Company'].notnull() | payments['Approx_Company'].notnull() | payments['OpenCorporates_Match'].notnull()]
	outputdf['Matched Individual Payments']['Company']=len(tempdf)
	outputdf['Total Amount Matched']['Company']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Company']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Charity'].notnull() | payments['Norm Charity'].notnull() | payments['Approx_Charity'].notnull()]
	outputdf['Matched Individual Payments']['Charity']=len(tempdf)
	outputdf['Total Amount Matched']['Charity']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Charity']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Health'].notnull() | payments['Norm Health'].notnull() | payments['Approx_Health'].notnull()]
	outputdf['Matched Individual Payments']['Health']=len(tempdf)
	outputdf['Total Amount Matched']['Health']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Health']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Public'].notnull() | payments['Norm Public'].notnull() | payments['Approx_Public'].notnull()]
	outputdf['Matched Individual Payments']['Public']=len(tempdf)
	outputdf['Total Amount Matched']['Public']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Public']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Education'].notnull() | payments['Norm Education'].notnull() | payments['Approx_Education'].notnull()]
	outputdf['Matched Individual Payments']['Education']=len(tempdf)
	outputdf['Total Amount Matched']['Education']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Education']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Sport'].notnull() | payments['Norm Sport'].notnull() | payments['Approx_Sport'].notnull()]
	outputdf['Matched Individual Payments']['Sport']=len(tempdf)
	outputdf['Total Amount Matched']['Sport']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Sport']=tempdf['amount'].mean()

	tempdf=payments[payments['Forename'].notnull() | payments['Title'].notnull()]
	outputdf['Matched Individual Payments']['Individ']=len(tempdf)
	outputdf['Total Amount Matched']['Individ']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Individ']=tempdf['amount'].mean()

	tempdf=payments[payments['Exact Company'].isnull() & 
	payments['Norm Company'].isnull() &  
	payments['Exact Charity'].isnull() &  
	payments['Norm Charity'].isnull() &  
	payments['Exact Health'].isnull() &  
	payments['Norm Health'].isnull() &  
	payments['Exact Education'].isnull() &  
	payments['Norm Education'].isnull() &  
	payments['Exact Sport'].isnull() &  
	payments['Norm Sport'].isnull() &  
	payments['Exact Public'].isnull() &  
	payments['Norm Public'].isnull() &  
	payments['OpenCorporates_Match'].isnull() &  
	payments['Forename'].isnull() &  
	payments['Title'].isnull() &  
	payments['Approx_Company'].isnull() &  
	payments['Approx_Charity'].isnull() &  
	payments['Approx_Health'].isnull() &  
	payments['Approx_Education'].isnull() &  
	payments['Approx_Public'].isnull() &  
	payments['Approx_Sport'].isnull() &  
	payments['Approx_Education'].isnull()]
	outputdf['Matched Individual Payments']['Unmatched']=len(tempdf)
	outputdf['Total Amount Matched']['Unmatched']=tempdf['amount'].sum()
	outputdf['Average Matched Payment']['Unmatched']=tempdf['amount'].mean()

	outputdf.to_csv("MatchEvaluation.csv")