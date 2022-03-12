import matplotlib.pyplot as plt, seaborn as sns
import pandas as pd, numpy as np

def PlotNaNs( X ):
    nans = X.isna().sum().sort_values(ascending=False) / X.shape[0]
    nans = nans[nans > 0]
    fig, ax = plt.subplots(figsize=(10, 6))
    # ax.grid()
    ax.bar(nans.index, nans.values, zorder=2, color="#3f72af")
    ax.set_ylabel("Percentage of missing values", labelpad=10)
    ax.set_xlim(-0.6, len(nans) - 0.4)
    ax.xaxis.set_tick_params(rotation=90)
    plt.show()
# CountNaN( df_train )

def PlotFeaturesCorrelation( 
        df_train, drops=None, 
        vmax=1, vmin=-1, cmap='PiYG' 
):
    if drops == None: drops = []
    corr_mat = df_train.corr()
    corr_mat = corr_mat.drop(drops)
    corr_mat = corr_mat.drop(drops, axis=1)
    
    f, ax = plt.subplots(figsize=(12, 9))

    sns.heatmap(corr_mat, vmax=vmax, vmin=vmin, cmap=cmap, square=True, annot=True)

    plt.suptitle('Correlatation Feature HeatMap')
    plt.xlabel('Features')
    plt.ylabel('Features')
    
def PlotCorrelationToResult( 
        df_train, y_name, 
        drops=None, ascending=True 
):
    if drops == None: 
        drops = []
    drops.append(y_name)
    correlations = df_train.corr()[y_name]
    correlations = correlations.drop( drops )
    correlations_sorted_indices = abs(correlations).sort_values(ascending=ascending).index
    correlations = correlations[correlations_sorted_indices]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(
        correlations.index, 
        correlations.values, 
        zorder=2, color="#3070a0"
    )
    ax.set_ylabel(f"Correlation to {y_name}", labelpad=10)
    
def Plot_ShowFigures(x,y,y_max, y_pos):
    for i in range(len(x)):
        plt.text(i, max(0,y_pos[i]), str(y[i])+'/'+str(y_max[i]), ha = 'center')
def PlotFeatureGroups( 
    X, feature_name, y_name, gap=1, 
    plot=lambda x,y: plt.bar(x, y), show_figures=True, 
    count_name='Count', figsize=(13,6), xlabel='', ylabel='' 
):

    Grouped = X.groupby(
            pd.cut(
                X[feature_name], np.arange(0, X[feature_name].max()+gap, gap)
            )
        ).sum()
    
    fig, ax = plt.subplots( figsize=figsize )
    plot(
        range(Grouped[feature_name].shape[0]),
        Grouped[y_name] / Grouped[count_name],
    )
    # ax.grid()
    # plt.xlabel(feature_name)
    if show_figures:
        # -- Custom x-axis values
        plt.xticks(
            range(Grouped[feature_name].shape[0]), 
            Grouped.index,
        )
    if show_figures:
        # -- show result/total on bar e.g. '3/5'
        Plot_ShowFigures(
            range(Grouped[feature_name].shape[0]),
            Grouped[y_name], Grouped[count_name],
            Grouped[y_name] / Grouped[count_name]
        )
    
    if xlabel == '':
        xlabel = feature_name
    plt.xlabel(xlabel, fontsize=30)
    plt.ylabel(ylabel, fontsize=30)
    return Grouped
    
