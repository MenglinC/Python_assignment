#import modules
from Bio.Seq import Seq

#input vector:
dna = "ATGCGGTCAGATAGTATCGATCATGCA" #字符串vector,输入的DNA片段
codon_map = {                       #字典,存放RNA翻译成蛋白质的密码子表，一一对应;
"AUA":"I","AUC":"I","AUU":"I","AUG":"M",
"ACA":"T","ACC":"T","ACG":"T","ACU":"T",
"AAC":"N","AAU":"N","AAA":"K","AAG":"K",
"AGC":"S","AGU":"S","AGA":"R","AGG":"R",
"CUA":"L","CUC":"L","CUG":"L","CUU":"L",
"CCA":"P","CCC":"P","CCG":"P","CCU":"P",
"CAC":"H","CAU":"H","CAA":"Q","CAG":"Q",
"CGA":"R","CGC":"R","CGG":"R","CGU":"R",
"GUA":"V","GUC":"V","GUG":"V","GUU":"V",
"GCA":"A","GCC":"A","GCG":"A","GCU":"A",
"GAC":"D","GAU":"D","GAA":"E","GAG":"E",
"GGA":"G","GGC":"G","GGG":"G","GGU":"G",
"UCA":"S","UCC":"S","UCG":"S","UCU":"S",
"UUC":"F","UUU":"F","UUA":"L","UUG":"L",
"UAC":"Y","UAU":"Y","UAA":"*","UAG":"*",
"UGC":"C","UGU":"C","UGA":"*","UGG":"W"
}

#Function
def translate(dna,frame=1): #自定义一个函数,函数名为translate，输入的变量为dna和frame
	aa_seq = "" #待输出的氨基酸序列，初始化为空
	dna = Seq(dna) #add #这行是我后来添加的，主要目的是为了使用Seq模块中的函数，将一个Seq的对象赋值给变量dna
	if frame < 1 or frame >6: #要求frame的值必须要在1和6之间，如果不再，则输出报错信息
		print ("[ERROR:Frame must be between 1 and 6]")
		return None
	if frame >=4 : #如果frame大于等于4
		dna = dna.reverse_complement() #modify #这段也是我修改的，使用了biopython中的取序列逆反的函数 #结合生物学过程就是模板的那个逆反序列
		start_pos = frame -4 #翻译的起始位点的规定
	else:
		start_pos = frame -1 #翻译的起始位点的规定
	#前面的这些if else语句都是对frame的情况的判断 #这里需要理解frame究竟是什么意思

	
	rna = dna.transcribe() #modify #将序列转录成RNA
	for position in range(start_pos,len(rna)-2,3): #position是range()中的取值
		codon = rna[position:position+3] #取rna的一段作为codon
		if codon in codon_map: #如果该code是字典codon_map的键
			aa_seq += codon_map[codon] #将该键对应的值添加到aa_seq(字符串的加)
	return aa_seq

a = translate(dna,frame=4)
print (a)
