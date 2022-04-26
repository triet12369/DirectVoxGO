_base_ = '../default.py'

expname = 'dvgo_ankle'
basedir = './logs/nerf_synthetic'

data = dict(
    datadir='./data/nerf_synthetic/ankle',
    dataset_type='blender',
    white_bkgd=True,
)