
import marshal
import matplotlib.pyplot as plt
import sys
import time


fun_bin = marshal.loads(fun_bytes)

def benchmark(fun, start, stop, step):
    plot_x = [] 
    plot_y = [] 
    fig = plt.figure(fun)
    fig.suptitle(f'fun{fun}')
    plt.xlabel('input size (n)')
    plt.ylabel('execution time (s)')

    for size in range(start, stop, step):
        fun_dict = {'fun': fun, 'size': size}
        start = time.time()
        exec(fun_bin, fun_dict)
        end = time.time()
        exec_time = end - start
        print(f"fun{fun}({size}): {exec_time} s")
        plot_x.append(size)
        plot_y.append(exec_time) 
        plt.scatter(plot_x, plot_y, c='tab:blue')
        plt.pause(0.001)

    plt.savefig(f"runtime-fun{fun}.pdf")


benchmark(1, 500, 50000, 500)
benchmark(2, 50, 2500, 50)
benchmark(3, 5000, 2500000, 5000)
plt.show()
