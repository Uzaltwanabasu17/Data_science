import matplotlib.pyplot as plt

def plot_anomaly_scores(anomaly_scores):
    plt.figure(figsize=(12, 6))
    plt.plot(anomaly_scores)
    plt.title('Anomaly Scores Over Time')
    plt.xlabel('Frame')
    plt.ylabel('Anomaly Score')
    plt.show()