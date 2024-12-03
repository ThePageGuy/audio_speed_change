# File path: modify_speed_sox.py

import os
import subprocess

# Define input and output folders
INPUT_FOLDER = "normal"
OUTPUT_FOLDER = "x2"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def change_playback_speed_with_sox(input_file, output_file, playback_speed=2.0):
    """
    Changes the playback speed of an MP3 file while preserving pitch using sox.

    Args:
        input_file (str): Path to the input MP3 file.
        output_file (str): Path to save the output MP3 file.
        playback_speed (float): Factor to change the speed (e.g., 2.0 for 2x speed).
    """
    try:
        # Call sox with pitch preservation
        subprocess.run(
            [
                "sox",
                input_file,
                output_file,
                "tempo",
                "-s",
                str(playback_speed),
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"SoX failed: {e}")

def process_files(input_folder, output_folder):
    """
    Processes all MP3 files in the input folder, adjusts their playback speed,
    and saves them to the output folder.

    Args:
        input_folder (str): Folder containing the input MP3 files.
        output_folder (str): Folder to save the modified MP3 files.
    """
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".mp3"):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name)
            
            print(f"Processing {file_name}...")
            try:
                change_playback_speed_with_sox(input_file_path, output_file_path)
                print(f"Saved modified file to {output_file_path}")
            except Exception as e:
                print(f"Failed to process {file_name}: {e}")

if __name__ == "__main__":
    process_files(INPUT_FOLDER, OUTPUT_FOLDER)
    print("All files processed.")
