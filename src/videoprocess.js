// Function to save the recorded video to a specific directory
export const saveVideoToDirectory = (videoBlob, fileName) => {
  const url = URL.createObjectURL(videoBlob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = fileName;
  anchor.click();
  URL.revokeObjectURL(url);
};
