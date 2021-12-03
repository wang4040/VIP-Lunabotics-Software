
import sys
import cv2

mosse_tracker = cv2.legacy.TrackerMOSSE_create()
video_capture = cv2.VideoCapture(0)

if not (video_capture.isOpened()):
    sys.exit()

check, screen = video_capture.read()

if not (check):
    sys.exit()

output = (300, 20, 90, 400)
output = cv2.selectROI(screen, False)
check = mosse_tracker.init(screen, output)

while True:
    check, screen = video_capture.read()
  
    if not (check):
        break

    timer = cv2.getTickCount()
    check, output = mosse_tracker.update(screen)

    if (check):
        xPosition = (int(output[0]), int(output[1]))
        yPosition = (int(output[0] + output[2]), int(output[1] + output[3]))
       
        cv2.rectangle(screen, xPosition, yPosition, (255,0,0), 2, 1)

    cv2.imshow("Tracking", screen)
    esc = cv2.waitKey(1) & 0xff

    if (esc == 27):
        break

