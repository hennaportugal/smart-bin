import cv2
from darkflow.net.build import TFNet
import numpy as np
import time


options = {
    'model': 'cfg/yolo-3c.cfg',
    'load': 6558,
    'threshold': 0.35,
    'gpu': 1.0
}


tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
        cv2.imshow('frame', frame)
        # ~ k=cv2.waitKey(0)
        
        # ~ if k == ord('s'):
            # ~ cv2.imwrite('captured.jpg', frame)
        
        # ~ cv2.flip(frame, 0)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
