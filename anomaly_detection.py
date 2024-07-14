import numpy as np
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1, random_state=42)

def detect_anomalies(features, history):
    history.append(features)
    
    if len(history) < history.maxlen:
        return 0  # Not enough data yet
    
    X = np.array(history).reshape(-1, 1)
    model.fit(X)
    anomaly_scores = model.decision_function(X)
    return anomaly_scores[-1]