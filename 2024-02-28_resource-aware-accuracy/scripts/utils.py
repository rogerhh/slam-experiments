import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_poses2d(poses=None, x=[], y=[], theta=[], filename=None, params={}, plot=True, save=False):
    if poses is not None:
        for i in range(poses.size()):
            pose = poses.atPose2(i)
            x.append(pose.x())
            y.append(pose.y())
    title = ""
    for key, item in params.items():
        title += f"{key}={item} "
    plt.title(title)
    plt.plot(x, y, '-', alpha=0.5, color="green")
    if plot:
        plt.show()
    if save:
        assert(filename is not None)
        plt.savefig(filename)

def plot_poses3d(poses=None, x=[], y=[], z=[], theta=[], filename=None, params={}, plot=True, save=False):
    if poses is not None:
        raise NotImplementedError

    title = ""
    for key, item in params.items():
        title += f"{key}={item} "
    plt.title(title)
    plt.plot(x, y, z, '-', alpha=0.5, color="green")
    if plot:
        plt.show()
    if save:
        assert(filename is not None)
        plt.savefig(filename)

def read_2d_poses(fin):
    x = []
    y = []
    theta = []
    max_num_poses = 0
    while True:
        line = fin.readline()
        if not line:
            break
        if "Values with" in line:
            arr = line.split()
            max_num_poses = int(arr[2])
            break

    num_poses = 0
    while True:
        if num_poses >= max_num_poses:
            break

        line = fin.readline()
        if not line:
            break

        if line[0] == "(":
            num_poses += 1
            arr = line.strip("() \n").split(",")
            x.append(float(arr[0]))
            y.append(float(arr[1]))
            theta.append(float(arr[2]))

    return x, y, theta



def read_3d_poses(fin):
    x = []
    y = []
    z = []
    max_num_poses = 0
    while True:
        line = fin.readline()
        if not line:
            break
        if "Values with" in line:
            arr = line.split()
            max_num_poses = int(arr[2])
            break

    num_poses = 0
    while True:
        if num_poses >= max_num_poses:
            break

        line = fin.readline()
        if not line:
            break

        if line[0] == "t":
            num_poses += 1
            arr = line.split(" ")
            arr = [s for s in arr if s]
            x.append(float(arr[1]))
            y.append(float(arr[2]))
            z.append(float(arr[3]))

    return x, y, z

