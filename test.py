import cv2
from datetime import datetime

video = cv2.VideoCapture(
    r'C:\Users\abdul\Desktop\Python Videos\VID-20171220-WA0022.mp4')

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('filename.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         60, size)

# speed increase and text will be written
while True:
    ret, frame = video.read()  # read frame/image one by one

    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    text = "Live Streaming"

    if not ret:
        break

    font = cv2.FONT_HERSHEY_SIMPLEX  # font to apply on text
    cv2.putText(frame, current_time, (50, 50), font,
                1, (0, 0, 255), 2)  # add text on frame
    result.write(frame)


video.release()  # release video capture object
result.release()  # release video capture object
cv2.destroyAllWindows()  # destroy all frame windows
