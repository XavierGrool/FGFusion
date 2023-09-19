from mmdet3d.apis import inference_detector, init_model
from mmdet3d.registry import VISUALIZERS

config_file = './checkpoints/second_hv_secfpn_8xb6-80e_kitti-3d-car.py'
checkpoint_file = './checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth'

model = init_model(config_file, checkpoint_file, device='cuda:0')

visualizer = VISUALIZERS.build(model.cfg.visualizer)
visualizer.dataset_meta = model.dataset_meta

pcd = './demo/data/kitti/000008.bin'
result, data = inference_detector(model, pcd)
points = data['inputs']['points']
data_input = dict(points=points)

out_dir = '/home/awesome/yzx/coding/mmdetection3d/mmdetection3d/checkpoints/test.png'
visualizer.add_datasample(
    'result',
    data_input,
    data_sample=result,
    draw_gt=False,
    show=False,
    wait_time=0,
    out_file=out_dir,
    vis_task='lidar_det')