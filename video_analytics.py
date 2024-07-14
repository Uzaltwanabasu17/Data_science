import cv2
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from preprocessing import preprocess_frame
from feature_extraction import extract_features
from anomaly_detection import detect_anomalies
from visualization import plot_anomaly_scores

class VideoAnalytics:
    def __init__(self, video_path, history_size=50):
        self.cap = cv2.VideoCapture(video_path)
        self.history = deque(maxlen=history_size)
        self.frame_count = 0

    def generate_alert(self, anomaly_score, threshold=-0.5):
        if anomaly_score < threshold:
            print(f"ALERT: Anomaly detected at frame {self.frame_count}")
            return True
        return False

    def run(self):
        anomaly_scores = []

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            self.frame_count += 1
            processed_frame = preprocess_frame(frame)
            features = extract_features(processed_frame)
            anomaly_score = detect_anomalies(features, self.history)
            anomaly_scores.append(anomaly_score)

            alert_generated = self.generate_alert(anomaly_score)

            if alert_generated:
                cv2.putText(frame, "ANOMALY DETECTED", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

        plot_anomaly_scores(anomaly_scores)