
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

# print("Hello python")

# plt.plot([1,2,3],[5,7,4])
# plt.savefig("fig1.svg", format="svg")
# plt.show()


if __name__ == "__main__":

    figure(num=None, figsize=(2.8, 1.7), dpi=300)   # 图片分辨率width=2.8(inch)*300(dpi)

    plt.plot([5, 7, 4], 'darkorange', label='with threshold')   # 画图，并指定颜色

    plt.xticks(fontproperties = 'Times New Roman', fontsize=8)
    plt.yticks(np.arange(0, 8, 1), fontproperties = 'Times New Roman', fontsize=8)
    # 指定横纵坐标的字体以及字体大小，记住是fontsize不是size。yticks上我还用numpy指定了坐标轴的变化范围。

    plt.legend(loc='lower right', prop={'family':'Times New Roman', 'size':8})
    # 图上的legend，记住字体是要用prop以字典形式设置的，而且字的大小是size不是fontsize，这个容易和xticks的命令弄混

    plt.title('title', fontdict={'family' : 'Times New Roman', 'size':8})
    # 指定图上标题的字体及大小

    plt.xlabel('iterations', fontdict={'family' : 'Times New Roman', 'size':8})
    plt.ylabel('accuracy', fontdict={'family' : 'Times New Roman', 'size':8})
    # 指定横纵坐标描述的字体及大小

    # plt.savefig('F:/where-you-want-to-save.png', dpi=300, bbox_inches="tight")    # 保存文件，dpi指定保存文件的分辨率
    plt.savefig("fig1.svg", format="svg", bbox_inches="tight")  # bbox_inches防止标纵label保存丢失

    plt.show()      # 记住要先savefig，再show，否则存出一张白纸
