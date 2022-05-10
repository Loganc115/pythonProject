import matplotlib.pyplot as plot
import numpy as np
#my name is logan Clementi
y=np.array([15, 33, 55, 45])
mylabels=['apples', 'bananas', 'cherries','dates']
mycolors=['red','yellow', 'purple','#4caf50']
plot.pie(y, labels=mylabels, colors=mycolors)
plot.legend(title='four fruits')
plot.legend(mylabels, bbox_to_anchor=(0.85,1.025),   loc="upper left")
plot.show()

print(x=+(4-2)