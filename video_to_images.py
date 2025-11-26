import cv2
import os

def video_to_images(video_name):
    video_path = os.path.join("videos", video_name)

    if not os.path.exists(video_path):
        print(f"❌ Video not found: {video_path}")
        return

    output_folder = "images"
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ Cannot open video: {video_path}")
        return

    # Get video FPS (frames per second)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps)  # capture 1 frame every second

    print(f"🎞 Video FPS: {fps}")
    print("🔄 Extracting 1 frame per second...")

    count = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save only every "fps"th frame
        if count % frame_interval == 0:
            filename = os.path.join(output_folder, f"frame_{saved:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

        count += 1

    cap.release()
    print(f"✅ Done! Extracted {saved} frames to 'images/' folder.")


# Run with your video file name:
video_to_images("1st.mp4")
