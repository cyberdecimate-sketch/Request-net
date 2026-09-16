#The request network works by splitting data into parts and then reassembling them at the end, but with the definitions fixed. This is a code demonstration. 
x = "abcefghijklmnopQrstuvwxy"

a1 = "abcefghi"
b1 = "jklmnopQ"
c1 = "rstuvwxy"

if x == x:
    a = a1
    b = b1
    c = c1
    print(a + b + c == x)
