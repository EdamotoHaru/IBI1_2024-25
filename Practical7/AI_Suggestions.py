# spliced_tata_genes.py
import re

# ===== 步骤1：获取用户输入 =====
while True:
    splice_site = input("请输入剪接供体/受体组合（GTAG、GCAG、ATAC）: ").upper()
    if splice_site in ['GTAG', 'GCAG', 'ATAC']:
        break
    print("错误：请输入GTAG、GCAG或ATAC中的一种！")

# 生成输出文件名（例如：GTAG_spliced_genes.fa）
output_filename = f"{splice_site}_spliced_genes.fa"

# ===== 步骤2：解析剪接位点 =====
# 前两位是剪接供体（如GT），后两位是受体（如AG）
donor = splice_site[:2]   # 例如：GT
acceptor = splice_site[2:] # 例如：AG

# 构建正则表达式模式（例如：GT.*AG）
splice_pattern = re.compile(
    re.escape(donor) +  # 转义特殊字符
    r'.*?' +            # 非贪婪匹配任意字符（内含子）
    re.escape(acceptor)
)

# ===== 步骤3：定义TATA盒模式 =====
# TATAWAW模式：TATA[AT]A[AT]
tata_pattern = re.compile(r'TATA[AT]A[AT]')

# ===== 步骤4：处理FASTA文件 =====
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, \
     open(output_filename, 'w') as outfile:

    current_gene = {'name': None, 'seq': []}

    for line in infile:
        # 遇到新基因头
        if line.startswith('>'):
            # 处理上一个基因
            if current_gene['name'] is not None:
                # 合并多行序列为单行
                full_seq = ''.join(current_gene['seq']).upper()
                
                # 检查剪接位点
                is_spliced = bool(splice_pattern.search(full_seq))
                # 统计TATA盒
                tata_count = len(tata_pattern.findall(full_seq))

                # 满足条件时写入文件
                if is_spliced and tata_count > 0:
                    header = f">{current_gene['name']} TATA_count:{tata_count}"
                    outfile.write(f"{header}\n{full_seq}\n")

            # 开始新基因（提取基因名，例如：>YFL039C ... → YFL039C）
            current_gene['name'] = line[1:].split()[0]  # 去除">"后取第一个字段
            current_gene['seq'] = []
        # 累积序列行
        else:
            current_gene['seq'].append(line.strip())

    # 处理最后一个基因
    if current_gene['name'] is not None:
        full_seq = ''.join(current_gene['seq']).upper()
        is_spliced = bool(splice_pattern.search(full_seq))
        tata_count = len(tata_pattern.findall(full_seq))
        if is_spliced and tata_count > 0:
            header = f">{current_gene['name']} TATA_count:{tata_count}"
            outfile.write(f"{header}\n{full_seq}\n")

print(f"处理完成！结果已保存至：{output_filename}")
# 这个代码段是一个Python脚本，用于从FASTA文件中提取特定基因的信息，并根据剪接位点和TATA盒的存在进行筛选和输出。