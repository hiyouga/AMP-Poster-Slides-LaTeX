import matplotlib
import numpy as np
import matplotlib.pyplot as plt

default_params = {
    'text.usetex': False,
    'font.family': 'Times New Roman',
    'font.serif': 'Times New Roman'
}

if __name__ == '__main__':
    plt.rcParams.update(default_params)
    myfont1 = matplotlib.font_manager.FontProperties(fname='C:\\times.ttf', size=14)
    myfont2 = matplotlib.font_manager.FontProperties(fname='C:\\times.ttf', size=12)
    plt.figure(figsize=(5, 3))
    x = np.linspace(0.001, 5, 1000)
    y1 = 0.001 * x ** 2 + 0.02 * 1 / x + 0.02
    y2 = 0.12 * x ** 2 + 0.04 * 1 / x + 0.06
    plt.plot(x, y1, color='b', linestyle='--', label='Training error')
    plt.plot(x, y2, color='g', linestyle='-', label='Generalization error')
    cx = 0.55
    cy = 0.12 * cx ** 2 + 0.04 * 1 / cx + 0.06
    plt.plot([cx, cx], [-0.01, cy], color='r', linestyle=':')
    plt.plot([-0.01, cx], [cy, cy], color='r', linestyle=':')
    plt.text(cx-0.3, -0.12, 'Optimal capacity', fontproperties=myfont2)
    plt.arrow(1.6, 0.21, 0.0, 0.12, head_width=0.03, head_length=0.03, shape='full', fc='black', ec='black', linewidth=1)
    plt.arrow(1.6, 0.21, 0.0, -0.12, head_width=0.03, head_length=0.03, shape='full', fc='black', ec='black', linewidth=1)
    plt.text(1.65, 0.18, 'Generalization gap', fontproperties=myfont2)
    plt.legend(loc='upper right', prop=myfont1)
    plt.xticks([0])
    plt.yticks([])
    plt.xlabel('Capacity', fontproperties=myfont1)
    plt.ylabel('Error', fontproperties=myfont1)
    plt.xlim((-0.01, 2.5))
    plt.ylim((-0.01, 1.2))
    plt.savefig('gap1.pdf', format='pdf', dpi=900, bbox_inches='tight')

    plt.figure(figsize=(5, 3))
    x = np.linspace(0.001, 5, 1000)
    y1 = 0.005 * x ** 2 + 0.03 * 1 / x + 0.03
    y2 = 0.04 * x ** 2 + 0.05 * 1 / x + 0.03
    plt.plot(x, y1, color='b', linestyle='--', label='Training error')
    plt.plot(x, y2, color='g', linestyle='-', label='Generalization error')
    cx = 0.855
    cy = 0.04 * cx ** 2 + 0.05 * 1 / cx + 0.03
    plt.plot([cx, cx], [-0.01, cy], color='r', linestyle=':')
    plt.plot([-0.01, cx], [cy, cy], color='r', linestyle=':')
    plt.text(cx-0.3, -0.12, 'Optimal capacity', fontproperties=myfont2)
    plt.legend(loc='upper right', prop=myfont1)
    plt.xticks([0])
    plt.yticks([])
    plt.xlabel('Capacity', fontproperties=myfont1)
    plt.ylabel('Error', fontproperties=myfont1)
    plt.xlim((-0.01, 2.5))
    plt.ylim((-0.01, 1.2))
    plt.savefig('gap2.pdf', format='pdf', dpi=900, bbox_inches='tight')
