# 伪代码：
# 1. 创建一个字典，键为编程语言，值为使用百分比。
# 2. 打印这个字典。
# 3. 使用matplotlib库绘制条形图。
# 4. 定义一个变量来存储要查询的编程语言。 
# 5. 从字典中获取并打印该语言的使用百分比。
import matplotlib.pyplot as plt  # Correct import

# 步骤1：创建字典
language_popularity = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}

# 步骤2：打印字典
print("Programming Language Popularity Dictionary:")
print(language_popularity)

# 步骤3：绘制条形图
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

plt.figure(figsize=(10, 6))
plt.bar(languages, percentages, color='skyblue')
plt.title('Top 5 Programming Languages by Usage Percentage (February 2024)')
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers (%)')
plt.ylim(0, 70)  # 设置y轴范围以更好地展示数据
plt.show()

# 步骤4：定义要查询的编程语言
# 你可以在这里修改语言名称
query_language = "Python"  # 例如，查询Python的使用百分比

# 步骤5：打印指定语言的使用百分比
if query_language in language_popularity:
    print(f"The percentage of developers using {query_language} is {language_popularity[query_language]}%.")
else:
    print(f"{query_language} is not in the top 5 programming languages list.")