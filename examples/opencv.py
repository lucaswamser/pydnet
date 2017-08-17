
import pydnet as dnet
import threading
import time
import base64
net = dnet.loadNetwork("/var/trains/generico/net.cfg", "/var/trains/generico/net.weights", "/var/trains/generico/net.names")

def functiont(b64,n):
	im = dnet.loadImageBase64(b64)
	r = dnet.classify(n,im,0.4)
	dnet.drawDetections(im,r)
	return dnet.getImageBase64(im)


#functiont(net)
#functiont(net)
#functiont(net)

import numpy as np
import cv2

cap = cv2.VideoCapture("BRANDING.mp4")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    b = base64.b64encode(cv2.imencode('.jpg', frame)[1])
    r = functiont(b,net)

    nparr = np.fromstring(base64.b64decode(r), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

    # Display the resulting frame
    cv2.imshow('frame',img_np)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
