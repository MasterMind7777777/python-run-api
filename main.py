



def accept_user_input(name, code, par=[], values=[]):
    f = open("demofile.txt", "w")
    f.write(code)
    f.close()

    exec(open("./demofile.txt").read())
    #exec(code)


accept_user_input("test name", "print('test msg')\nprint('test msg2')")