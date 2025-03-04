from frame_extractor import PhaseFrameExtractor

TIMESTAMP_FOLDER = "data/video_timestamps/"
VIDEO_FOLDER = "data/full_videos"
OUTPUT_FOLDER_PHASE = "data/frames_per_phase/"

def extract_frames(): 
    
    # Initialise frame extractor
    frame_extractor = PhaseFrameExtractor(TIMESTAMP_FOLDER, VIDEO_FOLDER, OUTPUT_FOLDER_PHASE)
    
    print("Running frame extraction per phase...")
    frame_extractor.extract_frames_per_phase(video_folder=VIDEO_FOLDER, timestamp_folder=TIMESTAMP_FOLDER, output_folder= OUTPUT_FOLDER_PHASE)
    print(f"Frames extracted and saved at {OUTPUT_FOLDER_PHASE}")
 
if __name__ == "__main__":
    extract_frames()