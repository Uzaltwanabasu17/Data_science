from video_analytics import VideoAnalytics

def main():
    video_path = r"C:\Users\ASUS TUF\Desktop\Data_science\Data_science\video\video1.mp4"  # Replace with your video file path
    analytics = VideoAnalytics(video_path)
    analytics.run()

if __name__ == "__main__":
    main()