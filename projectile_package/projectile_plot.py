import matplotlib.pyplot as plt

def plot_xy(x, y):
    fig, ax= plt.subplots(figsize = (20,8)) 
    ax = plt.subplot()
    plot = ax.plot(x , y)
    plt.show
