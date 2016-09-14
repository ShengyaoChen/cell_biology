# most modules that this program needs

import pandas as pd
import glob
import os
import mahotas as mh
import numpy as np

from skimage import io
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from scipy import ndimage as ndi
import skimage
from skimage import filters
from scipy.misc import imsave

import mahotas as mh

from matplotlib import pyplot as plt

plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'none'


def mt_analysis(seed_file, extension_file):
    seed = io.imread(seed_file)  # green channel
    mt = io.imread(extension_file)

    mt_mask = skimage.filters.threshold_yen(mt)
    mt_f = (mt > mt_mask)

    seed_mask = skimage.filters.threshold_yen(seed)
    seed_f = (seed > seed_mask)

    composite_f = np.maximum(seed_f, mt_f)

    distance = ndi.distance_transform_edt(composite_f)
    local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=composite_f)
    markers = ndi.label(local_maxi)[0]
    labels = watershed(-distance, markers, mask=composite_f)

    min_size = 250
    max_size = 600

    labeled, number_mt = mh.label(labels)

    sizes = mh.labeled.labeled_size(labeled)
    too_big = np.where(sizes > max_size)
    labeled = mh.labeled.remove_regions(labeled, too_big)
    too_small = np.where(sizes < min_size)
    labeled = mh.labeled.remove_regions(labeled, too_small)

    labeled = mh.labeled.remove_bordering(labeled)

    relabeled, n_final = mh.labeled.relabel(labeled)

    sizes = mh.labeled.labeled_size(relabeled)

    result_dict = {}
    for i in range(1, n_final):
        mask = relabeled == i
        labeled, number_mt = mh.label(mask & mt_f)
        sizes = mh.labeled.labeled_size(labeled)
        if len(sizes) == 3:
            result_dict[i] = sorted(sizes[1:].tolist(), reverse=True)
            imsave('dynamic_MT_%s.png' % i, mask & mt_f)

    mt_analysis = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in result_dict.items()])).transpose()
    mt_analysis.to_csv('measurement_result.csv')




