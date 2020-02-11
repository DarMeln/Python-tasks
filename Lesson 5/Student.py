class Student(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.conf = kwargs
        self.labs = [0] * self.conf['lab_num']
        self.labs_try = [0] * self.conf['lab_num']
        self.exam = 0
        self.exam_done = False

    def make_lab(self, m, n = -1):
        if m > self.conf['lab_max']:  # If greater than max -> than it's max
            m = self.conf['lab_max']
        if n >= self.conf['lab_num']:  #  Other labs does not count
            return self
        if n == -1:  # No number was given
            try:
                n = self.labs.index(0)
            except:  # If all labs have been done
                print('Please, specify the lab number')
                return self
        if self.labs_try[n] > 2:  # 3 tries
            print('You can\'t do this task anymore')
            return self
        self.labs[n] = m
        self.labs_try[n] += 1
        return self

    def make_exam(self, m):
        if m > self.conf['exam_max']:
            m = self.conf['exam_max']
        self.exam = m
        self.exam_done = True
        return self

    def is_certified(self):
        maximum = (self.conf['exam_max']
                   +self.conf['lab_num']*self.conf['lab_max'])
        res = (sum(self.labs) + self.exam)/maximum
        return res, res >= self.conf['k']


conf = {'exam_max': 30,
        'lab_max': 7,
        'lab_num': 10,
        'k': 0.61}
print('Please, enter your name')
name = input()
student = Student(name, **conf)
while True:
    print('Choose a number\n1 - Make a lab\n2 - Exam\n3 - Get certified')
    c = int(input())  # Choice
    if c == 1:
        print('Enter a mark and a number of lab:')
        mn = input()
        try:
            m, n = list(map(int, mn.split()))
            student.make_lab(m, n)
        except:
            m = int(mn)
            student.make_lab(m)
    elif c == 2:
        if student.exam_done == True:
            print('You already did the exam')
        else:
            print('Enter a mark for your exam:')
            m = int(input())
            student.make_exam(m)
    elif c == 3:
        print(student.is_certified())
        break
    else: print('Not a choice')
