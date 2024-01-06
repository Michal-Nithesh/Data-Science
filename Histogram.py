import matplotlib.pyplot as plt
import numpy as np
frommatplotlib import colors
Frommat plotlib.ticker importPercentFormatter
 
 
# Creating dataset
np.random.seed(23685752)
N_points =10000
n_bins =20
 
# Creating distribution
x =np.random.randn(N_points)
y =.8**x +np.random.randn(10000) +25
legend =[&#39;distribution&#39;]
# Creating histogram
fig, axs =plt.subplots(1, 1,
                        figsize=(10, 7),
                        tight_layout =True)
 
 
# Remove axes splines
fors in[&#39;top&#39;, &#39;bottom&#39;, &#39;left&#39;, &#39;right&#39;]:
    axs.spines[s].set_visible(False)
 
# Remove x, y ticks
axs.xaxis.set_ticks_position(&#39;none&#39;)
axs.yaxis.set_ticks_position(&#39;none&#39;)
   
# Add padding between axes and labels
axs.xaxis.set_tick_params(pad =5)
axs.yaxis.set_tick_params(pad =10)
 
# Add x, y gridlines
axs.grid(b =True, color =&#39;grey&#39;,
        linestyle =&#39;-.&#39;, linewidth =0.5,
        alpha =0.6)
 
# Add Text watermark
fig.text(0.9, 0.15, &#39;Jeeteshgavande30&#39;,
         fontsize =12,
         color =&#39;red&#39;,
         ha =&#39;right&#39;,
         va =&#39;bottom&#39;,
         alpha =0.7)
 
# Creating histogram

N, bins, patches =axs.hist(x, bins =n_bins)
 
# Setting color
fracs =((N**(1/5)) /N.max())
norm =colors.Normalize(fracs.min(), fracs.max())
 
forthisfrac, thispatch inzip(fracs, patches):
    color =plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
 
# Adding extra features   
plt.xlabel(&quot;X-axis&quot;)
plt.ylabel(&quot;y-axis&quot;)
plt.legend(legend)
plt.title(&#39;Customized histogram&#39;)
 
# Show plot
plt.show()
