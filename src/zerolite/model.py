#!/usr/bin/env python3
import torch
from torch import nn

def device() -> str:
    return "cuda" if torch.cuda.is_available() else "cpu"

class SimplifiedChessNetwork(nn.Module):
    def __init__(self):
        super(SimplifiedChessNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linearReluStack = nn.Sequential(
            nn.Linear(8*8, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 64),
        )
    
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linearReluStack(x)
        return logits