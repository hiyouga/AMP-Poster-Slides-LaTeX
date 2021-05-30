import matplotlib
import matplotlib.pyplot as plt


def draw_ece():
    ''' draw ece bar '''

    erm     = [0.0204, 0.0336, 0.1097]
    dropout = [0.0186, 0.0324, 0.1208]
    lsr     = [0.1894, 0.1762, 0.1851]
    flood   = [0.0109, 0.0085, 0.0709]
    mixup   = [0.0447, 0.0549, 0.0883]
    adv     = [0.0178, 0.0341, 0.1106]
    rmp     = [0.0193, 0.0335, 0.1081]
    amp     = [0.0052, 0.0125, 0.0392]

    colors = matplotlib.cm.Paired.colors
    width = 0.9

    plt.figure(figsize=(6, 4))
    plt.bar([10*i for i in range(3)], erm, width=width, color=colors[0], label='ERM')
    plt.bar([10*i+1 for i in range(3)], dropout, width=width, color=colors[1], label='Dropout')
    plt.bar([10*i+2 for i in range(3)], lsr, width=width, color=colors[2], label='Label Smoothing')
    plt.bar([10*i+3 for i in range(3)], flood, width=width, color=colors[3], label='Flooding')
    plt.bar([10*i+4 for i in range(3)], mixup, width=width, color=colors[4], label='MixUp')
    plt.bar([10*i+5 for i in range(3)], adv, width=width, color=colors[5], label='Adv. Training')
    plt.bar([10*i+6 for i in range(3)], rmp, width=width, color=colors[6], label='RMP')
    plt.bar([10*i+7 for i in range(3)], amp, width=width, color=colors[7], label='AMP')
    plt.legend(loc='upper left', ncol=1)
    plt.xlim((-1, 28))
    plt.xticks([])
    plt.text(1.6, -0.015, 'SVHN')
    plt.text(11.2, -0.015, 'CIFAR-10')
    plt.text(21.2, -0.015, 'CIFAR-100')
    plt.ylabel('ECE')
    plt.savefig('ece.pdf', format='pdf', dpi=900, bbox_inches='tight')



if __name__ == "__main__":
    draw_ece()
