# -*- coding: utf-8 -*-
"""
Calcualte the best match on a register for an input list of suppliers using DSC
Last updated: 14th March 2017
"""

import os
import pandas as pd
import time
import numpy as np
from numba import autojit
from tqdm import tqdm


def approximatematch(dfinputlist, register, fastorfull, base_dir, dicecoefficientcutoff):
    filename = 'Registers\\registersforinput\\raw_' + register + '.tsv'
    dffullregister = pd.read_csv(os.path.join(
        base_dir, filename), header=None, sep='\t', encoding='latin-1', names=['raw_name'])
    mask = (dffullregister['raw_name'].astype('str').str.len() > 6)
    dffullregister = dffullregister.loc[mask]
    dffullregister = dffullregister.reset_index(drop=True)
    filename = 'ListsForPotentialMatches\\potential' + register + '.tsv'
    dflist = pd.read_csv(os.path.join(base_dir, filename), header=None,
                         sep='\t', encoding='latin-1', names=['keyword'])
    if fastorfull == 'fast':
        index = 0
        start = time.time()
        dfbestmatches = pd.DataFrame()
        for keyword in dflist['keyword']:
            index = index + 1
#            print('Now on keyword: '+keyword+ ' which is '+register+' word '+str(index)+' of '+str(len(dflist['keyword'].index)))
            try:
                dfinputlist_temp = dfinputlist[dfinputlist['raw_name'].str.contains(
                    keyword) == 1]
                dfinputlist_temp['norm_name'] = dfinputlist_temp['raw_name'].str.replace(
                    keyword, '')
                dfregister_temp = dffullregister[dffullregister['raw_name'].str.contains(
                    keyword) == True]
                dfregister_temp['norm_name'] = dfregister_temp['raw_name'].str.replace(
                    keyword, '')
                mask = (dfregister_temp['norm_name'].astype(
                    'str').str.len() > 5)
                dfregister_temp = dfregister_temp.loc[mask]
                dfregister_temp = dfregister_temp.reset_index(drop=True)
                tqdm.pandas(desc='Register: ' + register + '. Keyword: ' + keyword + ' (' + str(index) + ' of ' + str(
                    len(dflist.index)) + '). Total of ' + str(len(dfinputlist_temp.index)) + ' to find. Finished')
                dfbestmatches_temp = dfinputlist_temp.progress_apply(
                    applywrapper, args=(dfregister_temp,), axis=1)
                dfbestmatches = dfbestmatches.append(dfbestmatches_temp)
            except:
                pass
        print('Finished ' + register + ' fastmatch after ' +
              str(time.time() - start) + ' seconds!')
    else:
        start = time.time()
        dfbestmatches = dfinputlist.progress_apply(
            applywrapper, args=(dffullregister,), axis=1)
        print('Finished applying the fullmatch after ' +
              str(time.time() - start) + ' seconds!')
    dfbestmatches = dfbestmatches[dfbestmatches['bestscore']
                                  >= dicecoefficientcutoff]
    return dfbestmatches


def applywrapper(dfinputlist, dfregister):
    d = []
    dfregister_norm = pd.DataFrame(dfregister.ix[:, 'norm_name'])
    dfregister_raw = pd.DataFrame(dfregister.ix[:, 'raw_name'])
    if len(dfinputlist['norm_name']) > 5:
        d = [dice_coefficient(dfinputlist['norm_name'], dfregister_norm['norm_name'][indexx])
             for indexx, rows in dfregister_norm.itertuples()]
        dfinputlist['Best Match'] = dfregister_raw['raw_name'][d.index(max(d))]
        dfinputlist['Best Score'] = max(d)
    else:
        dfinputlist['Best Match'] = 'N/A'
        dfinputlist['Best Score'] = 0.0
    return pd.Series({'raw_name': dfinputlist['raw_name'], 'bestmatch': dfinputlist['Best Match'], 'bestscore': dfinputlist['Best Score']})


def dice_coefficient(a, b):
    #    try:
    #        if not len(a) or not len(b): return 0.0
    #    except:
    #        return 0.0
    # if a == b: return 1.0
    if abs(len(a) - len(b)) > 4:
        return 0.0
#    if len(a) == 1 or len(b) == 1: return 0.0

    a_bigram_list, b_bigram_list = dice_coefficient_sorting(a, b)
    score = dice_coefficient_scoring(a_bigram_list, b_bigram_list)

    return score


def dice_coefficient_sorting(a, b):
    a = np.array([ord(i) for i in a])
    b = np.array([ord(i) for i in b])
    a_bigram_list = 256 * a[:-1] + a[1:]
    b_bigram_list = 256 * b[:-1] + b[1:]
    a_bigram_list.sort()
    b_bigram_list.sort()
    return a_bigram_list, b_bigram_list


@autojit(nopython=True)
def dice_coefficient_scoring(a_bigram_list, b_bigram_list):

    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1
    score = float(matches) / float(lena + lenb)
    return score

# def parallelize_dataframe(df, func):
#    df_split = np.array_split(df, 2)
#    pool = Pool(4)
#    df = pd.concat(pool.map(func, df_split))
#    pool.close()
#    pool.join()
#    return df
