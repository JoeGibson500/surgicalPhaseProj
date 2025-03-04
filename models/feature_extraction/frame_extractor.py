import os
import sys
import cv2
import pandas as pd

# Add project root to path for utils import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils.phase_utils import clean_phase_name


class FrameExtractor:
    """Extracts frames per surgical phase from videos using timestamp metadata."""

    def __init__(self, timestamp_folder, video_folder, output_folder):
        self.timestamp_folder = timestamp_folder
        self.video_folder = video_folder
        self.output_folder = output_folder

        os.makedirs(self.output_folder, exist_ok=True)

    def extract_all(self):
        """Extract frames for all timestamp files in the timestamp folder."""
        timestamp_files = [f for f in os.listdir(self.timestamp_folder) if f.endswith(".xlsx")]

        for timestamp_file in timestamp_files:
            video_name = timestamp_file.replace(".xlsx", ".mkv")
            video_path = os.path.join(self.video_folder, video_name)

            print(f"Extracting phases from {video_name}...")

            if not os.path.exists(video_path):
                print(f"Warning: No matching video found for {timestamp_file}")
                continue

            video_output_folder = os.path.join(self.output_folder, video_name.replace(".mkv", ""))
            os.makedirs(video_output_folder, exist_ok=True)

            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)

            df = pd.read_excel(os.path.join(self.timestamp_folder, timestamp_file))
            df["Action"] = df["Action"].dropna().apply(clean_phase_name)

            phases = df["Action"].to_list()
            start_times = df["Start Time (s)"].to_list()
            end_times = df["End Time (s)"].to_list()

            for i, phase in enumerate(phases):
                phase_folder = os.path.join(video_output_folder, phase)
                os.makedirs(phase_folder, exist_ok=True)

                start_frame = int(start_times[i] * fps)
                end_frame = int(end_times[i] * fps)

                for frame_id in range(start_frame, end_frame):
                    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
                    ret, frame = cap.read()
                    if not ret:
                        print(f"Warning: Could not extract frame {frame_id} in {video_name}, phase: {phase}")
                        break
                    frame_name = os.path.join(phase_folder, f"frame_{frame_id}.jpg")
                    cv2.imwrite(frame_name, frame)

            cap.release()