set -x -e

export NUM_GPUS=2

# torchrun --nproc_per_node=$NUM_GPUS --master_port=29500 \
CUDA_VISIBLE_DEVICES=0,1 uv run torchrun --nproc_per_node=2 \
    gr00t/experiment/launch_finetune.py \
    --base_model_path nvidia/GR00T-N1.6-3B \
    --dataset_path  ./demo_data/cube_to_bowl_5 \
    --modality_config_path examples/SO100/so100_config.py \
    --embodiment_tag NEW_EMBODIMENT \
    --num_gpus $NUM_GPUS \
    --output_dir /tmp/so100_finetune \
    --save_steps 1000 \
    --save_total_limit 5 \
    --max_steps 10000 \
    --warmup_ratio 0.05 \
    --weight_decay 1e-5 \
    --learning_rate 1e-4 \
    --use_wandb \
    --global_batch_size 4 \
    # --color_jitter_params brightness 0.3 contrast 0.4 saturation 0.5 hue 0.08 \
    --dataloader_num_workers 4
