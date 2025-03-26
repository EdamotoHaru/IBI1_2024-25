import panda as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 示例数据加载（假设CSV文件包含'日期'和'睡眠时间'两列）
# 日期格式应为YYYY-MM-DD，睡眠时间为小时数值
data = pd.read_csv('sleep_data.csv')
data['日期'] = pd.to_datetime(data['日期'])  # 转换日期格式

# 按周重采样计算平均值（默认从周日开始为一周）
weekly_avg = data.resample('W', on='日期')['睡眠时间'].mean().reset_index()

# 创建画布
plt.figure(figsize=(12, 6))

# 绘制折线图
plt.plot(weekly_avg['日期'], 
         weekly_avg['睡眠时间'], 
         marker='o', 
         linestyle='-', 
         color='steelblue',
         linewidth=2,
         markersize=8)

# 设置图表样式
plt.title('每周平均睡眠时间变化趋势', fontsize=14, pad=20)
plt.xlabel('日期', fontsize=12)
plt.ylabel('平均睡眠时间（小时）', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# 格式化横坐标日期显示
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.SU))
plt.xticks(rotation=45)

# 显示数据标签
for x, y in zip(weekly_avg['日期'], weekly_avg['睡眠时间']):
    plt.text(x, y+0.1, f'{y:.1f}', 
             ha='center', 
             va='bottom',
             fontsize=9)

# 调整布局并显示
plt.tight_layout()
plt.show()
