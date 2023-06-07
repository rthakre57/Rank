Matrix=[]
n=int(input("Enter N for NxN matrix:"))
print("Enter the elemnts::>")
for i in range(n):
	row=[]
	for j in range(n):
		row.append(int(input()))
	Matrix.append(row)
print(Matrix)
print("Matrix A in matrix form")
for i in range(n):
	for j in range(n):
		print(Matrix[i][j], end=" ")
	print()	
 
for k in range(n):
	B_k=[]
	for i in range(n):
		row1=[]
		for j in range(n):
			if (k==0):
				row1.append(int(Matrix[i][j]))
			else:
				for l in range(k-1,k):
					row1.append(int(B_l[i][j]))
					break
		B_k.append(row1)

	print(B_k)
	for l in range(k,n):
		B_l=[]
		for i in range(n):
			row1=[]
			for j in range(n):
				row1.append(int(0))
			B_l.append(row1)
		print(B_l)
		for m in range(k,k+1):
			for i in range(0,m+1):
				for j in range(n):
					B_l[i][j]+=int(B_k[i][j])
				
			for i in range(m+1,n):
				for j in range(m,n):
					B_l[i][j]+=int(B_k[i][j]*B_k[m][m])-(B_k[i][m]*B_k[m][j])

			for c in range(l+1,n):
				for d in range(l+1,n):
					B_l[c][d]=B_l[c][d]/B_l[l][l]
					

			#for c in range(l,n-1):
			#	B_l[c+1][c+1]=B_l[c+1][c+1]/B_l[l][l]		
			break

		print("After %d operation:" %l)
		for r in B_l:
			print(r)
		break
	
G=[]
for i in range(1):
	for j in range(n):
		G.append(int(0))
print(G)

rank=0
for i in range(n):
	if (B_l[i]==G):
		rank+=0
	else:
		rank+=1
print("Rank of Matrix A is :")
print(rank)


Output 
Enter N for NxN matrix:3
Enter the elemnts::>
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Matrix A in matrix form
1 2 3
4 5 6
7 8 9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
After 0 operation:
[1, 2, 3]
[0, -3.0, -6.0]
[0, -6.0, -12.0]
[[1, 2, 3], [0, -3, -6], [0, -6, -12]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
After 1 operation:
[1, 2, 3]
[0, -3, -6]
[0, 0, -0.0]
[[1, 2, 3], [0, -3, -6], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
After 2 operation:
[1, 2, 3]
[0, -3, -6]
[0, 0, 0]
[0, 0, 0]
Rank of Matrix A is :
2
