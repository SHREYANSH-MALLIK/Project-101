import os
import dropbox
from dropbox.files import WriteMode

class TransferData :

    def __init__(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)

                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, made=WriteMode("overwrite"))

def main():
    access_token = 'sl.BGI510p9bzV6gxapgUpDR5gWMrTQrY6e18nUG0TrYT6c--2AFsulxxHqpOozaLo5NdxLBYEDuE8IyKyRsjMYaqGsFP0pkxJgmStAi8fTa3x1A6g7xmUZBB1L7X2F6K01Xi7-UPGc5gOj'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder name to transfer (with extenstion like .py) to upload : "))
    file_to = input("Enter the full path of file to upload : ")

    transferData.upload_file(file_from,file_to)
    print ("File has been uploaded to dropbox")

main()
        