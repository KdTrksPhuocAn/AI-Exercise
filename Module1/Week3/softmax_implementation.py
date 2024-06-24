import torch
import torch.nn as nn


class Softmax(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):

        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x, dim=0, keepdim=True)
        return exp_x / sum_exp_x


class SoftmaxStable(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):

        # Compute stable softmax
        x_max = torch.max(x, dim=0, keepdim=True).values
        exp_x = torch.exp(x - x_max)
        sum_exp_x = torch.sum(exp_x, dim=0, keepdim=True)
        return exp_x / sum_exp_x
