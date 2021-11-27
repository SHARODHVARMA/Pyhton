import cv2
import time
import random
import dropbox

startTime=time.time()
def take_snapshot():
    number=random.randinit(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print("Snapshot is Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token="sl.A8-SoPKZDz62oIsvg6saK_DfE3VwZ0qU42GTuo6ru4C-J4oUxiyErkUPwNk-1UO2j9pL7mcYE6zZ8Ocqe0msWlYQpNKP66Ai59eoZuWVXzQXgbrq_mvOe4bsJhMgkdxLXUXWMWQ"
    file=img_name
    file_from=file
    file_to="/testFolder/" + (img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File is Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>= 5):
            name=take_snapshot()
            upload_file(name)

main()