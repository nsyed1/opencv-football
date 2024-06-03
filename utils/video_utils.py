import cv2

# takes a video and returns a list of frames
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    x_size = output_video_frames[0].shape[1]
    y_size = output_video_frames[0].shape[0]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (x_size, y_size))
    for frame in output_video_frames:
        out.write(frame)
    out.release()