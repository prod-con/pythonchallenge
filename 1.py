text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newstring = ""
for a in text:
	if (a==' ' or a=='.' or a=='(' or a==')' or a=="'"): 
		newstring += a
		continue
	newstring += chr((ord(a)+2-97)%26 + 97)

print(newstring)

table = str.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')

print("map".translate(table))
