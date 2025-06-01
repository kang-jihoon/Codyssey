import numpy as np

arr1 = np.genfromtxt("mars_base_main_parts-001.csv", delimiter = ",", dtype = None, encoding = 'utf-8-sig', names = True)
arr2 = np.genfromtxt("mars_base_main_parts-002.csv", delimiter = ",", dtype = None, encoding = 'utf-8-sig', names = True)
arr3 = np.genfromtxt("mars_base_main_parts-003.csv", delimiter = ",", dtype = None, encoding = 'utf-8-sig', names = True)

parts = np.concatenate((arr1, arr2, arr3))

names = parts['parts'].astype(str)
strengths = parts['strength']
unique_parts = np.unique(names)

averages = np.array([
    (part, strengths[names == part].mean())
    for part in unique_parts
], dtype = [('parts', 'U30'), ('avg_strength', 'f4')])

filtered = averages[averages['avg_strength'] < 50]

np.savetxt(
    'parts_to_work_on.csv',
    filtered,
    fmt='%s,%.3f',
    delimiter=',',
    header = 'parts,avg_strength',
)

parts2 = np.genfromtxt(
    'parts_to_work_on.csv',
    delimiter = ',',
    names = True,
    dtype = None,
    encoding = 'utf-8'
)

names = parts2['parts']
strengths = parts2['avg_strength']

data_matrix = np.vstack((names, strengths))
parts3 = data_matrix.T

print(parts3)
