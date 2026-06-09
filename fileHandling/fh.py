p = open("demofile.txt",'w')
p.write("hey! i created this text file.")
p.close()

r = open("demofile.txt",'r')
print(r.read())
r.close()