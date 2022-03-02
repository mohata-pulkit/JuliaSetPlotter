import numpy as np
import matplotlib.pyplot as plt

def julia_set(h_range, w_range, max_iterations, a):
	y, x = np.ogrid[1.5: -1.5: h_range*1j, -1.5: 1.5: w_range*1j]
	z_array = x + y*1j
	iterations_till_divergence = max_iterations + np.zeros(z_array.shape)
	for h in range(h_range):
		for w in range(w_range):
			z = z_array[h][w]
			for i in range(max_iterations):
				z = z**2 + a
				if z * np.conj(z) > 4:
					iterations_till_divergence[h][w] = i
					break

	return iterations_till_divergence



a = 0.355 + 0.355j

plottedSet = julia_set(8192, 8192, 256, a)

plt.imsave(str(a)+".png",plottedSet, cmap='twilight')
plt.axis('off')

plt.imshow(plottedSet, cmap='twilight')
plt.axis('off')
plt.show()