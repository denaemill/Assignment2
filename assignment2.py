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

        if len(string) < 10:
            return False
        if ord(string[0]) < 97 and ord(string[0]) > 122:
            return False


        i = 0
        count = 0
        while i < len(string):
            if string[i].isdigit():
                count = count + 1
            if count > 1:
                return False
            i = i + 1

        return True


    # Task 6
    @staticmethod
    def connectTcp(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        HOST = host
        PORT = port

        sock.bind((HOST, PORT))
        sock.listen(5)
        print('Waiting for incoming connections on', sock)
        conn, addr = sock.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                conn.send(data)

        conn.close()
        sock.close()
