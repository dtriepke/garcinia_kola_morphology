import numpy as np
import pandas as pd

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline

# Import the 3 dimensionality reduction methods
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


# Import Data
FILE = "Garcinia kola\Morphology\Final-database_Manourova_MSc.xlsx"
SHEET = "MERGE"
data = pd.read_excel(FILE, sheet_name = SHEET, header = [0])


# Select Targets and Train
region_id = data["Region"]
tree_id = data["Tree ID"]
tree_fruit_id = data["Tree ID"].astype(str) + '_'+ data["Fruit ID"].astype(str)





# Missing Values
train.isnull().sum()


#GPS
# -*- coding: latin-1 -*-

def conversion(old):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0,0,0])
    return (int(new[0])+int(new[1])/60.0+int(new[2])/3600.0) * direction[new_dir]

lat, lon = u'''0°25'30"S, 91°7'W'''.split(', ')
print(conversion(lat), conversion(lon))

data.GPS[0]



