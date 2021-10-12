## Commands

### Experiment 1 (MsPacman-v0)
Run `MsPacman-v0` task.
```
python cs285/scripts/run_hw3_dqn.py --env_name MsPacman-v0 --exp_name q1
```

### Experiment 2 (LunarLander-v3)
Run DQN and DDQN on `LunarLander-v3` task with different seeds.
```
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_1 --seed 1
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_2 --seed 2
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_dqn_3 --seed 3

python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_1 --double_q --seed 1
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_2 --double_q --seed 2
python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q2_doubledqn_3 --double_q --seed 3
```

### Experiment 3 (LunarLander-v3)
Run `LunarLander` task with different learning rates: `5e-4`, `1e-3`, `2e-3`, `5e-3`.
Change the learning rate at !(cs285/infrastructure/dqn_utils.py)[`cs285/infrastructure/dqn_utils.py:167`]
```
python run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam1
python run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam2
python run_hw3_dqn.py --env_name LunarLander-v3 --exp_name q3_hparam3
```

### Experiment 4 (CartPole-v0)
Run commmands below to find the best value for `num_grad_steps_per_target_update` and `num_target_updates`.
```
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_ac_1_1 -ntu 1 -ngsptu 1
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_100_1 - ntu 100 -ngsptu 1
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_1_100 - ntu 1 -ngsptu 100
python run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name q4_10_10 - ntu 10 -ngsptu 10
```

### Experiment 5 (InvertedPendulum-v2 & HalfCheetah-v2)
Run `InvertedPendulum-v2` and `HalfCheetah-v2` tasks with `num_grad_steps_per_target_update = 10` and `num_target_updates = 10`.
```
python run_hw3_actor_critic.py --env_name InvertedPendulum-v2 --ep_len 1000 --discount 0.95 --scalar_log_freq 1 \
    -n 100 -l 2 -s 64 -b 5000 -lr 0.01 --exp_name q5_10_10 -ntu 10 -ngsptu 10
python run_hw3_actor_critic.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.90 --scalar_log_freq 1 \
    -n 150 -l 2 -s 32 -b 30000 -eb 1500 -lr 0.02 --exp_name q5_10_10 -ntu 10 -ngsptu 10
```
