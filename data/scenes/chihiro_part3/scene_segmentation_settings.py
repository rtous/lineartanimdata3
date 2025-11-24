import numpy as np


masks_points = []
mask0_points = []
mask0_labels = []

#positive points
mask0_points.append([600,800])
mask0_labels.append(1)

#negative points
#mask0_points.append([1250,800]) 
#mask0_labels.append(0)

masks_points.append([np.array(mask0_points, dtype=np.float32), np.array(mask0_labels, np.int32)])
