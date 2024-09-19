# FOR
# IMPORTANTE!!!
# The range function outputs an ordered sequence as a list “i”.

range(3) # te muestra todos los números antes de ese 
range(10,15) # en este caso te da los números comenzando el 10, pero sin contar el 15

squares = ["red","yellow","green","purple","blue"]
for i in range(0,5):        #T he range function outputs an ordered sequence as a list “i”.
    squares[i]="white"

triangles = ["red","yellow","green"]    # Here is the list triangles. Each iteration of the list we pass one element 
for triangle in triangles:              # of the list triangles to the variable triangle.
    triangle                            # For the first iteration, the value of triangle is red, for the second, yellow...

squares = ["red","yellow","green"]      # For the girst iteration, the value of the variable square is red,  
for i,square in enumerate(squares):     # corresponding to the zeroth index, and the value o "i" is zero
    square                              # pasa como con los dictionaries más o menos 
    i

# Use Loops to print out the elements in the list A:
A=[3,4,5]
for i in A:
    print(i)
# 3
# 4
# 5

# WHILE

circles = ["orange","orange","purple","orange","blue"]
newcircles=[]
i=0

while(circles[i]=="orange"):    # mientras los círculos sean naranjas, se van a agregar a la lista newcircles
    newcircles.append(circles[i])
    i=i+1                       # comienza con el primer círculo porque i = 0 -> primer lugar, luego se le suma 1
print(newcircles)               # para que continúe hasta que se tope un círculo que no sea naranja y se pare

# Find the value of x that will print out the sequence 1,2,3,4,5,6,7,8,9,10
x=11
y=1
while(y != x):
    print(y)
    y=y+1