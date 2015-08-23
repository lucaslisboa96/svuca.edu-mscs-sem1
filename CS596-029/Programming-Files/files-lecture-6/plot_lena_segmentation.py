"""
=========================================
Segmenting the picture of Lena in regions
=========================================

This example uses :ref:`spectral_clustering` on a graph created from
voxel-to-voxel difference on an image to break this image into multiple
partly-homogeneous regions.

This procedure (spectral clustering on an image) is an efficient
approximate solution for finding normalized graph cuts.

There are two options to assign labels:

* with 'kmeans' spectral clustering will cluster samples in the embedding space
  using a kmeans algorithm
* whereas 'discrete' will iteratively search for the closest partition
  space to the embedding space.
"""
# print(__doc__)

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>, Brian Cheung
# License: BSD 3 clause

# import time
import numpy as np
# import scipy as sp
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
# from sklearn.feature_extraction import image
# from sklearn.cluster import spectral_clustering
from sklearn.cluster import KMeans
# from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle

def HSVColor(img):
    if isinstance(img,Image.Image):
        r,g,b = img.split()
        Hdat = []
        Sdat = []
        Vdat = [] 
        for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
            h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    img = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            img[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return img

'''
localFolder = '.\\hands\\*.jpg'
for file in glob.glob(localFolder):
    try:
        img = {'file': open(file, 'rb')}
    finally:
        img['file'].close()
lena = sp.misc.lena()
'''
file = 'hand_1__by_RainbowCupcakeKidd.jpg'
img = Image.open(file)
# Downsample the image by a factor of 4
# lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
# lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
# downsize
ratio = 0.25
img = img.resize( [int(ratio * s) for s in img.size])
img.show()
# convert to HSV
im = HSVColor(img)# apply a series of erosions and dilations to the mask

im.show()
w, h = original_shape = tuple(im.size)
assert im.mode == 'RGB'
# convert to np array
im = list(im.getdata())
im = map(list, im)
img_np = np.array(im)
# try K-means
image_array_sample = shuffle(img_np, random_state=0)[:10000]
n_colors = 4
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)
labels = kmeans.predict(img_np)
img_np_new = recreate_image(kmeans.cluster_centers_, labels, w, h)
img_new = np.uint8(img_np_new)
#img_new = Image.fromarray(img_new, mode='RGB')
img_new = Image.frombuffer('RGB', (w, h), img_new, "raw", 'RGB', 0, 1)
img_new.show()
'''
# Convert the image into a graph with the value of the gradient on the edges.
graph = image.img_to_graph(image_array)
# Take a decreasing function of the gradient: an exponential
# The smaller beta is, the more independent the segmentation is of the
# actual image. For beta=1, the segmentation is close to a voronoi
beta = 5
eps = 1e-6
graph.data = np.exp(-beta * graph.data / image_array.std()) + eps

# Apply spectral clustering (this step goes much faster if you have pyamg
# installed)
N_REGIONS = 11

###############################################################################
# Visualize the resulting regions

for assign_labels in ('kmeans', 'discretize'):
    t0 = time.time()
    labels = spectral_clustering(graph, n_clusters=N_REGIONS,
                                 assign_labels=assign_labels,
                                 random_state=1)
    t1 = time.time()
    labels = labels.reshape(image_array.shape)

    plt.figure(figsize=(5, 5))
    plt.imshow(image_array, cmap=plt.cm.gray)
    for l in range(N_REGIONS):
        plt.contour(labels == l, contours=1,
                    colors=[plt.cm.spectral(l / float(N_REGIONS)), ])
    plt.xticks(())
    plt.yticks(())
    plt.title('Spectral clustering: %s, %.2fs' % (assign_labels, (t1 - t0)))

plt.show()
'''