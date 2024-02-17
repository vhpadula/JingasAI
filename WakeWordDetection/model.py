import torch
import torch.nn as nn

class LSTMWakeWordDetector(nn.Module):

    def __init__(self, num_classes, feature_size, hidden_size, num_layers, dropout, bidirectional, device='cpu'):
        super(LSTMWakeWordDetector, self).__init__()
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.directions = 2 if bidirectional else 1
        self.device = device
        self.layernorm = nn.LayerNorm(feature_size)
        self.lstm = nn.LSTM(input_size=feature_size, hidden_size=hidden_size,
                            num_layers=num_layers, dropout=dropout,
                            bidirectional=bidirectional)
        self.classifier = nn.Linear(hidden_size * self.directions, num_classes)

    def _init_hidden(self, batch_size):
        return (torch.zeros(self.num_layers * self.directions, batch_size, self.hidden_size).to(self.device),
                torch.zeros(self.num_layers * self.directions, batch_size, self.hidden_size).to(self.device))
    
    def forward(self, x):
        # x.shape => seq_len, batch, feature
        if x.size(0) == 0:  # Check if the sequence length is 0
            return None

        x = self.layernorm(x)
        hidden = self._init_hidden(x.size()[1])
        out, (hn, cn) = self.lstm(x, hidden)
        out = self.classifier(hn)
        return out