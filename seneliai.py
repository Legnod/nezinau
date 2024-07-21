# Pradzia
a = 0
zaidziam = True

# if programa
while zaidziam == True:
    kait = int(input("Ar nori prideti?(1/0)"))
    if kait == 1:
        a = a+1
        print(a)
        testi = int(input("Ar nori testi programa?(1/0)"))
        if testi == 1:
            zaidziam = True
        elif testi == 0:
            zaidziam = False
        else:
            print("neteisingai idetos instrukcijos")
    elif kait == 0:
        a = a+0
        print(a)
        testi = int(input("Ar nori testi programa?(1/0)"))
        if testi == 1:
            zaidziam = True
        elif testi == 0:
            zaidziam = False
        else:
            print("neteisingai idetos instrukcijos")
    else:
        print("netinkamai idetos instrukcijos")
        testi = int(input("Ar nori testi programa?(1/0)"))
        if testi == 1:
            zaidziam = True
        elif testi == 0:
            zaidziam = False
        else:
            print("neteisingai idetos instrukcijos")
