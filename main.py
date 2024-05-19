import cv2
import pathlib
import datetime

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))
camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = camera.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 3)
        snapshot_filename = f'snapshot_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        cv2.imwrite(snapshot_filename, frame)
    
    cv2.putText(frame, f'Faces count: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Faces', frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()
