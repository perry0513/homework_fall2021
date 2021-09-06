## Commands

### Section 1 (Behavior Cloning)
Command for Question 1.2:

1. Run `Ant-v2` task with BC.
```
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
    --expert_data cs285/expert_data/expert_data_Ant-v2.pkl \
    --video_log_freq -1 \
    --train_batch_size 1000 \
    --num_agent_train_steps_per_iter 800 \
    --eval_batch_size 5000
```

2. Run `Walker2d-v2`task with BC.
```
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/Walker2d.pkl \
    --env_name Walker2d-v2 --exp_name bc_walker2d --n_iter 1 \
    --expert_data cs285/expert_data/expert_data_Walker2d-v2.pkl \
    --video_log_freq -1 \
    --train_batch_size 1000 \
    --num_agent_train_steps_per_iter 800 \
    --eval_batch_size 5000 \
```

Command for Question 1.3:

Run `Walker2d-v2` task with BC with `num_agent_train_steps_per_iter` = 800, 1600, 2400, 3200, 4000.
```
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/Walker2d.pkl \
    --env_name Walker2d-v2 --exp_name bc_walker2d --n_iter 1 \
    --expert_data cs285/expert_data/expert_data_Walker2d-v2.pkl \
    --video_log_freq -1 \
    --train_batch_size 1000 \
    --num_agent_train_steps_per_iter <800 | 1600 | 2400 | 3200 | 4000> \ // choose one here
    --eval_batch_size 5000 \
```


### Section 2 (DAgger)
Command for Question 2.2:
1. Run `Ant-v2` task with DAgger.
```
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name dagger_ant --n_iter 10 \
    --do_dagger \
    --expert_data cs285/expert_data/expert_data_Ant-v2.pkl \
    --video_log_freq -1 \
    --eval_batch_size 5000
```

2. Run `Walker2d-v2` task with DAgger.
```
python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/Walker2d.pkl \
    --env_name Walker2d-v2 --exp_name dagger_walker2d --n_iter 10 \
    --do_dagger \
    --expert_data cs285/expert_data/expert_data_Walker2d-v2.pkl \
    --video_log_freq -1 \
    --eval_batch_size 5000
```
