# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 22:32:25 2015

@author: Ivan.Liuyanfeng
"""
from datetime import datetime
from csv import DictReader
import pandas as pd

pred_file1 = 'pred/blending/ftrl_5_2.5_2.5_0.3915902.csv'
pred_file2 = 'pred/blending/libFM_0.4027643.csv'  
pred_file3 = 'pred/blending/nn_60_80_0.3957782.csv'  
pred_file4 = 'pred/blending/xgboost_900_03_0.3931970.csv' 
#pred_file5 = 'pred/blending/NN_NN_0.3957782.csv'   
#pred_file6 = 'pred/blending/libLinear_logreg_dual_0.3987665.csv'   

pred_2 = {}
for t, row in enumerate(DictReader(open(pred_file2))): # site/app
    pred_2[row['id']] = row['click']

pred_3 = {}
for t, row in enumerate(DictReader(open(pred_file3))): # site/app
    pred_3[row['id']] = row['click']

pred_4 = {}
for t, row in enumerate(DictReader(open(pred_file4))): # site/app
    pred_4[row['id']] = row['click']
'''
pred_5 = {}
for t, row in enumerate(DictReader(open(pred_file5))): # site/app
    pred_5[row['id']] = row['click']
    
pred_6 = {}
for t, row in enumerate(DictReader(open(pred_file6))): # site/app
    pred_6[row['id']] = row['click']
'''

start = datetime.now()
with open('Blending_models_FTRL_FM_XG_NN86.csv',"wb") as outfile:
    outfile.write('id,click\n')
    for t, row in enumerate(DictReader(open(pred_file1))):
        
        ID = row['id']
        click = row['click']
        #if(float(pred_5[ID])==0):
        #    pred_5[ID]=0.0000000001
        click = 4/(1/float(click)+1/float(pred_2[ID])+1/float(pred_3[ID])+1/float(pred_4[ID]))#+1/float(pred_5[ID]))
        #click = 0.3*(0.7*float(click)+0.3*float(pred_2[ID])) + 0.3*float(pred_3[ID]) + 0.2*float(pred_3[ID]) + 0.2*float(pred_5[ID])
        
        outfile.write('%s,%s\n' % (str(ID), str(click)))
        
        if t % 100000 == 0:
            print("%s\t%s"%(t, str(datetime.now() - start)))