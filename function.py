def temp(c):
    f=(9/5)*c +32
    # print(f)
    return print(f)


c=input("write the temperature in celciuos ")

c=int(c)
temp(c)



def leng(m,s):
    h=m/60+ s/3600
    return print (h)

m=input ("write number of minutes")
m=int(m)
s=input ("write number of seconds")
s=int(s)

leng(m,s)
