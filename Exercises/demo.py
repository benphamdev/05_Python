import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x

plt.plot(x, y, label='sin(3x)/x')
plt.plot(x, y2, label='sin(2x)/x')
plt.plot(x, y3, label='sin(x)/x')

plt.title('Biểu đồ hàm Sinc')
plt.xlabel('X')
plt.ylabel('Y')
ax.spines['left'].set_position(('outward', 10))
ax.spines['bottom'].set_position(('outward', 10))

# Đặt các điểm dữ liệu trên trục x cách nhau một khoảng là π
plt.xticks(np.arange(-2*np.pi, 2*np.pi + np.pi, np.pi), 
           ['-2π', '-π', '0', 'π', '2π'])

# Đặt các điểm dữ liệu trên trục y cách nhau một khoảng là 1
plt.yticks(np.arange(-1, 4, 1))

ax = plt.gca()

# Di chuyển các nhãn của trục x lên truc ox
ax.xaxis.set_label_coords(1.05, 0.5)

# Đặt trục x và trục y tại (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Ẩn các đường viền không cần thiết
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.legend()
plt.grid(True)
plt.show()
