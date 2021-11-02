import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import glob
import tensorflow as tf
import numpy as np
from tensorflow.python.summary.summary_iterator import summary_iterator
import sys
import glob

def get_section_results(file):
    """
        requires tensorflow==1.12.0
    """
    Y = []
    for e in summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Eval_AverageReturn':
                Y.append(v.simple_value)
    return np.array(Y)

def parse_file(logfiles):
    parsedfiles = [(logfile[4:-70], glob.glob(logfile)[0]) for logfile in logfiles]
    return parsedfiles


def plot_experiments(title, eventfiles):
    plt.clf()
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('reward')
    for name, eventfile in eventfiles:
        Y = get_section_results(eventfile)
        plt.plot(np.arange(len(Y)), Y, marker='o', label=name)
    plt.legend()
    plt.savefig(title+'.png')


if __name__ == '__main__':

    # logdir = 'data/q1_lb_rtg_na_CartPole-v0_27-09-2021_01-03-36/events*'
    # logfiles = sys.argv[2:]
    # parsedfiles = [(logfile[9:-70], glob.glob(logfile)[0]) for logfile in logfiles]

    # Q2
    title = 'obstacles_singleiteration'
    logfiles = ['hw4_q2_obstacles_singleiteration_obstacles-cs285-v0_28-10-2021_13-26-41/events.out.tfevents.1635398801.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
    # Q3
    title = 'MBRL_on-policy_data_collection_iterative_training'
    logfiles = [
            'hw4_q3_cheetah_cheetah-cs285-v0_28-10-2021_14-33-50/events.out.tfevents.1635402830.andyh0913-Ubuntu20',
            'hw4_q3_obstacles_obstacles-cs285-v0_28-10-2021_14-01-27/events.out.tfevents.1635400887.andyh0913-Ubuntu20',
            'hw4_q3_reacher_reacher-cs285-v0_28-10-2021_14-06-10/events.out.tfevents.1635401170.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
    # Q4 ensemble size
    title = 'comparison_ensemble_size'
    logfiles = [
            'hw4_q4_reacher_ensemble1_reacher-cs285-v0_28-10-2021_16-35-24/events.out.tfevents.1635410124.andyh0913-Ubuntu20',
            'hw4_q4_reacher_ensemble3_reacher-cs285-v0_28-10-2021_16-37-28/events.out.tfevents.1635410248.andyh0913-Ubuntu20',
            'hw4_q4_reacher_ensemble5_reacher-cs285-v0_28-10-2021_16-42-52/events.out.tfevents.1635410572.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
    # Q4 num action sequences
    title = 'comparison_num_action_sequences'
    logfiles = [
            'hw4_q4_reacher_numseq1000_reacher-cs285-v0_28-10-2021_16-30-04/events.out.tfevents.1635409804.andyh0913-Ubuntu20',
            'hw4_q4_reacher_numseq100_reacher-cs285-v0_28-10-2021_16-26-20/events.out.tfevents.1635409580.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
    # Q4 horizon
    title = 'comparison_horizon'
    logfiles = [
            'hw4_q4_reacher_horizon15_reacher-cs285-v0_28-10-2021_16-05-01/events.out.tfevents.1635408301.andyh0913-Ubuntu20',
            'hw4_q4_reacher_horizon30_reacher-cs285-v0_28-10-2021_16-12-28/events.out.tfevents.1635408748.andyh0913-Ubuntu20',
            'hw4_q4_reacher_horizon5_reacher-cs285-v0_28-10-2021_16-01-46/events.out.tfevents.1635408106.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
    # Q5
    title = 'comparison_randomshooting_and_CEM'
    logfiles = [
            'hw4_q5_cheetah_cem_2_cheetah-cs285-v0_29-10-2021_02-55-29/events.out.tfevents.1635447329.andyh0913-Ubuntu20',
            'hw4_q5_cheetah_cem_4_cheetah-cs285-v0_29-10-2021_03-01-29/events.out.tfevents.1635447689.andyh0913-Ubuntu20',
            'hw4_q5_cheetah_random_cheetah-cs285-v0_28-10-2021_16-52-17/events.out.tfevents.1635411137.andyh0913-Ubuntu20']
    plot_experiments(title, parse_file(logfiles))
