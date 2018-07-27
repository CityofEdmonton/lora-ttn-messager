import subprocess

proc = subprocess.Popen("./thethingsnetwork-send-v1",
stdin=subprocess.PIPE,stdout=subprocess.PIPE)

proc.stdin.write(b'haha')
proc.stdin.write(b'q')

data = 0
	val = proc.stdout.read(1)
	print(val)
	data =  1
