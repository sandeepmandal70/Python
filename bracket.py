inputiop = input()
inlist = list(inputiop)
z = [ord(i) for i in inlist]
# print(z)
print(z.count(40))
print(z.count(41))

if z.count(40)<z.count(41):
    print(z.count(40))
else:
    print(z.count(41))
