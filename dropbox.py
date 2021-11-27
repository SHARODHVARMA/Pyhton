from _typeshed import Self
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A87paGnpBwUwd4d5THFeVlGj1Uou9p5ZOo5jyTm4MnbTYXTrqN5g-GVNKub6LkmZfI7U6OTZrx00rYQicd3aBbyrKFSdGKFtXZE_J1_77yCPnUyEWG32gNmdhk1LJcpWyi4Rjfs'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :- ")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()