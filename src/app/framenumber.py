import cv2

def increase_frame_count(input_video_path, output_video_path, increase_factor, input_codec):
    cap = cv2.VideoCapture(input_video_path)
    out_cap = cv2.VideoCapture(input_video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    out_total_frames = int(out_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('total_frames', total_frames)
    print('out_total_frames', out_total_frames)


increase_frame_count('output_video.mpg', 'output.mpg', increase_factor=2, input_codec='mpg')
