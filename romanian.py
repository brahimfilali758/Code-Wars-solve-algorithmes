
def solution(n):

	if n >= 4000 : return
	dic = { 1    : "I" ,
			2    : "II" ,
			3    : "III" , 
			4    : "IV" , 
			5    : "V" ,
			6    : "VI" ,
			7    : "VII" ,
			8    : "VIII" ,
			9    : "IX" ,
			10   : "X" ,
			20   : "XX" , 
			30   : "XXX" ,
			40   : "XL" ,
			50   : "L" ,
			60   : "LX" , 
			70   : "LXX" ,
			80   : "LXXX" , 
			90   : "XC" ,
			100  : "C" ,
			200  : "CC" ,
			300  : "CCC" ,
			400  : "CD" ,
			500  : "D" ,
			600  : "DC" ,
			700  : "DCC" ,
			800  : "DCCC" ,
			900  : "CM" ,
			1000 : "M" ,
			2000 : "MM" ,
			3000 : "MMM"
			}
	
	result = ""

	def first_step(n):
		lis = []
		for i in range(len(str(n))) :
			num = int(str(n)[i]) * (((10**(len(str(n)) - (i + 1) ) )))
			if not num == 0 : lis.append(num)
		return lis

	for i in first_step(n) :
		if i in dic :
			result +=  dic[i]
		else : print(i)
	return result


print(solution(984))
