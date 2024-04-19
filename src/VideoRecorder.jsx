import { useState, useRef } from "react";

const VideoRecorder = () => {
    const [recordedVideoUrl, setRecordedVideoUrl] = useState(null);
    const videoRef = useRef();

    const startCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoRef.current.srcObject = stream;
            videoRef.current.play();
            const mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
            const chunks = [];
            mediaRecorder.ondataavailable = (event) => {
                chunks.push(event.data);
            };
        } catch (error) {
            console.error('Error accessing camera:', error);
        }
    };

    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoRef.current.srcObject = stream;
            videoRef.current.play();
            const mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
            const chunks = [];
            mediaRecorder.ondataavailable = (event) => {
                chunks.push(event.data);
            };
            mediaRecorder.onstop = () => {
                const blob = new Blob(chunks, { type: 'video/mp4' });
                const url = URL.createObjectURL(blob);
                setRecordedVideoUrl(url);
            };
            mediaRecorder.start();
        } catch (error) {
            console.error('Error accessing camera:', error);
        }
    };

    const stopRecording = () => {
        if (videoRef.current.srcObject) {
            const tracks = videoRef.current.srcObject.getTracks();
            tracks.forEach(track => track.stop());
        }
    };

    return (
        <div className="video_area">
            
            <video ref={videoRef} style={{ width: '100%' }} controls />
            {/* <img src="man-3123561_640.jpg"></img> */}
            <div className="button_area">
                <button onClick={startCamera}>Camera</button>
                <button onClick={startRecording}>Recording</button>
                <button onClick={stopRecording}>Stop</button>
                {recordedVideoUrl && (
                    <a href={recordedVideoUrl} download="nsccassignment_test.mp4">Download Recording</a>
                )}
            </div>
        </div>
    );
};

export default VideoRecorder;
