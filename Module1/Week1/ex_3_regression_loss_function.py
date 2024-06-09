# Write a function to choose a regression loss function to calculate loss.

import random
import math


def exercise3():
    num_samples = input('Input num_samples = ')

    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return

    num_samples = int(num_samples)
    loss_name = input('Input loss name (MAE, MSE, RMSE): ')
    final_loss = 0

    def calc_ae(pred, target):
        return abs(pred - target)

    def calc_se(pred, target):
        return (pred - target) ** 2

    for i in range(num_samples):
        pred_sample = random.uniform(0, 10)
        target_sample = random.uniform(0, 10)

        if loss_name == 'MAE':
            loss = calc_ae(pred_sample, target_sample)
        elif loss_name in ['MSE', 'RMSE']:
            loss = calc_se(pred_sample, target_sample)

        final_loss += loss
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred_sample}, "
              f"target: {target_sample}, loss: {loss}")

    final_loss /= num_samples

    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)

    print(f"final {loss_name}: {final_loss}")


exercise3()
