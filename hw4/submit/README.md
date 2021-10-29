## Commands

### Experiment 1 
Train dynamics model on `cheetah` task.
```
python cs285/scripts/run_hw4_mb.py --exp_name q1_cheetah_n500_arch1x32 \
    --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 \
    --num_agent_train_steps_per_iter 500 --n_layers 1 --size 32 --scalar_log_freq -1 \
    --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q1_cheetah_n5_arch2x250 \
    --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 \
    --num_agent_train_steps_per_iter 5 --n_layers 2 --size 250 --scalar_log_freq -1 \
    --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q1_cheetah_n500_arch2x250 \
    --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 \
    --num_agent_train_steps_per_iter 500 --n_layers 2 --size 250 --scalar_log_freq -1 \
    --mpc_action_sampling_strategy 'random'
```

### Experiment 2
Run single iteration with action selection using trained dynamics model.
```
python cs285/scripts/run_hw4_mb.py --exp_name q2_obstacles_singleiteration \ 
    --env_name obstacles-cs285-v0 --add_sl_noise --num_agent_train_steps_per_iter 20 \
    --n_iter 1 --batch_size_initial 5000 --batch_size 1000 --mpc_horizon 10 \
    --mpc_action_sampling_strategy 'random'
```

### Experiment 3
Run MBRL algorithm with on-policy data collection and iterative model training.
```
python cs285/scripts/run_hw4_mb.py --exp_name q3_obstacles --env_name obstacles-cs285-v0 \
    --add_sl_noise --num_agent_train_steps_per_iter 20 --batch_size_initial 5000 \
    --batch_size 1000 --mpc_horizon 10 --n_iter 12 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q3_reacher --env_name reacher-cs285-v0 \
    --add_sl_noise --num_agent_train_steps_per_iter 1000 --batch_size_initial 5000 \
    --batch_size 5000 --mpc_horizon 10 --n_iter 15 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q3_cheetah --env_name cheetah-cs285-v0 \
    --mpc_horizon 15 --add_sl_noise --num_agent_train_steps_per_iter 1500 \
    --batch_size_initial 5000 --batch_size 5000 --n_iter 20 --mpc_action_sampling_strategy 'random'
```

### Experiment 4
Run commmands below to compare performance differences when changing `horizon`, `num_action_sequences`, and `ensemble_size`.
```
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_horizon5 --env_name reacher-cs285-v0 \
    --add_sl_noise --mpc_horizon 5 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_horizon15 --env_name reacher-cs285-v0 \
    --add_sl_noise --mpc_horizon 15 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_horizon30 --env_name reacher-cs285-v0 \
    --add_sl_noise --mpc_horizon 30 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'

python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_numseq100 --env_name reacher-cs285-v0 \
    --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 --batch_size 800 \
    --n_iter 15 --mpc_num_action_sequences 100 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_numseq1000 --env_name reacher-cs285-v0 \
    --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 --batch_size 800 \
    --n_iter 15 --mpc_num_action_sequences 1000 --mpc_action_sampling_strategy 'random'

python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_ensemble1 --env_name reacher-cs285-v0 \
    --ensemble_size 1 --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_ensemble3 --env_name reacher-cs285-v0 \
    --ensemble_size 3 --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q4_reacher_ensemble5 --env_name reacher-cs285-v0 \
    --ensemble_size 5 --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 \
    --batch_size 800 --n_iter 15 --mpc_action_sampling_strategy 'random'
```

### Experiment 5
Run below commands to compare performances between random shooting and CEM.
```
python cs285/scripts/run_hw4_mb.py --exp_name q5_cheetah_random --env_name 'cheetah-cs285-v0' 
    --mpc_horizon 15 --add_sl_noise --num_agent_train_steps_per_iter 1500 --batch_size_initial 5000 
    --batch_size 5000 --n_iter 5 --mpc_action_sampling_strategy 'random'
python cs285/scripts/run_hw4_mb.py --exp_name q5_cheetah_cem_2 --env_name 'cheetah-cs285-v0' 
    --mpc_horizon 15 --add_sl_noise --num_agent_train_steps_per_iter 1500 --batch_size_initial 5000 
    --batch_size 5000 --n_iter 5 --mpc_action_sampling_strategy 'cem' --cem_iterations 2
python cs285/scripts/run_hw4_mb.py --exp_name q5_cheetah_cem_4 --env_name 'cheetah-cs285-v0' 
    --mpc_horizon 15 --add_sl_noise --num_agent_train_steps_per_iter 1500 --batch_size_initial 5000 
    --batch_size 5000 --n_iter 5 --mpc_action_sampling_strategy 'cem' --cem_iterations 4
```
