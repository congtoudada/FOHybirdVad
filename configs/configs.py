import ml_collections


def get_configs_avenue():
    config = ml_collections.ConfigDict()
    config.batch_size = 64
    config.epochs = 25
    config.mask_ratio = 0.5
    config.start_TS_epoch = 15
    config.masking_method = "random_masking"
    config.output_dir = "experiments/avenue"  # the checkpoints will be loaded from here
    config.abnormal_score_func = 'L2'
    config.grad_weighted_rec_loss = True
    config.model = "mae_cvt"
    config.input_size = (320, 640)
    config.norm_pix_loss = False
    config.use_only_masked_tokens_ab = False
    config.run_type = 'train'
    config.resume = False
    config.finetune = True
    config.pred_cls = True

    # Optimizer parameters
    config.weight_decay = 0.05
    config.lr = 1e-4

    # Dataset parameters
    config.dataset = "avenue"
    config.avenue_path = "H:/AI/dataset/VAD/Featurize_png/avenue"
    config.avenue_gt_path = "H:/AI/dataset/VAD/Featurize_png/avenue/avenue_gt"
    # config.avenue_path = "/home/featurize/data/avenue"
    # config.avenue_gt_path = "/home/featurize/data/avenue/avenue_gt"
    config.percent_abnormal = 0.25
    config.input_3d = True
    config.device = "cuda"

    config.start_epoch = 0
    config.print_freq = 10
    config.num_workers = 2
    config.pin_mem = False

    return config


def get_configs_shanghai():
    config = ml_collections.ConfigDict()
    config.batch_size = 100
    config.epochs = 50
    config.mask_ratio = 0.5
    config.start_TS_epoch = 30
    config.masking_method = "random_masking"
    config.output_dir = "experiments/shanghai"  # the checkpoints will be loaded from here
    config.abnormal_score_func = 'L2'
    config.grad_weighted_rec_loss = True
    config.model = "mae_cvt"
    config.input_size = (240, 480)
    config.norm_pix_loss = False
    config.use_only_masked_tokens_ab = False
    config.run_type = "inference"
    config.resume = False
    config.finetune = False
    config.pred_cls = True

    # Optimizer parameters
    config.weight_decay = 0.05
    config.lr = 1e-4

    # Dataset parameters
    config.dataset = "shanghai"
    config.shanghai_path = "H:/AI/dataset/VAD/Featurize_png/shanghaitech"
    config.shanghai_gt_path = "H:/AI/dataset/VAD/Featurize_png/shanghaitech/shanghai_gt"
    config.percent_abnormal = 0.25
    config.input_3d = True
    config.device = "cuda"

    config.start_epoch = 0
    config.print_freq = 10
    config.num_workers = 4
    config.pin_mem = False

    return config
