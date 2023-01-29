import socket

class Assignment2:
    # Task 1
    def __init__(self, year):
        self.year = year
        self.year = int(self.year)
        self.currentYear = 2023

    # Task 2
    def tellAge(self, currentYear):
        self.currentYear = currentYear
        self.currentYear = int(self.currentYear)
        age = abs(self.currentYear - self.year)
        print("Your age is %d" % age)

    # Task 3
    def listAnniversaries(self):
        test = abs(self.year - self.currentYear)
        ani = []
        i = 0

        while i < test:
                if i == 0:
                    i = i + 10
                else:
                    ani.append(i)
                    i = i + 10

        return ani

    # Task 4
    def modifyYear(self, n):
        strYear = str(self.year)
        st = ""

        for i in range(0, n):
            st = st + strYear[0:2]

        result = self.year * n
        strResult = str(result)

        st = st + strResult[::2]

        return st

    # Task 5
    @staticmethod
    def checkGoodString(string):

        tf = True

        if len(string) < 9:
            tf = False
        if string[0].isupper():
            tf = False


        count = 0
        for i in range(0, len(string)):
            if string[i].isdigit():
                count = count + 1

        if count != 1:
            tf = False

        return tf


    # Task 6
    @staticmethod
    def connectTcp(host, port):
        host = socket.gethostbyname(host)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        sock.bind((host, port))
        sock.listen(1)
        print('Waiting for incoming connections on', sock)
        conn, addr = sock.accept()

        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)

            if not data:
                break
            conn.send(data)

        conn.close()
        sock.close()
        return True


##if retval:
    #print("Connection established correctly")
#else:
    #print("Some error")
