#Python Project
#Submitted to ICFOSS
#pip install plotly==4.8.1(install needed for running the program )

import numpy as np               
from plotly.offline import plot
import plotly.graph_objects as go

ch='y' #initialisation of varaiable ch

v = np.array([[0,0,0],[0,0.5,0],[0.25,0.5,0],[0.25,0,0],
              [0,0,1],[0,0.5,1],[0.25,0.5,1],[0.25,0,1]])   #Array used to specify the coordinates of the cuboid.

v1 = np.zeros((22,3),float)  #Array used for scatter plot

for i in range(11):
    if i == 4:
        v1[i]=v[i-4]
    elif i == 9:
        v1[i]=v[i-5]
    elif i == 8:
        v1[i]=v[7]
    elif i < 4:
        v1[i]=v[i]
    elif i > 4  and i <= 7:
        v1[i]=v[i-1]

v1[10]=v[0]
v1[11]=v[1]
v1[12]=v[5]
v1[13]=v[4]
v1[14]=v[0]
v1[15]=v[3]
v1[16]=v[2]
v1[17]=v[6]
v1[18]=v[5]
v1[19]=v[3]
v1[20]=v[3]
v1[21]=v[7] #inputting values into array v1


x,y,z=v.T     
#storing x comps in x, y comps in y and z comps in z using array unpacking.
x1,y1,z1=v1.T


print("The 3D object is a Rectangular Cuboid (The output will be displayed in the browser)")
fig=go.Figure() #for plotting the 3D object
fig.add_trace(go.Scatter3d(x=x1,y=y1,z=z1,mode='lines+markers'))
fig.add_trace(
    go.Mesh3d(x=x, y=y, z=z,
                   alphahull=1,
                   opacity=1,
                   color='orange')
    )

plot(fig) #command to display the cuboid


while(ch=='y' or ch=='Y'): #loop condition
    
    print("\nEnter rotation angles \n" ) 
    a=float(input("Enter angle 'a' in terms of degrees (rot along x-axis) : "))
    b=float(input("Enter angle 'b' in terms of degrees (rot along y axis) : "))
    c=float(input("Enter angle 'c' in terms of degrees (rot along z axis) : "))
    
     #Creation and initialisation of rotation matrices
    X=np.zeros((3,3),float)
    Y=np.zeros((3,3),float)
    Z=np.zeros((3,3),float)
    p=np.zeros((8,3),float)
    
    X[0,0]=1
    X[1,1]=np.cos(a*(np.pi/180))
    X[1,2]=np.sin(a*(np.pi/180))
    X[2,1]=-np.sin(a*(np.pi/180))
    X[2,2]=np.cos(a*(np.pi/180))
    print("\n Rotation matrix about x axis; X = \n",X)
    Y[1,1]=1
    Y[0,0]=np.cos(b*(np.pi/180))
    Y[0,2]=np.sin(b*(np.pi/180))
    Y[2,0]=-np.sin(b*(np.pi/180))
    Y[2,2]=np.cos(b*(np.pi/180))
    print("\n Rotation matrix about y axis; Y = \n",Y)
    Z[2,2]=1
    Z[0,0]=np.cos(c*(np.pi/180))
    Z[0,1]=np.sin(c*(np.pi/180))
    Z[1,0]=-np.sin(c*(np.pi/180))
    Z[1,1]=np.cos(c*(np.pi/180))
    print("\n Rotation matrix about z axis; Z = \n",Z)
    
    #Matrix multiplication
    R=np.dot(X,np.dot(Y,Z))
    print("\nRotational Matrix = X*Y*Z = \n",R)
    
    print("\n Old Coordinates = \n",v)
    p=np.dot(v,R)
    print("\n New coordinates = R*X_old = \n",p)
    
    v1 = np.zeros((22,3),float)  #Array used for scatter plot

    for i in range(11):
        if i == 4:
            v1[i]=p[i-4]
        elif i == 9:
            v1[i]=p[i-5]
        elif i == 8:
            v1[i]=p[7]
        elif i < 4:
            v1[i]=p[i]
        elif i > 4  and i <= 7:
            v1[i]=p[i-1]

    v1[10]=p[0]
    v1[11]=p[1]
    v1[12]=p[5]
    v1[13]=p[4]
    v1[14]=p[0]
    v1[15]=p[3]
    v1[16]=p[2]
    v1[17]=p[6]
    v1[18]=p[5]
    v1[19]=p[3]
    v1[20]=p[3]
    v1[21]=p[7] #inputting values into array v1


    x,y,z=p.T     
    #storing x comps in x, y comps in y and z comps in z using unpacking.
    x1,y1,z1=v1.T


    print("The 3D cuboid after rotation (The output will be displayed in the browser)")
    fig=go.Figure() #for plotting the 3D object
    fig.add_trace(go.Scatter3d(x=x1,y=y1,z=z1,mode='lines+markers'))
    fig.add_trace(
        go.Mesh3d(x=x, y=y, z=z,
                       alphahull=1,
                       opacity=1,
                       color='orange')
        )

   
    plot(fig) #result output
    
   
    ch=input("Want to rotate again? (Y/N) : ")

