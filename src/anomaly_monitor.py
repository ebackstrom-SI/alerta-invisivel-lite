"""
Alerta Invisível Lite
Educational prototype for anomaly observation in cybersecurity environments.
"""

import pandas as pd


def detect_basic_anomalies(values, threshold=2.0):
    """
    Simple anomaly detector using deviation from average.
    Educational demonstration only.
    """

    mean_value = sum(values) / len(values)

    anomalies = []

    for value in values:
        deviation = abs(value - mean_value)

        if deviation > threshold:
            anomalies.append(value)

    return anomalies


if __name__ == "__main__":

    sample_network_activity = [10, 11, 9, 10, 50, 12, 11]

    detected = detect_basic_anomalies(sample_network_activity)

    print("Detected anomalies:")
    print(detected)
    
