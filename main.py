#!/usr/bin/env python
# coding: utf-8

# In[47]:
import numpy as np

# In[48]:
np.random.seed(123)

# In[49]:
large_sample = np.random.normal(loc=0, scale=1, size=100000)

# In[50]:
print(large_sample[:5])

# In[51]:
import matplotlib.pyplot as plt

# In[52]:
plt.hist(large_sample, bins=30, color='blue', edgecolor='black')
plt.title('Histogram of Random Values (Standard Normal)')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# In[53]:
import numpy as py

# In[54]:
np.random.seed(123)

# In[55]:
large_uniform_sample = np.random.uniform(low=-3, high=3, size=100000)

# In[56]:
print(large_uniform_sample[:5])

# In[57]:
import matplotlib.pyplot as plt
plt.hist(large_uniform_sample, bins=30, color='green', edgecolor='black')
plt.title('Histogram of Random Values (Uniform -3 to 3)')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# In[58]:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_values = np.arange(-4, 4.1, 0.1)
densities = norm.pdf(x_values, loc=0, scale=1)
plt.plot(x_values, densities, color='blue', linewidth=2)
plt.title('Probability Density Plot (Standard Normal)')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.show()

# In[59]:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_values = np.arange(-4, 4.1, 0.1)
densities = norm.pdf(x_values, loc=0, scale=1)
plt.plot(x_values, densities, color='blue', linewidth=2, label='Theoretical Normal')
plt.hist(large_sample, bins=30, color='green', alpha=0.5, label='Histogram', density=True)
plt.title('Probability Density Plot (Standard Normal) vs. Histogram')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend(loc='upper right')
plt.show()

# In[60]:
print("When one compares the probability density curve to the histogram one should notice that the curve very closely resembles the bell-shaped curve characteristic of a standard normal distribution.")

# In[61]:
import numpy as np
import matplotlib.pyplot as plt
x_values_uniform = np.arange(-4, 4.1, 0.1)
densities_uniform = np.where((x_values_uniform >= -3) & (x_values_uniform <= 3), 1/6, 0)
plt.plot(x_values_uniform, densities_uniform, color='red', linewidth=2)
plt.title('Probability Density Plot (Uniform -3 to 3)')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.show()

# In[62]:
import numpy as np
import matplotlib.pyplot as plt
x_values_uniform = np.arange(-4, 4.1, 0.1)
densities_uniform = np.where((x_values_uniform >= -3) & (x_values_uniform <= 3), 1/6, 0)
plt.plot(x_values_uniform, densities_uniform, color='red', linewidth=2, label='Theoretical Uniform')
plt.hist(large_uniform_sample, bins=30, color='green', alpha=0.5, label='Histogram', density=True)
plt.title('Probability Density Plot (Uniform -3 to 3) vs. Histogram')
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend(loc='upper right')
plt.show()

# In[63]:
import numpy as np
np.random.seed(123)
small_sample = np.random.normal(loc=0, scale=1, size=5)
print(small_sample)

# In[64]:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
np.random.seed(123)
small_sample = np.random.normal(loc=0, scale=1, size=5)
x_values = np.arange(-4, 4.1, 0.1)
densities = norm.pdf(x_values, loc=0, scale=1)
plt.hist(small_sample, bins=5, color='green', alpha=0.5, density=True, label='Histogram')
plt.plot(x_values, densities, color='blue', linewidth=2, label='Theoretical Normal')
plt.title('Histogram and Density Plot (Small Sample vs. Normal Distribution)')
plt.xlabel('Values')
plt.ylabel('Density')
plt.legend(loc='upper right')
plt.show()

# In[65]:
import numpy as np
np.random.seed(123)
small_uniform_sample = np.random.uniform(low=-3, high=3, size=5)
print(small_uniform_sample)

# In[66]:
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
small_uniform_sample = np.random.uniform(low=-3, high=3, size=5)
x_values_uniform = np.arange(-4, 4.1, 0.1)
densities_uniform = np.where((x_values_uniform >= -3) & (x_values_uniform <= 3), 1/6, 0)
plt.hist(small_uniform_sample, bins=5, color='green', alpha=0.5, density=True, label='Histogram')
plt.plot(x_values_uniform, densities_uniform, color='blue', linewidth=2, label='Theoretical Uniform')
plt.title('Histogram and Density Plot (Small Sample vs. Uniform Distribution)')
plt.xlabel('Values')
plt.ylabel('Density')
plt.legend(loc='upper right')
plt.show()

# In[67]:
print("Part 2")

# In[68]:
import random
num_rolls = 10000
sample = [random.randint(1, 20) for _ in range(num_rolls)]
print(sample[:10])

# In[69]:
import random
import matplotlib.pyplot as plt
import numpy as np
num_rolls = 10000
sample = [random.randint(1,20) for _ in range(num_rolls)]
plt.hist(sample, bins=range(1,22), edgecolor='black', alpha=0.7)
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Histogram of 20 sided of Die Rolls')
plt.grid(True)
plt.show()
mean = np.mean(sample)
median = np.median(sample)
mode = max(set(sample),key=sample.count)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

# In[70]:
import numpy as np
import matplotlib.pyplot as plt
num_samples = 10000
mu = 10000
sigma = 2
normal
