import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i",
                  "--input",
                  dest="input_file",
                  help="GIGGLE result file name with '-s'")

parser.add_option("-o",
                  "--output",
                  dest="output_file",
                  help="Output file name")

parser.add_option("-t",
                  "--title",
                  dest="title",
                  help="the title of this figure")

(options, args) = parser.parse_args()
def addtwodimdict(thedict, key_a, key_b, val): 
    adic = thedict.keys()
    if key_a in adic:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

trait = []
M = {}
#"Hs_AluYg6.bed.gz.giggle.result"
with open(options.input_file, 'r') as f:
    next(f)
    lines = f.readlines()
    for l in lines:
        line = l.rstrip().split('\t')[0]
        line1 = line.replace("Region_sort/","")
        line2 = line1.replace("H3K27ac_Human_Brain_","")
        line3 = line2.replace("_hg38_peaks.bed.gz","")
        trait.append(line3)
        m=line3.rstrip().split('_')[1]
        n=line3.rstrip().split('_')[2]
        num=l.rstrip().split('\t')[7]
        addtwodimdict(M,m,n,num)
traits =trait[1:]
cell = []
for n in traits:
     m=n.rstrip().split('_')[1]
     cell.append(m)
cell_ls=set(cell)
cells=sorted(cell_ls)
#cells=list(set(cell)).sort()
#print(cells)
sample = []
for s in traits:
     k=s.rstrip().split('_')[2]
     sample.append(k)
samples_ls=set(sample)
samples=sorted(samples_ls)
#print(samples)
D=np.zeros([len(cells),len(samples)])
for n in traits:
     m=n.rstrip().split('_')[1]
     cell.append(m)

c = 0


for cell in cells:
    s = 0
    for sample in samples:
        D[c,s] = M[cell][sample]
        s+=1
    c+=1


row_labels = cells
column_labels = samples
data = D
fig, ax = plt.subplots(figsize=(2,3))
from matplotlib import colors as mcolors
from matplotlib.colors import Normalize

_seismic_data = ( (0.0, 0.0, 0.3), 
                  (0.0, 0.0, 1.0),
                  (1.0, 1.0, 1.0),
                  (1.0, 0.0, 0.0),
                  (0.5, 0.0, 0.0))

hm = mcolors.LinearSegmentedColormap.from_list( \
        name='red_white_blue', \
        colors=_seismic_data, N=256)

#norm=matplotlib.colors.LogNorm(vmin=data.min(), vmax=data.max()), \
print(data.min(), data.max())
import matplotlib.colors as mcolors
if(data.min()<0<data.max()):
	norm = mcolors.TwoSlopeNorm(vmin=data.min(), vmax = data.max(), vcenter=0)
	plt.pcolor(data, 
			   norm = norm,
			   cmap=hm)
	#ax.xaxis.tick_top()
	ax.set_xticklabels("")
	ax.set_yticklabels("")
	ax.xaxis.set_ticks_position('none') 
	ax.yaxis.set_ticks_position('none') 
	plt.title(options.title,   
				 fontsize = 14,
				 fontweight ="bold")
	plt.yticks(np.arange(0.1,len(row_labels)+0.1,1),row_labels, fontsize=10) #y axis
	plt.xticks(np.arange(0.5,len(column_labels)+0.5,1.0),column_labels,rotation=90, fontsize=10) #x axis
	plt.ylim((0,len(cells)))
	plt.xlim((0,len(samples)))
	plt.colorbar(pad=0.04, ticks=[data.min(), 0, data.max()])
	plt.savefig(options.output_file,bbox_inches='tight')
if(data.max()<0):
	#center_num=(data.min()+data.max())/2
	norm = mcolors.TwoSlopeNorm(vmin=data.min(),vcenter=0,vmax =1)
	plt.pcolor(data, 
			   norm = norm,
			   cmap=hm)
	#ax.xaxis.tick_top()
	ax.set_xticklabels("")
	ax.set_yticklabels("")
	ax.xaxis.set_ticks_position('none') 
	ax.yaxis.set_ticks_position('none') 
	plt.title(options.title,   
				 fontsize = 14,
				 fontweight ="bold")
	plt.yticks(np.arange(0.1,len(row_labels)+0.1,1),row_labels,fontsize=10) #y axis
	plt.xticks(np.arange(0.5,len(column_labels)+0.5,1.0),column_labels,rotation=90, fontsize=10) #x axis
	plt.ylim((0,len(cells)))
	plt.xlim((0,len(samples)))
	plt.colorbar(pad=0.04, ticks=[data.min(),0,1])
	plt.savefig(options.output_file,bbox_inches='tight')
if(data.min()>0):
	#center_num=(data.min()+data.max())/2
	norm = mcolors.TwoSlopeNorm(vmin=-1,vcenter=0,vmax =data.max())
	plt.pcolor(data, 
			   norm = norm,
			   cmap=hm)
	#ax.xaxis.tick_top()
	ax.set_xticklabels("")
	ax.set_yticklabels("")
	ax.xaxis.set_ticks_position('none') 
	ax.yaxis.set_ticks_position('none') 
	plt.title(options.title,   
				 fontsize = 14,
				 fontweight ="bold")
	plt.yticks(np.arange(0.1,len(row_labels)+0.1,1),row_labels,fontsize=10) #y axis
	plt.xticks(np.arange(0.5,len(column_labels)+0.5,1.0),column_labels,rotation=90,fontsize=10) #x axis
	plt.ylim((0,len(cells)))
	plt.xlim((0,len(samples)))
	plt.colorbar(pad=0.04, ticks=[-1,0,data.max()])
	plt.savefig(options.output_file,bbox_inches='tight')