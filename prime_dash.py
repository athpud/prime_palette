import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from prime_factors import *

#Overall title
st.title("Prime Palette")

#Sidebar title
st.sidebar.title('Options')

#Pick a number
st.sidebar.write("Choose a range of numbers to visualize")
chosen_num = st.sidebar.slider("Number range:", 2, 100, 50)

#Pick a color
st.sidebar.write("Chooose two colors for your visualization")
chosen_color_1 = st.sidebar.color_picker("Click square below to pick the first color:")
chosen_color_2 = st.sidebar.color_picker("Click square below to pick the second color:")

num_prime_df = prime_dfdict(chosen_num)
unique_primes = num_prime_df.Primes.unique()

#Create a pallette from the chosen colors
color_text = "blend"+":"+chosen_color_1+','+chosen_color_2
cmap = sns.color_palette(color_text,n_colors=max(num_prime_df.Repeats))

rc={'axes.labelsize': 15, 'axes.titlesize': 15,
    'legend.title_fontsize': 10, 'legend.fontsize': 7,  
    'xtick.labelsize': 3.5, 'ytick.labelsize': 7,
    'font.size': 15}
sns.set(rc=rc)
sns.set_style("whitegrid")
g = sns.relplot(
    data=num_prime_df,
    x="Numbers", y="Primes",
    hue="Repeats", size="Repeats",
    palette=cmap, sizes=(20, 100),
    facet_kws={"legend_out": True})
g.set(xticks=list(range(1, chosen_num+1)), yticks=list(unique_primes))
plt.xticks(rotation=90)
plt.tick_params(pad=0)
st.pyplot(g)