def function (a):
    if len(a[0]) >= len(a[1]):
        print(a[0])
    else:
        print(a[1])

a= input()
a = a.split(", ")

function(a)
