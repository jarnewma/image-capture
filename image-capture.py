import cv2 as cv
fourcc = cv.VideoWriter_fourcc(*'XVID')

cap = cv.VideoCapture(0)
out = cv.VideoWriter('output.mp4', fourcc, 30.0, (1280, 720))

print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()