#数据文件大小不同，因为数据精度不同，s42为float64，s132和s102为float32

import numpy as np

# filename = 'experiments/rb2d/data/rb2d_ra1e6_s42.npz'
# filename = 'experiments/rb2d/data/rb2d_ra1e6_s132.npz'
filename = 'experiments/rb2d/data/rb2d_ra1e6_s102.npz'
d = np.load(filename)

print(d.keys())
# >>> ['p', 'b', 'u', 'w', 'bz', 'uz', 'wz', 'write_number', 'sim_time']

print(d['p'].shape)
print(type(d['p'][0,0,0]))
print(d['b'].shape)
# # >>> (200, 512, 128)
print(d['u'].shape)
print(d['w'].shape)
print(d['bz'].shape)
print(d['uz'].shape)
print(d['wz'].shape)
print(d['write_number'].shape)
print(d['sim_time'].shape)
