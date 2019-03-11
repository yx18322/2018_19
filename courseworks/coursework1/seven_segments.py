#for the submission uncomment the submission statements
#see submission.README

from math import *

from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=map(to_bool,pattern)

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
        
submission=Submission("Mohit_Bhardwaj")
submission.header("Mohit Bhardwaj")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

def weight_matrix(x_v):
N = len(x_v)
w = np.zeros([N,N])
for i in range(N):
        for j in range(i,N):
            if i==j:
                w[i,j] = 0
            else:
                w[i,j] = x_v[i]*x_v[j]
                w[j,i] = w[i,j]
    return w
##this assumes you have called your weight matrix "weight_matrix"
submission.section("weight matrix")
def update(W,weight):
W_ = np.zeros_like(W)
N = len(W)
m = 0
for i in range(N):
            m = W[i]+np.dot(weight[i][:],W)
            if m > 0:
                W_[i]=1
            else:
                W_[i]=-1
 
    return W_


def energy(W,weight):
N = len(W)
E = 0
for i in range(N):
       for j in range(N):
           E = E-W[i]*weight[i,j]*W[j]/2.0
    print(E)
    return E
submission.matrix_print("W",weight)
weight = (weight_matrix(one) + weight_matrix(three) + weight_matrix(six)) / 3.0
#print out the energy of the three learned patterns
print("the energy of the three learned patterns")
energy(W=one,weight=weight)
energy(W=six,weight=weight)
energy(W=three,weight=weight)
print("test1")
submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

seven_segment(test)
submission.seven_segment(test)
##for COMSM0027
flag =0
while(flag <1):
    a=energy(test=test1,weight=weight)
    b=update(test=test1,weight=weight)
   
##where energy is the energy of test
submission.qquad()
submission.print_number(energy)
c=energy(test=b,weight=weight)
   
##this prints a space
submission.qquad()
if a-c==0:
        print(b)
        flag=0
else:
        flag=2

#here the network should run printing at each step
#for the final submission it should also output to submission on each step
seven_segment(b)

print("test2")
submission.section("Test 2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]

seven_segment(test)

submission.seven_segment(test)
flag_=0
while (flag_ < 1):
    a_=energy(test=test2,weight=weight)
    b_=update(test=test2,weight=weight)
    c_=energy(test=b_,weight=weight)
    
##for COMSM0027
##where energy is the energy of test
submission.qquad()
submission.print_number(energy)
if a_-c_==0:
        print(b_)
        flag_=0
else:
        flag_=2

##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step
seven_segment(b_)

submission.bottomer()
