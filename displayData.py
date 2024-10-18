import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def computeLoehne(inputData): 
    dfData = pd.DataFrame(inputData)
    dfData["BerufserfahrungJahre"] = dfData["Berufserfahrung"] / 12
    dfData["Monatsbrutto"] = dfData["Gesamtjahresbrutto"] / 12
    print(dfData["Monatsbrutto"].min())
    sns.scatterplot( data = dfData, x="BerufserfahrungJahre", y="Gesamtjahresbrutto")

    plt.ylim(0, 200000)  # Y-Achse auf max. 200.000 € begrenzen

    plt.show()