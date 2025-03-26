# 导入必要的库
import numpy as np          # 用于数组操作和数值计算
import matplotlib.pyplot as plt  # 用于数据可视化

# 初始化种群网格（100x100）
population = np.zeros((100, 100))  # 创建全0二维数组，0表示易感者(S)
outbreak = np.random.choice(range(100), 2)  # 随机选择初始感染坐标
population[outbreak[0], outbreak[1]] = 1    # 设置初始感染者(I)为1

# 设置模型参数
beta = 0.3   # 感染概率（感染者传染给邻居的概率）
gamma = 0.05 # 康复概率（感染者每天康复的概率）

# 配置时间点记录
time_points = [0, 10, 50, 100]       # 需要记录快照的时间点
snapshots = [(0, population.copy())] # 记录初始状态（使用copy防止引用问题）

# 主模拟循环（运行100天）
for t in range(100):
    # (1) 查找当前所有感染者坐标
    current_infected = np.argwhere(population == 1)  # 获取所有值为1的坐标
    
    # (2) 感染传播阶段
    infected_neighbors = []  # 存储新感染坐标的临时列表
    for individual in current_infected:  # 遍历每个感染者
        x, y = individual[0], individual[1]  # 提取当前感染者坐标
        
        # 检查8个相邻网格（Moore邻域）
        for dx in [-1, 0, 1]:       # x方向偏移量
            for dy in [-1, 0, 1]:   # y方向偏移量
                if dx == 0 and dy == 0:
                    continue  # 跳过自身单元格
                
                # 计算邻居坐标
                nx, ny = x + dx, y + dy
                
                # 边界检查（确保坐标在0-99范围内）
                if 0 <= nx < 100 and 0 <= ny < 100:
                    # 仅感染易感者（状态为0）
                    if population[nx, ny] == 0:  
                        # 根据概率决定是否感染
                        if np.random.rand() < beta:
                            infected_neighbors.append((nx, ny))  # 记录新感染
    
    # 应用所有感染事件（统一更新避免状态冲突）
    for (x, y) in infected_neighbors:
        population[x, y] = 1  # 将易感者变为感染者
    
    # (3) 康复处理阶段
    for individual in current_infected:  # 遍历原始感染者列表
        x, y = individual[0], individual[1]
        # 根据概率决定是否康复
        if np.random.rand() < gamma:
            population[x, y] = 2  # 将感染者变为康复者(R)
    
    # 记录指定时间点的系统快照
    if (t + 1) in time_points:
        snapshots.append((t + 1, population.copy()))  # 保存深拷贝的状态

# 可视化结果
plt.figure(figsize=(12, 8))  # 创建画布（12x8英寸）
for i, (time, pop) in enumerate(snapshots):
    plt.subplot(2, 2, i + 1)              # 创建2x2的子图布局
    plt.imshow(pop, cmap='viridis',        # 使用viridis颜色映射
               interpolation='nearest')   # 最近邻插值保持像素化效果
    plt.title(f'Time = {time}')           # 设置子图标题
    plt.axis('off')                       # 隐藏坐标轴

plt.tight_layout()  # 自动调整子图间距
plt.show()          # 显示完整图像
