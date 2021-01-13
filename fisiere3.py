with open ('globulet.txt.txt', "r") as f:
    a=f.read()
t=int(a)+int(a)+3+(2*int(a)+1)
with open ("bradut.txt.txt","w") as f:
    f.write(str(t))