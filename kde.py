"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 13
Due Date 5/1/2023
This code plots a kernel density estimation and a histogram from randomly generated data
"""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys


if __name__ == "__main__":
	if '-h' in sys.argv or '--help' in sys.argv:
			print ("Usage: %s [-p -n -size]" % sys.argv[0])
			print
			sys.exit(1)
	if '-p' in sys.argv:
		q = sys.argv.index('-p')
		p = float(sys.argv[q+1])
	else:
		p = .1
	if '-n' in sys.argv:
		q = sys.argv.index('-n')
		n_trials = int(sys.argv[q+1])
	else:
		n_trials = 100
	if '-size' in sys.argv:
		q = sys.argv.index('-size')
		size = int(sys.argv[q+1])
	else:
		size = 100
	np.random.seed(677)

	# Draws samples from a binomial distribution
	samples = np.random.binomial(n_trials, p, size)

	# Plots the data and KDE
	sns.histplot(samples, kde=True, stat = 'probability',color = 'aqua', alpha = .25)
	plt.title('Kernel Density Estimation for Binomial Distribution')
	#plt.savefig(f'kde_n_{n_trials}_p{p}_size{size}.png')
	plt.show()