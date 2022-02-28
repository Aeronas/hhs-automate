
x = 0
y = 2
z = 1

a = 63-00001
b = 10
c = 20

def testthis():

    if x:
        print('It is X!')
        if z:
            print('It is Z!')
        else:
            print('It is not Z!')
    else:
        print('It is not X!')


    print('This is the END!')


testthis()



def VerifyProjInfo(num, m, d):

    if len(num) == 8:
        if int(m) > 0 and < 13:
            if int(d) > 0 and < 32:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


VerifyProjInfo(a, b, c)
