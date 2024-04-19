import cv2

def increase_frame_count(input_video_path, output_video_path, target_frame_count):
    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mpg')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_to_add = target_frame_count - total_frames

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        for _ in range(frames_to_add):
            out.write(frame)

    cap.release()
    out.release()

increase_frame_count('yumi_video.mpg', 'output_video.mpg', target_frame_count=75)
