import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import random

from prime_factors import *

#Overall title
st.sidebar.title("Prime Palette")

#Sidebar title

#Pick a number
st.sidebar.write('Choose the range of numbers to visualize:')
chosen_num = st.sidebar.slider('', 2, 100, 50)

num_prime_df = prime_df(chosen_num)
unique_primes = num_prime_df.Primes.unique()

#Pick a color
#Streamlit's sharing deployment currently d/n allow choosing color values
#st.sidebar.write("Chooose two colors for your visualization")
#chosen_color_1 = st.sidebar.color_picker("Click square below to pick the first color:")
#st.sidebar.write(chosen_color_1)
#chosen_color_2 = st.sidebar.color_picker("Click square below to pick the second color:")
#st.sidebar.write(chosen_color_2)

#Switch up colors
color_pairs = [['#06770a', '#fbee04'], ['#0416f7', '#fb7d04'], ['#a6b1f1', '#fb04f7'], ['#e25e71', '#fbe984'],['#38b777','#c448ef']]

#st.sidebar.write("Switch up the colors for your visualization")
push_or_not = st.sidebar.button('Click here to switch up the colors!')

if push_or_not == True:
    int_dice = random.randint(0, 4)
    color_1 = color_pairs[int_dice][0]
    color_2 = color_pairs[int_dice][1]
else:
    color_1 = '#06770a'
    color_2 = '#fbee04'
    
#Create a pallette from the randomly chosen or default colors
cmap = sns.blend_palette([color_1, color_2],n_colors=max(num_prime_df.Powers))

rc={'axes.labelsize': 15, 'axes.titlesize': 15,
    'legend.title_fontsize': 10, 'legend.fontsize': 7,  
    'xtick.labelsize': 3.5, 'ytick.labelsize': 7,
    'font.size': 15}
sns.set(rc=rc)
sns.set_style("whitegrid")
g = sns.relplot(
    data=num_prime_df,
    x="Numbers", y="Primes",
    hue="Powers", size="Powers",
    palette=cmap, sizes=(20, 100),
    facet_kws={"legend_out": True})
g.set(xticks=list(range(1, chosen_num+1)), yticks=list(unique_primes))
plt.xticks(rotation=90)
plt.tick_params(pad=0)
st.pyplot(g)