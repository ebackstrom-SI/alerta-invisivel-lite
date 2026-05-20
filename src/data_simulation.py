"""
Synthetic network activity generator
for educational cybersecurity experiments.
"""

import random


def generate_network_activity(size=50):

    traffic = []

    for _ in range(size):

        normal_activity = random.randint(8, 15)
        traffic.append(normal_activity)

    anomaly_index = random.randint(0, size - 1)
    traffic[anomaly_index] = random.randint(40, 80)

    return traffic


if __name__ == "__main__":

    simulated_data = generate_network_activity()

    print("Synthetic network activity:")
    print(simulated_data)
