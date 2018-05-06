# -*- coding: utf-8 -*-
"""
-Decompose payments to charitable recipients across NUTS3 regions
-
-Last updated: 14th March 2017
-"""

import pandas as pd
import numpy as np
from tqdm import tqdm

payments = pd.read_csv(
    "Data\\LAInputData\\MergedOutputs\\allpayments.tsv", sep='\t', encoding='latin-1')
latonutslookup = pd.read_csv(
    "Data\\ForAnalysis\\latonutslookup.csv", sep=',', encoding='latin-1')
payments = pd.read_csv(
    "Data\\LAInputData\\MergedOutputs\\allpayments.tsv", sep='\t', encoding='latin-1')
payments = pd.merge(payments, latonutslookup, on=[
                    'provider'], how='left', indicator=False)
df2 = pd.read_csv("Data\\ForAnalysis\\Charity_Payments_Only.csv",
                  sep=',', encoding='latin-1')
df2 = pd.merge(df2, latonutslookup, on=[
               'provider'], how='left', indicator=False)

uniqueproviders = df2['Nuts3'].unique()
df = pd.DataFrame()
counter = 0
for provider in tqdm(uniqueproviders):
    df1 = df2
    df3 = payments
    df1 = df1[df1['Nuts3'] == str(provider)]
    df3 = df3[df3['Nuts3'] == str(provider)]
if df1.empty is False:
    temp = pd.DataFrame({'Nuts3': provider, '# Charity Payments': [len(df1.index)],
                         'Charity Value (£m)': np.sum(df3['amount']) / 1000000,
                         'Percent to Charity by Value': (np.sum(df1['amount']) / np.sum(df3['amount'])) * 100,
                         'Percent to Charity by Volume': (len(df1['amount']) / len(df3['amount'])) * 100})
    df = pd.concat([df, temp])
df = df[['Nuts3', '# Charity Payments',
         'Charity Value (£m)', 'Percent to Charity by Value', 'Percent to Charity by Volume']]

df.to_csv("Compile\\Charity_Payments_By_Nuts3.csv", index=False)
