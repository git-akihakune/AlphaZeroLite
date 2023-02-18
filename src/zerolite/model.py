#!/usr/bin/env python3
import torch
from torch import nn
from zerolite import globalval

def device() -> str:
    return "cuda" if torch.cuda.is_available() else "cpu"
    
class ZeroLiteNetwork(nn.Module):
    def __init__(self):
        super(ZeroLiteNetwork, self).__init__()
        self.stack = nn.Sequential(
            nn.Conv2d(
                in_channels=globalval.differentPiecesEachSide * 2,
                out_channels=globalval.differentPiecesEachSide * 2,
                kernel_size=3
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=globalval.differentPiecesEachSide * 2,
                out_channels=globalval.differentPiecesEachSide * 2,
                kernel_size=3
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=globalval.differentPiecesEachSide * 2,
                out_channels=globalval.differentPiecesEachSide,
                kernal_size=3
            )
        )

    def forward(self, param):
        return self.stack(param)
