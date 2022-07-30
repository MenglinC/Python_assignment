import numpy as np

def smith_waterman(s1,s2,match =1,mismatch=-1,gap=-1):
	n = len(s1)+1
	m = len(s2)+1
	matrix = np.zeros((n,m))
	traceback = np.zeros((n,m))
	for i,a1 in enumerate(s1):
		for j,a2 in enumerate(s2):
			if a1==a2:
				score1 = matrix[i,j]+match
			else:
				score1 = matrix[i,j]+mismatch
			score2 = matrix[i+1,j] + gap
			score3 = matrix[i,j+1] + gap
			score = np.max([score1,score2,score3,0])
			matrix[i+1,j+1] = score
			direction = np.argmax([score1,score2,score3])
			traceback[i+1,j+1] = direction
	optimal_score = np.max(matrix)
	return (optimal_score,matrix,traceback)

def local_traceback(s1,s2,matrix,traceback):
	r1 = ""
	r2 = ""
	indices = np.where(matrix==matrix.max())
	i = indices[0][0]#这里让人不理解的是一定有两个值嘛？#我现在卡的点可能在于对这里的底层逻辑不理解;
	j = indices[1][0]
	while matrix[i,j]>0: #也许有很多最大值，但取得是第一个值的最大值的坐标
		if traceback[i,j]==0:
			r1 += s1[i-1]
			r2 += s2[j-1]
			i -= 1  #坐标减一
			j -= 1
		elif traceback[i,j]==1:
			r1 += s1[i-1] #回溯的方向也不一样
			r2 += "-"
			i -= 1
		elif traceback[i,j]==2:
			r1 += "-"   #谁添加gap
			r2 += s2[j-1]
			j -= 1
	print (r1[::-1]) #最终逆序输出
	print (r2[::-1]) #最终逆序输出


s1 = "ACGTTC"
s2 = "GTTACC"
score,matrix,traceback = smith_waterman(s1,s2,match=1,mismatch=-1,gap=-1)
print("Optimal Score : %d" % score)
local_traceback(s1,s2,matrix,traceback)
