##width = 30
##m = 30
##n = 80
##
##for i in range(m):
##	rem = n - 2*width - 2*i
##	if(rem <= 0):
##		break
##	print("'#" + '0'*i + '1'*width + '0'*rem + '1'*width + '0'*i + "' +")
##
##for j in range(m):
##	i = m-j
##	rem = n - 2*width - 2*i
##	if(rem >= 0):
##		print("'#" + '0'*i + '1'*width + '0'*rem + '1'*width + '0'*i + "' +")


width = 12
m = 30
n = 50

rem = n - 2*width
i = 0

while(rem != 0):
	rem = n - 2*width - 2*i
	print("'#" + '0'*i +'1'*width + '0'*rem + '1'*width + '0'*i + "' + ")
	i += 1

print("\n\n")

rem = n - 2*width
while(i >= 0):
	rem = n - 2*width - 2*i
	print("'#" + '0'*i +'1'*width + '0'*rem + '1'*width + '0'*i + "' + ")
	i -= 1
