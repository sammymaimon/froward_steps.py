import torch
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn

N = 40
mu = 0.02
std = 2e-1
noise=[]

X1_plot, X2_plot = np.meshgrid(np.linspace(-1., 1., N), np.linspace(-1., 1., N))
X = torch.tensor(np.stack([X1_plot.reshape(N ** 2), X2_plot.reshape(N ** 2)]), dtype=torch.float32).T
noise = np.array((np.random.normal(mu, std, N**2), np.random.normal(mu, std, N**2))).T
noise= torch.Tensor(noise)
# plt.scatter(noise[0,:], noise[1,:])
# plt.show()

#Y = X.clone().detach()
Y = noise.clone().detach()

for i in range(19, 2, -1):
    model = nn.Sequential(
        nn.Linear(2, 24),
        nn.ReLU(),
        nn.Linear(24, 12),
        nn.ReLU(),
        nn.Linear(12, 6),
        nn.ReLU(),
        nn.Linear(6, 2))

    model.load_state_dict(torch.load(f"../models3/_{i}_{i-1}.pt"))
    model.eval()

    Y = model(noise)
    Y_plot = (Y.clone().detach().numpy())
    print('this is Y_plot', Y_plot)
    # X_plot = X_plot.detach().numpy()
    #
    # plt.quiver(X_plot[:, 0], X_plot[:, 1], Y_plot[:, 0], Y_plot[:, 1])
    # # plt.plot(X_plot[:, 0], X_plot[:, 1], '.')

    # plt.plot(Y_plot[:N, 0], Y_plot[:N, 1], 'k')
    # plt.plot(Y_plot[N:2*N, 0], Y_plot[N:2*N, 1], 'k')
    # plt.plot(Y_plot[2*N:3 * N, 0], Y_plot[2*N:3 * N, 1], 'k')


#for grid and lines
    plt.figure()
    # for i in range(N):
    #     ii = i + 1
    #     plt.plot(Y_plot[i*N:ii*N, 0], Y_plot[i*N:ii*N, 1], 'k')
    #     plt.plot(Y_plot[i::N, 0], Y_plot[i::N, 1], 'k')

    plt.scatter(Y_plot[:, 0], Y_plot[:, 1], s=None)
plt.show()