import socket

class Assignment2:
    # Task 1
    def __init__(self, year):
        self.year = year
        self.year = int(self.year)
        self.currentYear = 0

    # Task 2
    def tellAge(self, curYear):
        self.currentYear = curYear
        self.currentYear = int(self.currentYear)
        age = abs(self.currentYear - self.year)
        print("Your age is %d" % age)

    # Task 3
    def listAnniversaries(self):
        test = abs(self.year - self.currentYear)
        ani = []
        i = 10
        j = 0

        while test > 0:
                if i > test:
                    break
                else:
                    ani.append(i)
                    i = i + 10
                    j = j + 1

        print("[", end="")
        for x in range(0, j):
            if x == j - 1:
                print("%d]" % ani[x])
            else:
                print("%d, " % ani[x], end = " ")

    # Task 4
    def modifyYear(self, n):
        strYear = str(self.year)

        for i in range(0, n):
            print("%s" % strYear[0:2], end = "")

        result = self.year * n
        result = str(result)

        print("%s" % result[::2])

    # Task 5
    @staticmethod
    def checkGoodString(string):

        if len(string) < 9:
            return False
        elif ord(string[0]) < 97:
            return False

        i = 0
        count = 0
        while i < len(string):
            if string[i].isdigit():
                count = count + 1
            i = i + 1

        if count > 1:
            return False
        else:
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

