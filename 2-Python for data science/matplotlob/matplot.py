import pandas as pd
songs69=pd.Series([7,16,21,39],
index=['ram','jay','sham','adi'],
name='counts')
songs69

import matplotlib.pyplot as plt
figg=plt.Figure()
songs69.plot()
plt.legend()

songs69.plot(kind='bar')
songs69.plot(kind='bar',color='b',alpha=.5)
plt.legend()

############################################
import numpy as np
data= pd.Series(np.random.rand(500),
                name='500 random')
fig1=plt.Figure()
ax=fig1.add_subplot(111)
data.hist()
##############################3
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()
###############################################################3
#multiline plots
import matplotlib.pyplot as plt
x1=range(1,5)
plt.plot(x1,[xi*1.5 for xi in x1])
plt.plot(x1,[xi*3.0 for xi in x1])
plt.plot(x1,[xi/3.0 for xi in x1])
plt.show()
################################################################
#grid plot
import matplotlib.pyplot as plt
import numpy as np
x2=np.arange(1,5)
plt.plot(x2,x2*1.5,x2*3.0,x2/3.0 )
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x2=np.arange(1,5)
plt.plot(x2,x2*1.5,x2,x2*3.0,x2,x2/3.0 )
plt.axis()
plt.axis(0,5,-1,13)
plt.show()

##########################################################
#give lable to the x nad y axis
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.show()
##########################################################
#additing title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('graph')
plt.show()
##############################################################
#adding  legend or square box ro upper left side
import matplotlib.pyplot as plt
import numpy as np
x1=np.arange(1,5)
plt.plot(x1,x1*1.5,label='normal')
plt.plot(x1,x1*3.0,label='fast')
plt.plot(x1,x1/3.0,label='slow')
plt.legend()
plt.show()
######################################################################
#change colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

######################################################################
#change colors
#method 2
import matplotlib.pyplot as plt
import numpy as np
z=np.arange(1,3)
plt.plot(z,'y',z+1,'m',y+2,'g');
plt.show()
##############################################################3
#change line
import matplotlib.pyplot as plt
import numpy as np
z=np.arange(1,3)
plt.plot(z,'--',z+1,'-.',y+2,':');
plt.show()

###########################################################################
"""
style and markers
"""
#print line in pattern
import matplotlib.pyplot as plt
import numpy as np
z=np.arange(1,3,0.2)
plt.plot(z,'x',z+0.5,'o',z+1,'D',z+1.5,'*',z+2,'s');
plt.show()
####################################################################
#histogram charts
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y)
plt.show()

###################################################33
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])
plt.show()

######################################
import matplotlib.pyplot as plt
import numpy as np

#scatter plots
#to check how points related to each other
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x, y)

plt.show()
#give color to scatter chart point
size=50*np.random.randn(1000)
color=np.random.randn(1000)
plt.scatter(x, y, s=size,c=color);
plt.show()
#############################################
#adding text
#minima graph
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-4, 4,1024)
y= .25 * (x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,-0.25,'brackmard minimum')
plt.plot(x,y,c='k')
plt.xlabel('om')
plt.show()









































