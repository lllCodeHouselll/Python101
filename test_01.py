# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:51:58 2018

@author: wuttinun_r
"""

import pandas as pd
url = "http://www.panphol.com/data/page/stockprice/ADVANC#"
data = pd.read_html(url)
#print(data[0])
print(data[0].iloc[0,1])