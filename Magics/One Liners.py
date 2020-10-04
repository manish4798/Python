### 1. Swap 2 Variables
a,b=1,2
a,b=b,a
print(a,b)

### 2. Mutliple variable assignments
a=[1,2,3,4,5,6]
s=sum(a[1::2])
print(s)

### 3. Delete multiple elements 
a=[1,2,3,4,50]
del a[::2]
print(a)

### 4. Read file into array of lines
c=[line.strip() for line in open('file.txt')]
print(c)

### 5. Write String to file
with open('file.txt','a') as f:
    f.write("\n hello world")
   
### 6. Create list from another inline list
l=[('HI '+x)for x in ["harsh","hamam"]]
print(l)

### 7. List Mapping (type change)
l=list(map(int,[1.,2.,3]))
print(l)

### 8. Palindrome Check
phrase = 'harshsra'
is_palindrome=phrase==phrase[::-1]
print(is_palindrome)
