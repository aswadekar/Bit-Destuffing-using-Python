# CCN Exp. 8  Python code for Bit Stuffing
# Atharva Wadekar 21103A2004

def bitDestuffing(N, arr):

	brr = [0 for i in range(30)]

	k = 0
	i = 0
	j = 0

	count = 1

	while (i < N):

		if (arr[i] == 1):

			brr[j] = arr[i]

			for k in range(i + 1, k < N and arr[k] == 1 and count < 5,1):
				j += 1
				brr[j] = arr[k]
				count += 1

				if (count == 5):
					k += 1
					i = k


		else:
			brr[j] = arr[i]

		i += 1
		j += 1

	for i in range(0, j):
		print(brr[i],end="")

if __name__ == '__main__':
	N = 7
	arr = [1, 1, 1, 1, 1, 0, 1]

	bitDestuffing(N, arr)
