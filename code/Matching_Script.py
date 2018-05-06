# -*- coding: utf-8 -*-
"""
This is the master matching script which calls other normalized text inputs and last applies the targetted approximate matching technique

Last updated: 14th March 2017
"""
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
from tqdm import tqdm
import sys
sys.path.append('Approximate\\')
from Dice_Coefficient_Functions import approximatematch
base_dir = '\\Data'
fastorfull = 'fast'
dicecoefficientcutoff = 0.85
minnamelength = 4

if __name__ == "__main__":

    # Unique Suppliers
    supplier = pd.read_csv("raw_suppliers.tsv", sep='\t',
                           encoding='latin-1', names=['raw_name'], header=None)
    supplier['norm_name'] = pd.read_csv(
        "Data\\LAInputData\\UniqueRecipients\\norm_suppliers.tsv", sep='\t', encoding='latin-1', header=None)

    # Companies
    company = pd.read_csv("Registers\\registersforinput\\raw_company.tsv",
                          sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    company['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_company.tsv", sep='\t', encoding='latin-1', header=None)
    company = company.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, company, on=[
                        'raw_name'], how='left', indicator='Exact Company')
    supplier['Exact Company'] = np.where(
        supplier['Exact Company'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    company = company.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, company, on=[
                        'norm_name'], how='left', indicator='Norm Company')
    supplier['Norm Company'] = np.where(
        supplier['Norm Company'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Company Names')

    # Charities
    charity = pd.read_csv("Registers\\registersforinput\\raw_charity.tsv",
                          sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    charity['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_charity.tsv", sep='\t', encoding='latin-1', header=None)
    charity = charity.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, charity, on=[
                        'raw_name'], how='left', indicator='Exact Charity')
    supplier['Exact Charity'] = np.where(
        supplier['Exact Charity'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    charity = charity.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, charity, on=[
                        'norm_name'], how='left', indicator='Norm Charity')
    supplier['Norm Charity'] = np.where(
        supplier['Norm Charity'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Charity Names')

    # Health
    healthcare = pd.read_csv("Registers\\registersforinput\\raw_health.tsv",
                             sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    healthcare['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_health.tsv", sep='\t', encoding='latin-1', header=None)
    healthcare = healthcare.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, healthcare, on=[
                        'raw_name'], how='left', indicator='Exact Health')
    supplier['Exact Health'] = np.where(
        supplier['Exact Health'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    healthcare = healthcare.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, healthcare, on=[
                        'norm_name'], how='left', indicator='Norm Health')
    supplier['Norm Health'] = np.where(
        supplier['Norm Health'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Health Names')

    # Education
    education = pd.read_csv("Registers\\registersforinput\\raw_education.tsv",
                            sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    education['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_education.tsv", sep='\t', encoding='latin-1', header=None)
    education = education.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, education, on=[
                        'raw_name'], how='left', indicator='Exact Education')
    supplier['Exact Education'] = np.where(
        supplier['Exact Education'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    education = education.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, education, on=[
                        'norm_name'], how='left', indicator='Norm Education')
    supplier['Norm Education'] = np.where(
        supplier['Norm Education'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Education Names')

    # Sport
    sport = pd.read_csv("Registers\\registersforinput\\raw_sport.tsv",
                        sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    sport['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_sport.tsv", sep='\t', encoding='latin-1', header=None)
    sport = sport.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, sport, on=[
                        'raw_name'], how='left', indicator='Exact Sport')
    supplier['Exact Sport'] = np.where(
        supplier['Exact Sport'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    sport = sport.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, sport, on=[
                        'norm_name'], how='left', indicator='Norm Sport')
    supplier['Norm Sport'] = np.where(
        supplier['Norm Sport'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Sport Names')

    # Public
    public = pd.read_csv("Registers\\registersforinput\\raw_public.tsv",
                         sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    public['norm_name'] = pd.read_csv(
        "Registers\\registersforinput\\norm_public.tsv", sep='\t', encoding='latin-1', header=None)
    public = public.drop_duplicates(subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, public, on=[
                        'raw_name'], how='left', indicator='Exact Public')
    supplier['Exact Public'] = np.where(
        supplier['Exact Public'] == 'both', supplier['raw_name'], '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    public = public.drop_duplicates(subset=['norm_name'], keep=False)
    supplier = pd.merge(supplier, public, on=[
                        'norm_name'], how='left', indicator='Norm Public')
    supplier['Norm Public'] = np.where(
        supplier['Norm Public'] == 'both', supplier['raw_name_y'], '')
    supplier = supplier.drop('raw_name_y', 1)
    supplier.columns = supplier.columns.str.replace('_x', '')
    print('Exact Matching Raw and Normalized Public Names')

    # OpenCorporates
    opencorporatesapproximatematches = pd.read_csv("ApproximateMatches\\opencorporates_matches.csv", sep=',', encoding='latin-1', names=[
                                                   'raw_name', 'OpenCorporates_Match', 'OpenCorporates_URL', 'OpenCorporates_Score'], header=None)
    # shouldnt be, check anyway
    opencorporatesapproximatematches = opencorporatesapproximatematches.drop_duplicates(
        subset=['raw_name'], keep=False)
    supplier = pd.merge(supplier, opencorporatesapproximatematches, on=[
                        'raw_name'], how='left', indicator='OpenCorporates')
    supplier['OpenCorporates'] = np.where(
        supplier['OpenCorporates'] == 'both', supplier['raw_name'], '')
    supplier = supplier.replace(np.nan, '', regex=True)
    supplier = supplier.drop('OpenCorporates', 1)
    print('Bring In the OpenCorporates Matches Here')

    # print('Checking the List of Potential Forenames and Titles for Names Individuals')
    potentialtitles = pd.read_csv("ListsForPotentialMatches\\potentialtitles.tsv",
                                  sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    potentialforenames = pd.read_csv("ListsForPotentialMatches\\cleanedforenames.tsv",
                                     sep='\t', encoding='latin-1', names=['raw_name'], header=None)
    supplier['Forename'] = ""
    supplier['Title'] = ""
    for row in supplier.itertuples():
    if supplier['Exact Company'][row[0]] == '' and supplier['Norm Company'][row[0]] == '' and supplier['Exact Charity'][row[0]] == '' and supplier['Norm Charity'][row[0]] == '' and supplier['Exact Health'][row[0]] == '' and supplier['Norm Health'][row[0]] == '' and supplier['Exact Education'][row[0]] == '' and supplier['Norm Education'][row[0]] == '' and supplier['Exact Public'][row[0]] == '' and supplier['Norm Public'][row[0]] == '' and supplier['Exact Sport'][row[0]] == '' and supplier['Norm Sport'][row[0]] == '' and supplier['OpenCorporates_Match'][row[0]] == '':
    for roww in potentialtitles.itertuples():
    if potentialtitles['raw_name'][roww[0]] in supplier['raw_name'][row[0]]:
        supplier['Title'][row[0]] = potentialtitles['raw_name'][roww[0]]
    break
    for roww in potentialforenames.itertuples():
        if len(potentialforenames['raw_name'][roww[0]]) >= minnamelength:
            if potentialforenames['raw_name'][roww[0]] in supplier['raw_name'][row[0]]:
                supplier['Forename'][row[0]
                                     ] = potentialforenames['raw_name'][roww[0]]
                break
-
    unmatchedsuppliers = supplier[(supplier['Exact Company'] == '') & (supplier['Norm Company'] == '') & (supplier['Exact Charity'] == '') & (supplier['Norm Charity'] == '') & (supplier['Exact Health'] == '') & (supplier['Norm Health'] == '') & (supplier['Exact Public'] == '') & (
        supplier['Norm Public'] == '') & (supplier['Exact Education'] == '') & (supplier['Norm Education'] == '') & (supplier['Exact Sport'] == '') & (supplier['Norm Sport'] == '') & (supplier['OpenCorporates_Match'] == '') & (supplier['Forename'] == '') & (supplier['Title'] == '')]
    unmatchedsuppliers = pd.DataFrame(unmatchedsuppliers['raw_name'])

    approxmatches_company = approximatematch(
        unmatchedsuppliers, 'company', fastorfull, base_dir, dicecoefficientcutoff)
    approxmatches_public = approximatematch(
        unmatchedsuppliers, 'public', fastorfull, base_dir, dicecoefficientcutoff)
    approxmatches_education = approximatematch(
        unmatchedsuppliers, 'education', fastorfull, base_dir, dicecoefficientcutoff)
    approxmatches_sport = approximatematch(
        unmatchedsuppliers, 'sport', fastorfull, base_dir, dicecoefficientcutoff)
    approxmatches_health = approximatematch(
        unmatchedsuppliers, 'health', fastorfull, base_dir, dicecoefficientcutoff)
    approxmatches_charity = approximatematch(
        unmatchedsuppliers, 'charity', fastorfull, base_dir, dicecoefficientcutoff)

    supplier = pd.merge(supplier, approxmatches_company, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Company', 'bestscore': 'Approx_Company_Score'})

    supplier = pd.merge(supplier, approxmatches_charity, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Charity', 'bestscore': 'Approx_Charity_Score'})

    supplier = pd.merge(supplier, approxmatches_health, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Health', 'bestscore': 'Approx_Charity_Health'})

    supplier = pd.merge(supplier, approxmatches_education, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Education', 'bestscore': 'Approx_Education_Score'})

    supplier = pd.merge(supplier, approxmatches_public, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Public', 'bestscore': 'Approx_Public_Score'})

    supplier = pd.merge(supplier, approxmatches_sport, on=[
                        'raw_name'], how='left', indicator='matchtype')
    supplier.columns = supplier.columns.str.replace('_x', '')
    supplier = supplier.drop('norm_name_y', 1)
    supplier = supplier.drop('matchtype', 1)
    supplier = supplier.rename(
        columns={'bestmatch': 'Approx_Sport', 'bestscore': 'Approx_Sport_Score'})

    supplier = supplier.replace(np.nan, '', regex=True)

    unmatchedsuppliers = supplier[(supplier['Exact Company'] == '') & (supplier['Norm Company'] == '') & (supplier['Exact Charity'] == '') & (supplier['Norm Charity'] == '') & (supplier['Exact Health'] == '') & (supplier['Norm Health'] == '') & (supplier['Exact Public'] == '') & (
        supplier['Norm Public'] == '') & (supplier['Exact Education'] == '') & (supplier['Norm Education'] == '') & (supplier['Exact Sport'] == '') & (supplier['Norm Sport'] == '') & (supplier['OpenCorporates_Match'] == '') & (supplier['Forename'] == '') & (supplier['Title'] == '')]
    unmatchedsuppliers = pd.DataFrame(unmatchedsuppliers['raw_name'])
    unmatchedsuppliers.to_csv("ForAnalysis\\UnmatchedUniqueSuppliers.csv")

    supplier.to_csv("MatchedUniqueSuppliers.csv")
