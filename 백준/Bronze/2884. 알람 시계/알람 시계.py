H, M = map(int,input().split())
if M-45<0:
    M = 60 + (M-45)
    H = H - 1
    if H<0:
        H = 23
        print (f"{H} {M}")
    else:
        print (f"{H} {M}")
else: 
    M = M - 45
    print (f"{H} {M}")