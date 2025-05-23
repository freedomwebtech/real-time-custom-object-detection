import cv2
import os

# Number of images to capture
num_images = 30  # Change this to capture more or fewer images

# Directory to save images
save_dir = 'images'
os.makedirs(save_dir, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

count = 0
while count < num_images:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(1020,600))
    if not ret:
        print("Failed to capture image.")
        break

    # Display the frame
    cv2.imshow("Webcam - Press 'q' to Quit", frame)

    # Save the image
    img_name = os.path.join(save_dir, f'snickers{count+1:03}.jpg')
    cv2.imwrite(img_name, frame)
    print(f"Saved {img_name}")
    count += 1

    # Delay between captures (optional)
    cv2.waitKey(500)  # 500 ms delay

    # Optional early exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Image capture complete.")
