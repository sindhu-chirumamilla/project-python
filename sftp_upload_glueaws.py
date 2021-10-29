import boto3
import pysftp

"""
This is the functionality which will be used to
upload a file which is in S3 to an sftp server 
using AWS Glue. So this code will go in the place 
of your Glue script. The package used for SFTP
transfer is "pysftp".
"""

def sftp_upload():
    try:
        s3 = boto3.resource('s3')
        # download the file to /tmp folder in glue from s3
        s3.Bucket('bucket').download_file('key/filename.extension','/tmp/filename.extension')
        # make sure your key dont have '/' in the beginning of your key , it should be something like 'my_folder/my_file.txt'
        print('file downloaded to /tmp')
        host = 'ip address of host or dns name'
        username = 'user'
        password = 'password'
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        # establish connection to server using pysftp
        with pysftp.Connection(host, username=username, password=password,cnopts=cnopts) as sftp:
            print('putting file')
            sftp.put('/tmp/filename.extension', 'path_to_upload')

        print('Upload done.')

    except Exception as e:
        print(e)
        raise e
def main():
    sftp_upload()

if __name__ == "__main__":
    main()

