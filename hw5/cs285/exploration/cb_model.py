from cs285.infrastructure import pytorch_util as ptu
from .base_exploration_model import BaseExplorationModel
import torch.optim as optim
from torch import nn
import torch
import numpy as np

# Count-based exploration model
class CBModel(nn.Module, BaseExplorationModel):
    def __init__(self, hparams, optimizer_spec, **kwargs):
        super().__init__(**kwargs)

        self.round_digit = hparams['round_digit']
        self.state2count = dict()

    def forward(self, ob_no):
        def count_plus1(ob):
            ob_tup = tuple(ob)
            if ob_tup in self.state2count:
                return self.state2count[ob_tup] + 1
            else: return 1

        rounded = np.round(ob_no, self.round_digit)
        count = np.array(list(map(count_plus1, rounded)))
        bonus = 1 / count
        return bonus

    def forward_np(self, ob_no):
        return self(ob_no)

    def update(self, ob_no):
        rounded = np.round(ob_no, self.round_digit)
        for ob in rounded:
            ob_tup = tuple(ob)
            if ob_tup in self.state2count:
                self.state2count[ob_tup] += 1
            else:
                self.state2count[ob_tup] = 1
        return 0 # dummy
