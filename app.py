def suma(a, b):
    return a + b

if __name__ == "__main__":
    print(suma(2, 3))

AWS_SECRET_ACCESS_KEY="AKIAIOSFODNN7EXAMPLE"

import subprocess

user_input = "ls"

subprocess.Popen(user_input, shell=True)