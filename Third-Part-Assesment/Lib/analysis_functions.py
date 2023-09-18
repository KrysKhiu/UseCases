import pandas as pd
import os
import numpy as np
import scipy
from scipy.stats import f_oneway
from scipy.stats import pearsonr
from sklearn.metrics import mutual_info_score
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt 
import math
import seaborn as sns



class PlotFunctions:
    def __init__(self):
        self
    
    def histogram_plots(self, columns_to_plot, super_title, x_lim, y_lim):
        # set number of rows and number of columns
        number_of_columns = 2
        number_of_rows = math.ceil(len(columns_to_plot)/2)
    
        # create a figure
        fig = plt.figure(figsize=(24, 5 * number_of_rows)) 
        fig.suptitle(super_title, fontsize=22,  y=.95)
     
    
        # loop to each demographic column name to create a subplot
        for index, column in enumerate(columns_to_plot, 1):
    
            # create the subplot
            ax = fig.add_subplot(number_of_rows, number_of_columns, index)
    
            # histograms for each class (normalized histogram)
            df_join_freq_sev[df_join_freq_sev['FlagClaim']== 0][column].plot(kind='hist', ax=ax, density=True, 
                                                           alpha=0.5, color='springgreen', label='No')
            df_join_freq_sev[df_join_freq_sev['FlagClaim']== 1][column].plot(kind='hist', ax=ax, density=True,
                                                            alpha=0.5, color='salmon', label='Yes')
            
            # set the legend in the upper right corner
            ax.legend(loc="upper right", bbox_to_anchor=(0.5, 0.5, 0.5, 0.5),
                      title='WithClaims', fancybox=True)
    
            # set title and labels
            ax.set_title('Distribution of ' + column + ' by churn',
                         fontsize=16, loc='left')
    
            ax.tick_params(rotation='auto')
            
            if len(y_lim) > 0:
                plt.ylim(y_lim[0], y_lim[1])
                
            if len(x_lim) > 0:
                plt.xlim(x_lim[0], x_lim[1])
            
            # eliminate the frame from the plot
            spine_names = ('top', 'right', 'bottom', 'left')
            for spine_name in spine_names:
                ax.spines[spine_name].set_visible(False)
    
    def percentage_stacked_plot(self, columns_to_plot, super_title, x_lim, y_lim):
        number_of_columns = 2
        number_of_rows = math.ceil(len(columns_to_plot)/2)
        
        # create a figure
        fig = plt.figure(figsize=(12, 5 * number_of_rows)) 
        fig.suptitle(super_title, fontsize=22,  y=.95)
         
        if len(columns_to_plot) == 1:
            fig = plt.figure(figsize=(24, 5 * number_of_rows)) 
            fig.suptitle(super_title, fontsize=22,  y=.95)
    
        # loop to each column name to create a subplot
        for index, column in enumerate(columns_to_plot, 1):
    
            # create the subplot
            ax = fig.add_subplot(number_of_rows, number_of_columns, index)
    
            # calculate the percentage of observations of the response variable for each group of the independent variable
            # 100% stacked bar plot
            prop_by_independent = pd.crosstab(df_join_freq_sev[column], df_join_freq_sev['FlagClaim']).apply(lambda x: x/x.sum()*100, axis=1)
    
            prop_by_independent.plot(kind='bar', ax=ax, stacked=True,
                                     rot=0, color=['springgreen','salmon'])
            
            # set the legend in the upper right corner
            ax.legend(loc="upper right", bbox_to_anchor=(0.62, 0.5, 0.5, 0.5),
                      title='With a Claim', fancybox=True)
    
            # set title and labels
            ax.set_title('Proportion of observations by ' + column,
                         fontsize=10, loc='left')
    
            ax.tick_params(rotation='auto')
            
            if len(y_lim) > 0:
                plt.ylim(y_lim[0], y_lim[1])
                
            if len(x_lim) > 0:
                plt.xlim(x_lim[0], x_lim[1])
            
            # eliminate the frame from the plot
            spine_names = ('top', 'right', 'bottom', 'left')
            for spine_name in spine_names:
                ax.spines[spine_name].set_visible(False)




