import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import glob
import tensorflow as tf
import numpy as np
from tensorflow.python.summary.summary_iterator import summary_iterator
import sys
import glob

prefix = 'data/hw5_expl_'

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
    parsedfiles = [(logfile[len(prefix):-70], glob.glob(logfile)[0]) for logfile in logfiles]
    return parsedfiles


def plot_experiments(title, eventfiles):
    plt.clf()
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('reward')
    for name, eventfile in eventfiles:
        Y = get_section_results(eventfile)
        plt.plot(np.arange(len(Y)), Y, label=name)
    plt.legend()
    plt.savefig(title+'.png')


if __name__ == '__main__':

    # logdir = 'data/q1_lb_rtg_na_CartPole-v0_27-09-2021_01-03-36/events*'
    # logfiles = sys.argv[2:]
    # parsedfiles = [(logfile[9:-70], glob.glob(logfile)[0]) for logfile in logfiles]

    title = sys.argv[1]
    logfiles = sys.argv[2:]
    plot_experiments(title, parse_file(logfiles))
