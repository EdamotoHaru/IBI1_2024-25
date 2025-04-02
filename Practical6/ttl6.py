import numpy as np
import matplotlib.pyplot as plt

# 模型参数
total_population = 100000
initial_infected = 1
vaccination_rate = 0.2
vaccine_efficacy = 0.6
asymptomatic_rate = 0.9
base_r0 = 2.0
isolation_days = 2
recovery_window = (7, 14)

# 衍生参数
effective_vax = vaccination_rate * vaccine_efficacy
susceptible_vax = vaccination_rate * (1 - vaccine_efficacy)
initial_susceptible = total_population * (1 - vaccination_rate + susceptible_vax)

# 初始化隔间
S = initial_susceptible - initial_infected
Ia = initial_infected * asymptomatic_rate  # 无症状感染者
Is = initial_infected * (1 - asymptomatic_rate)  # 有症状感染者
R = total_population * effective_vax  # 免疫人群

# 时间参数
days = 90
daily_infections = []

# 模拟传播
for day in range(days):
    # 动态传播率计算
    effective_contact = base_r0 * (S / total_population)
    
    # 不同人群传播周期
    asymp_contagious_days = np.mean(recovery_window)
    symp_contagious_days = isolation_days
    
    # 每日新感染人数
    new_infections = (Ia * effective_contact/asymp_contagious_days +
                      Is * effective_contact/symp_contagious_days)
    
    # 隔离和恢复机制
    new_asymp = new_infections * asymptomatic_rate
    new_symp = new_infections * (1 - asymptomatic_rate)
    
    # 人群状态更新
    S -= new_infections
    recovered_asymp = Ia * (1/asymp_contagious_days) 
    recovered_symp = Is * (1/symp_contagious_days)
    
    Ia += new_asymp - recovered_asymp
    Is += new_symp - recovered_symp
    R += recovered_asymp + recovered_symp
    
    # 记录数据
    daily_infections.append(new_infections)

# 可视化
plt.figure(figsize=(12,6))
plt.plot(daily_infections, color='darkred', label='Daily New Infections')
plt.fill_between(range(days), daily_infections, color='mistyrose')
plt.title('Epidemic Curve with Vaccination and Isolation Measures')
plt.xlabel('Days Since Outbreak')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
