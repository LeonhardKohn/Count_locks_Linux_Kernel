import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def read_and_smooth_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                tag, result = line.split("|")
                branch_tag = tag.strip().split(":")[1].strip()
                if "rc" in branch_tag:
                    #if branch_tag != "v2.6.12": 
                    continue
                result = result.strip().split(":")[1].strip()
                shell_result = int(result.strip())
                data.append((branch_tag, shell_result))
    
    x_values = [entry[0] for entry in data if not "rc" in entry[0]]
    y_values = [entry[1] for entry in data]
    print(x_values)
    
    return x_values, y_values

# Read and smooth data for different lock mechanisms
x_values_lines, smoothed_y_lines = read_and_smooth_data("lines_code_linux.txt")
#x_values_spin, smoothed_y_spin = read_and_smooth_data("results_spin_lock.txt")
#x_values_mutex, smoothed_y_mutex = read_and_smooth_data("results_mutex_lock.txt")
#x_values_cmpxchg, smoothed_y_cmpxchg = read_and_smooth_data("results_cmpxchg.txt")

# Plot the graph as a line
plt.plot(x_values_lines, smoothed_y_lines, linestyle='solid')
#plt.plot(x_values_spin, smoothed_y_spin, linestyle='solid')
#plt.plot(x_values_cmpxchg, smoothed_y_cmpxchg, linestyle='solid')
#plt.plot(x_values_mutex, smoothed_y_mutex, linestyle='solid')

# Configure x-axis labels for branches without 'rc'
plt.xticks(rotation=45, ha='right')
# Set axis labels and title
plt.xlabel('Linux Version')
plt.ylabel('Number of line Code')
plt.legend(["Lines of Code"])
plt.title('History over Linux versions regarding lines of code')

# Display the graph
plt.tight_layout()
plt.show()

