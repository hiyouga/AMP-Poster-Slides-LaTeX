import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from scipy.stats import multivariate_normal
from matplotlib.patches import FancyArrowPatch


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


if __name__ == '__main__':

    X = np.linspace(-5.5, 5.5, 100)
    Y = np.linspace(-5.5, 5.5, 100)
    X, Y = np.meshgrid(X, Y)
    S = np.transpose(np.stack((X, Y)))
    Z = -3.0 * multivariate_normal.pdf(S, mean=[0, 0], cov=np.matrix([[4, 2], [2, 4]]))

    params = {
        'text.usetex': True,
        'text.latex.preamble': [
            r'\usepackage{amssymb}',
            r'\usepackage{amsmath}'
        ],
        'font.family': 'serif',
        'font.serif': 'Computer Modern'
    }
    plt.rcParams.update(params)
    arrow_prop_dict = dict(mutation_scale=10, arrowstyle='-|>', color='black', shrinkA=0, shrinkB=0)
    fig = plt.figure(figsize=(6, 4))
    ax = Axes3D(fig)
    ax.grid(False)
    ax._axis3don = False
    ax.view_init(20, -36)
    ax.plot_surface(X, Y, Z, rcount=100, ccount=100, cmap=plt.cm.coolwarm, antialiased=False)
    ax.contour(X, Y, Z, levels=4, zdir='z', offset=-0.2, cmap=plt.cm.coolwarm)
    ax.plot([-5.75, 6.0], [10.0, 10.0], [-0.2, -0.2], color='black', linewidth=2)
    a = Arrow3D([6.0, 6.4], [10.0, 10.0], [-0.2, -0.2], **arrow_prop_dict)
    ax.add_artist(a)
    ax.plot([-5.8, -5.8], [9.95, -5.0], [-0.2, -0.2], color='black', linewidth=2)
    b = Arrow3D([-5.8, -5.8], [-5.0, -5.4], [-0.2, -0.2], **arrow_prop_dict)
    ax.add_artist(b)
    ax.plot([-5.8, -5.8], [10.0, 10.0], [-0.2, 0.02], color='black', linewidth=2)
    c = Arrow3D([-5.8, -5.8], [10.0, 10.0], [0.02, 0.027], **arrow_prop_dict)
    ax.add_artist(c)
    ax.text(7.2, 9.5, -0.2, r'$\theta_x$')
    ax.text(-5.5, -6.4, -0.2, r'$\theta_y$')
    ax.text(-5.8, 10.5, 0.018, r'$\mathcal{L}$')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 10)
    ax.set_zlim(-0.18, 0)
    plt.savefig("surface.pdf", format='pdf', dpi=900, bbox_inches='tight')
    plt.show()
