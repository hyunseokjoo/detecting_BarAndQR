import cv2
import pyzbar.pyzbar as pyzbar

font = cv2.FONT_HERSHEY_SIMPLEX

def read_frame(frame):
    try:
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, barcode_info, (x , y - 20), font, 0.5, (0, 0, 255), 1)

        return frame
    except Exception as e:
        print(e)


def main():
    try:
        cap = cv2.VideoCapture("barcode.mp4")
        while cap.isOpened():
            ret, frame = cap.read()
            print(type(frame))
            print(type(""))
            if ret:
                frame = read_frame(frame)
                cv2.imshow("barcode reader", frame)
                if cv2.waitKey(1) == 27:
                    break
            else:
                print("예외")
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

