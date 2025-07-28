# PyTorch model for anomaly detection
import torch.nn as nn

class AnomalyDetector(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64), nn.ReLU(),
            nn.Linear(64, 32), nn.ReLU())
        self.decoder = nn.Sequential(
            nn.Linear(32, 64), nn.ReLU(),
            nn.Linear(64, input_dim))

    def forward(self, x):
        return self.decoder(self.encoder(x))
