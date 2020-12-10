import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
# 用于进行层次聚类，画层次聚类图的工具包

points = scipy.randn(20, 4)
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
disMat = sch.distance.pdist(points, 'euclidean')

# 进行层次聚类:
Z = sch.linkage(disMat, method='average')

plt.figure()

# 将层级聚类结果以树状图表示出来并保存为plot_dendrogram.png
P = sch.dendrogram(Z)

plt.show()
