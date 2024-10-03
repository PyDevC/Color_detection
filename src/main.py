from masking import hsvmethod
import cv2
import sys

if __name__ == "__main__":
    for i in sys.argv[1:]:
        img = cv2.imread(f'test/images/{i}')
        hsvmethod(img)
        cv2.imshow("",img)
        if cv2.waitKey(0):
            cv2.destroyAllWindows()