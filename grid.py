# %%
import numpy as np
import pandas as pd
from holoviews import opts
import holoviews as hv
hv.extension('bokeh', 'matplotlib')

# %%

import tifffile
#fn = '/Volumes/core/micro/jeg/ac1692/10-31-19_GapR-Overnight/00000-10-29-19_GapR-100nmBE.tiff'
#x = tifffile.imread(fn)
xp = np.load('xp.npy')


# %%
st, sc, sy, sx = xp.shape

# %%

ds = hv.Dataset((np.arange(sy),
                 np.arange(sx),
                 np.arange(st), xp[:,1,:,:]),
                ['x','y', 'Frame'], 'movie')

# %%
#ds.clone(datatype=['xarray']).data


# %%
opts.defaults(
    opts.GridSpace(shared_xaxis=True, shared_yaxis=True),
    opts.Image(cmap='viridis', width=400, height=400),
    opts.Labels(text_color='white', text_font_size='8pt', text_align='left', text_baseline='bottom'),
    opts.Path(color='white'),
    opts.Spread(width=600),
    opts.Overlay(show_legend=False))
# %%
ds.to(hv.Image, ['x', 'y']).hist()


# %%
#np.save('xp.npy', xp)

# %%
