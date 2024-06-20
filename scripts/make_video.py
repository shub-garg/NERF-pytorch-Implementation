import argparse
import os
import imageio.v2 as imageio
import numpy as np

def parse_arguments():
    """
    Parses command line arguments for the image directory and video title.
    """
    parser = argparse.ArgumentParser(description="Create an MP4 video file from images in a directory.")
    parser.add_argument("--img_dir", type=str, required=True, help="Directory containing the images")
    parser.add_argument("--vid_title", type=str, required=True, help="Title of the output video file")
    return parser.parse_args()

def collect_images(img_dir):
    """
    Collects and reads images from the specified directory.
    
    Args:
        img_dir (str): The directory containing image files.
    
    Returns:
        list: A list of images read from the files.
    """
    # Get list of image files, sorted, and with full paths
    files = sorted([os.path.join(img_dir, file) for file in os.listdir(img_dir) if file.endswith(('png', 'jpg', 'jpeg'))])
    # Read images
    return [imageio.imread(file) for file in files]

def create_video(imgs, vid_title):
    """
    Creates an MP4 video file from a list of images.
    
    Args:
        imgs (list): List of images to include in the video.
        vid_title (str): Title of the output video file.
    """
    video_path = f"{vid_title}.mp4"
    # Initialize video writer
    with imageio.get_writer(video_path, format="FFMPEG", mode="I", fps=24, macro_block_size=1) as writer:
        for img in imgs:
            writer.append_data(img)  # Append each image to the video
    print(f"Video saved as {video_path}")

def main():
    """
    Main function to parse arguments, collect images, and create video.
    """
    args = parse_arguments()  # Parse command line arguments
    imgs = collect_images(args.img_dir)  # Collect images from the directory
    create_video(imgs, args.vid_title)  # Create video from collected images

if __name__ == "__main__":
    main()
