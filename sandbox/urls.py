s = open("sandbox//url11.txt","a")
i=1205
while i>1105:
    s.write("https://admitere.usm.md/?attachment_id="+str(i)+"\n")
    i-=1
s.close()
