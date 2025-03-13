import numpy as np
import cv2 as cv
import datetime

cam = cv.VideoCapture(0)
mode = 0

fourcc = cv.VideoWriter_fourcc(*'DIVX')
width = int(cam.get(3))
height = int(cam.get(4))

out = None

fps_table = [10, 20, 30]
fps_index = 2

format_table = ['.mp4', '.avi']
format_index = 0

while True:
    ret, frame = cam.read()

    if mode == 0:
        cv.putText(frame, 'Preview mode: Press Space to start recording', (30, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv.putText(frame, 'Current FPS:' + str(fps_table[fps_index]), (30, 60), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv.putText(frame, 'Current Save Format: '+ str(format_table[format_index]), (30, 90), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    elif mode == 1:
        if out is not None:
            out.write(frame)
        cv.putText(frame, 'Recording...', (30, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv.imshow('Joy Recorder', frame)

    key = cv.waitKey(1)
    if key == 27:
        if mode == 1:
            out.release()
        break
    elif key == 32:
        if mode == 0:
            mode = 1
            filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + format_table[format_index]
            out = cv.VideoWriter(filename, fourcc, fps_table[fps_index], (width, height))
        elif mode == 1:
            mode = 0
            out.release()
            out = None
    elif key == ord('<') or key == ord(','):
        fps_index = max(0, fps_index - 1)
    elif key == ord('>') or key == ord('.'):
        fps_index = min(len(fps_table)-1, fps_index + 1)
    elif key == ord('f'):
        format_index = 1 - format_index


cam.release()
cv.destroyAllWindows()