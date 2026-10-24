import io

s1="WORD"
print ("original string:", s1, " type:", type(s1))

sio=io.StringIO(s1)
print ("sio:", sio, " type:", type(sio))

sio.seek(3)
sio.write("LD")
s1=sio.getvalue()

print ("Modified string:", s1, " type:", type(s1))