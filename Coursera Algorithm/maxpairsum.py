# Python 3
def maxpairsum(seq):
	t = max(seq)
	seq.remove(t)
	t2 = max(seq)
	return t*t2



if __name__ == '__main__':
	n_size = input()
	seq = [int(val) for val in input().split()]
	out = maxpairsum(seq)
	print(out)