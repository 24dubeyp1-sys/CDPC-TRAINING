#1ST:- TO CHANGE A PROFILE PHOTO 

L = int(input().strip())
N = int(input().strip())

for _ in range(N):
    W, H = map(int, input().split())
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")



#2ND:- MONK AND ROTATION

T = int(input().strip())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    K = K % N  
    

    result = A[N-K:] + A[:N-K]
    
    print(*result)
  

# 3RD:- Toggle String

S = input().strip()
result = ""

for x in S:
    if x.islower():
        result += x.upper()
    else:
        result += x.lower()

print(result)
  
