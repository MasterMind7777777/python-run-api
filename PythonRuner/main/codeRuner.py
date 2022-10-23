import os.path
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old



def accept_user_input(name, code, par=[], values=[]):
    path = os.path.dirname(__file__) + "/../execFiles/" + name + ".txt"
    f = open(path, "w")

    extra_params = ""
    count = 0
    for p in par:
        extra_params = extra_params + p + " = " +  values[count] + "\n"
        count = count + 1
    

    f.write(extra_params + code)
    f.close()



    code_file = open(path).read()
    exec(extra_params)
    with stdoutIO() as s:
        exec(code)

    return (s.getvalue())


x = accept_user_input("test name", "print(\"test msg1\")\nprint(\"test msg2\")\nprint(num1)", ["num1", "num2","num3"], ["1", "2", "3"])
print("x = ", x)