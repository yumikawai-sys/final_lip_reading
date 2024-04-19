# (pls. use the specified version)
# pip install the following 
# pip install numpy==1.24.1
# pip install opencv-python==4.6.0.66
# pip install tensorflow==2.10.1
# pip install scikit-image

import os 
import cv2
import numpy as np
import tensorflow as tf
from app.utils import num_to_char
from app.modelutil import load_model

# Set the video file path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data', 's1', 'lrik3s.mpg')

vocab = [x for x in "abcdefghijklmnopqrstuvwxyz'?!123456789 "]
char_to_num = tf.keras.layers.StringLookup(vocabulary=vocab, oov_token="")
num_to_char = tf.keras.layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True
)

def resize_video(video_path, target_shape=(75, 46, 140)):
    print('video_path_inpred', video_path)
    
    cap = cv2.VideoCapture(video_path)
    frames = []
    print('cap', cap)
    frame_count = 0 
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        resized_frame = cv2.resize(frame, (target_shape[2], target_shape[1]))
        
        resized_frame_gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        
        resized_frame_gray = np.expand_dims(resized_frame_gray, axis=-1)
        frames.append(resized_frame_gray)
        
        frame_count += 1 
        
        if frame_count >= target_shape[0]:
            break
    
    cap.release()

    if not frames:
        ret, first_frame = cv2.VideoCapture(video_path).read()
        if ret:
            first_frame = cv2.resize(first_frame, (target_shape[2], target_shape[1]))
            first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
            first_frame_gray = np.expand_dims(first_frame_gray, axis=-1)
            frames.append(first_frame_gray)

    while len(frames) < target_shape[0]:
        if frames:
            frames.append(np.copy(frames[-1]))
        else:
            break

    frames_array = np.array(frames)
    print('frames_array', frames_array)
    print('frames_array_shape', frames_array.shape)
    return frames_array


def sample_prediction(video_path):
    model = load_model()
    
    # Load video data and resize
    resized_frames = resize_video(video_path)
    
    # Check if the number of frames is less than 75
    if len(resized_frames) < 75:
        while len(resized_frames) < 75:
            resized_frames = np.append(resized_frames, [resized_frames[-1]], axis=0)
    elif len(resized_frames) > 75:
        resized_frames = resized_frames[:75]
    
    input_frames = np.expand_dims(resized_frames, axis=0)
    
    # Predict
    yhat = model.predict(input_frames)
    decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
    converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
    print('Prediction:', converted_prediction)

    return converted_prediction

