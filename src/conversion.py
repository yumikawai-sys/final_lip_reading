import cv2

def convert_mp4_to_mpg(input_file, output_file, target_width=360, target_height=288):
    cap = cv2.VideoCapture(input_file)
    
    fourcc = cv2.VideoWriter_fourcc(*'mpg1')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    resized_width = target_width
    resized_height = target_height

    out = cv2.VideoWriter(output_file, fourcc, fps, (resized_width, resized_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (resized_width, resized_height))
        out.write(resized_frame)

    cap.release()
    out.release()

convert_mp4_to_mpg('input.mp4', 'output.mpg')