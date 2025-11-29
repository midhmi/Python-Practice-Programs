import cv2  # OpenCV for webcam handling and image display
import numpy as np  # NumPy for numerical operations

# Step 1: Initialize Webcam
# Open the default webcam (0 is the device ID for the first connected webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():  # Check if the webcam is accessible
    print("Error: Could not open webcam.")
    exit()

# Step 2: Define K-means Parameters
# Define the stopping criteria for K-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
# Number of clusters (K): This determines how many color groups the image will be segmented into
k = 3

# Step 3: Continuously Capture and Process Webcam Frames
while True:
    ret, frame = cap.read()  # Capture a frame from the webcam
    
    #ret: A boolean indicating whether the frame was successfully captured.
    #frame: The actual frame data, which is a 3D NumPy array representing the captured image.
    if not ret:  # If frame capture fails, exit the loop
        print("Failed to grab frame.")
        break

    # Convert the frame from BGR (default in OpenCV) to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Reshape the frame to a 2D array of pixels (num_pixels x 3 for RGB)
    pixels = frame_rgb.reshape((-1, 3)).astype(np.float32)

    # Step 4: Apply K-means Clustering
    # Cluster the pixels into k groups based on color similarity
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert cluster centers (float) to integers (valid RGB values in 0–255 range)
    centers = np.uint8(centers)

    # Replace each pixel's color with its corresponding cluster center's color
    segmented_pixels = centers[labels.flatten()]
    # Reshape the flattened array back to the original image shape
    segmented_frame = segmented_pixels.reshape(frame.shape)

    # Step 5: Display the Segmented Frame
    # Convert the segmented frame back to BGR format for OpenCV and display it
    cv2.imshow('Segmented Frame', cv2.cvtColor(segmented_frame, cv2.COLOR_RGB2BGR))

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 6: Release Resources
cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
