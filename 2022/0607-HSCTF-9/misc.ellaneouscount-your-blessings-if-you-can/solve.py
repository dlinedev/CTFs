#查到主要使用deMoivre公式，具體原因沒了解
import gc,sys,time
from multiprocessing import Pool
sys.setrecursionlimit(1000000000)

def poss(k,n,m=2):
    p=[0]*(n+1)
    for i in range(0,n+1):    
        if i == k:
            p[i] = 1/2**k * m
        elif i > k:
            if m == 1:
                p[i] = p[i-1] + (1-p[i-k-1])/2**(k+1)
            elif m == 2:
                p[i] = p[i-1] + (1-p[i-k])/2**k
    return p[n]

def possB(k,n):
    p=[0]*(n+1)
    for i in range(0, n+1):    
        if i == k:
            p[i] = 1/2**k
        elif i > k:
            p[i] = p[i-1] + (1-p[i-k-1])/2**(k+1)
    return p[n]
 
def possC(k,count):
    gc.collect
    max = 1000000000
    s = 2**(k+1)
    p=[0]*(max+1)
    for i in range(0, max+1):    
        if i == k:
            p[i] = 1/2**k
        elif i > k:
            p[i] = p[i-1] + (1-p[i-k-1])/s
        if (p[i]>0.5):
            print("連續",k,"次 大於50%需要拋",i,"次" )
            break
        if i == max:
            count+=max
            px=[0]*(k+1)
            for j in range(0, k+1):
                px[j]=p[max+1-k-1+j]
            del p,i,max
            possD(k, px, count)
    
def possD(k, px, count):
    gc.collect
    max = 1000000000
    s = 2**(k+1)
    p=[0]*(max+1)
    for i in range(0,k+1):
        p[i]=px[i]
    for i in range(k+1, max+1):
        p[i] = p[i-1] + (1-p[i-k-1])/s
        count+=1
        if (p[i]>0.5):
            print("連續",k,"次 大於50%需要拋",count,"次" )
            break
        if i == max:
            pxx=[0]*(k+1)
            for j in range(0, k+1):
                pxx[j]=p[max+1-k-1+j]
            del p,i
            possD(k, pxx, count)

if __name__ == '__main__':

    # num = 375
    count = 0
    # ans = possC(num, count)

    for k in range(300,400):
        ans = possC(k, count)