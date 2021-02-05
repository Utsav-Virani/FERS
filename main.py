import cv2
import face_recognition

stream = cv2.VideoCapture('http://192.168.0.105:4747/video')
# stream = cv2.VideoCapture(r'E:\Series\The Vampire Diaries\Session 3\The.Vampire.Diaries.S03E01.720p.mkv')


face_locations = []

while True:
    # r, f = stream.read()
    r, frame = stream.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('IP Camera stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
