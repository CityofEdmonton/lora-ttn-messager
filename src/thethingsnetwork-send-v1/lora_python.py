import pexpect
child = pexpect.spawn ("./thethingsnetwork-send-v1")
while(1):
	child.expect('waiting')
	child.sendline('12')
	print(child.before, child.after)
