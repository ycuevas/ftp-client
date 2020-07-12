from ftplib import FTP

def connectViaFTP():
    ftp = FTP('ftp.dlptest.com')     # connect to host, default port
    ftp.login(user='dlpuser@dlptest.com', passwd = 'SzMf7rTE4pCrf9dV286GuNe4N') 
    return ftp

def listFolders(ftpConnection):
    ftpConnection.dir()

def deleteFile():
    print('connection')

    
def main():
    ftpConnection = connectViaFTP()
    ftpConnection.retrlines('LIST')

if __name__ == "__main__":
    main()
