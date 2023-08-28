import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def analyse_two_more(df, fig_path, column_group, column_name):
    this_df = df[column_name]

    if column_name == '新鲜蔬菜':
        range_low = 0
        range_high = 5000
        threshold = 300
    elif column_name == '体育锻炼':
        range_low = 0
        range_high = 1950
        threshold = 150

    if column_group == '年龄':
        # 将年龄分成不同的区间
        age_bins = list(range(20, 131, 10))
        age_labels = [f"{i}-{i+10}" for i in range(20, 130, 10)]
        df['年龄'] = pd.cut(df[column_group], bins=age_bins, labels=age_labels)
        column_group = '年龄'

    # 设置区间范围和标签
    bin_edges = [range_low, threshold, range_high]
    bin_labels = ['不足', '足量']

    # 计算每一类职业人群的每一档次新鲜蔬菜的摄入量平均值
    average = df.groupby([column_group, pd.cut(this_df, bins=bin_edges, labels=bin_labels)])[column_name].mean().unstack(fill_value=0).round(3)

    # 计算每一类职业人群的每一档次新鲜蔬菜的人数统计
    count = df.groupby([column_group, pd.cut(this_df, bins=bin_edges, labels=bin_labels)]).size().unstack(fill_value=0)

    # 创建新的Excel writer
    result_excel = column_name + '-' + column_group + '.xlsx'
    os.chdir(fig_path)
    writer = pd.ExcelWriter(result_excel, engine='xlsxwriter')

    # 将结果存储到Excel的不同工作表中
    count.to_excel(writer, sheet_name='人数统计')
    average.to_excel(writer, sheet_name='平均值')

    # 保存Excel文件
    writer._save()


def analyse_two_less(df, fig_path, column_group, column_name):
    this_df = df[column_name]

    if column_name == '酒精':
        range_low = 0
        range_high = 7
        threshold = 15
    elif column_name == '油炸面食':
        range_low = 0
        range_high = 260
        threshold = 100
    elif column_name == '含糖饮料':
        range_low = 0
        range_high = 42
        threshold = 2
    elif column_name == '不吃早餐':
        range_low = 0
        range_high = 8
        threshold = 1

    if column_group == '年龄':
        # 将年龄分成不同的区间
        age_bins = list(range(20, 131, 10))
        age_labels = [f"{i}-{i+10}" for i in range(20, 130, 10)]
        df['年龄'] = pd.cut(df[column_group], bins=age_bins, labels=age_labels)
        column_group = '年龄'

    # 设置区间范围和标签
    bin_edges = [range_low, threshold, range_high]
    bin_labels = ['健康', '不健康']

    # 使用cut函数将食用油值分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels, right=False)

    # 计算每一类人群的每一档次的平均值
    average = df.groupby([column_group, df['new']])[column_name].mean().unstack(fill_value=0).round(3)

    # 计算每一类职业人群的每一档次新鲜蔬菜的人数统计
    count = df.groupby([column_group, df['new']]).size().unstack(fill_value=0)

    # 创建新的Excel writer
    result_excel = column_name + '-' + column_group + '.xlsx'
    os.chdir(fig_path)
    writer = pd.ExcelWriter(result_excel, engine='xlsxwriter')

    # 将结果存储到Excel的不同工作表中
    count.to_excel(writer, sheet_name='人数统计')
    average.to_excel(writer, sheet_name='平均值')

    # 保存Excel文件
    writer._save()


def analyse_three(df, fig_path, column_group, column_name):
    this_df = df[column_name]

    if column_name == '新鲜水果':
        range_low = 0
        range_high = 28600
        threshold_low = 200
        threshold_high = 350

    if column_group == '年龄':
        # 将年龄分成不同的区间
        age_bins = list(range(20, 131, 10))
        age_labels = [f"{i}-{i+10}" for i in range(20, 130, 10)]
        df['年龄'] = pd.cut(df[column_group], bins=age_bins, labels=age_labels)
        column_group = '年龄'

    # 设置区间范围和标签
    bin_edges = [range_low,  threshold_low, threshold_high, range_high]
    bin_labels = ['不足', '适量', '过量']

    # 使用cut函数将吸烟指数分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels)

    # 计算每一类人群的每一档次的平均值
    average = df.groupby([column_group, df['new']])[column_name].mean().unstack(fill_value=0).round(3)

    # 计算每一类职业人群的每一档次新鲜蔬菜的人数统计
    count = df.groupby([column_group, df['new']]).size().unstack(fill_value=0)

    # 创建新的Excel writer
    result_excel = column_name + '-' + column_group + '.xlsx'
    os.chdir(fig_path)
    writer = pd.ExcelWriter(result_excel, engine='xlsxwriter')

    # 将结果存储到Excel的不同工作表中
    count.to_excel(writer, sheet_name='人数统计')
    average.to_excel(writer, sheet_name='平均值')

    # 保存Excel文件
    writer._save()


def analyse_four(df, fig_path, column_group, column_name):
    this_df = df[column_name]

    if column_name == '吸烟指数':
        range_low = -2000
        range_high = 3800
        threshold_low = 0
        threshold_medium = 400
        threshold_high = 800

    if column_group == '年龄':
        # 将年龄分成不同的区间
        age_bins = list(range(20, 131, 10))
        age_labels = [f"{i}-{i+10}" for i in range(20, 130, 10)]
        df['年龄'] = pd.cut(df[column_group], bins=age_bins, labels=age_labels)
        column_group = '年龄'

    # 设置区间范围和标签
    bin_edges = [range_low,  threshold_low, threshold_medium, threshold_high, range_high]
    bin_labels = ['无', '轻度', '中度', '重度']

    # 使用cut函数将吸烟指数分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels)

    # 计算每一类人群的每一档次的平均值
    average = df.groupby([column_group, df['new']])[column_name].mean().unstack(fill_value=0).round(3)

    # 计算每一类职业人群的每一档次新鲜蔬菜的人数统计
    count = df.groupby([column_group, df['new']]).size().unstack(fill_value=0)

    # 创建新的Excel writer
    result_excel = column_name + '-' + column_group + '.xlsx'
    os.chdir(fig_path)
    writer = pd.ExcelWriter(result_excel, engine='xlsxwriter')

    # 将结果存储到Excel的不同工作表中
    count.to_excel(writer, sheet_name='人数统计')
    average.to_excel(writer, sheet_name='平均值')

    # 保存Excel文件
    writer._save()


def plot_relate(df, fig_path, column_group, column_name):
    if column_group == '职业':
        step = 3
    elif column_group == '文化程度':
        step = 2
    elif column_group == '性别':
        step = 1
    elif column_group == '婚姻状况':
        step = 1
    elif column_group == '年龄':
        step = 3
        age_bins = list(range(20, 131, 10))
        age_labels = [f"{i}-{i+10}" for i in range(20, 130, 10)]
        df['年龄'] = pd.cut(df[column_group], bins=age_bins, labels=age_labels)
        column_group = '年龄'

    # 按照column_group列进行分类，计算每一类对应的含糖饮料平均值
    test_df = df.groupby(column_group)[column_name].mean()
    test_df = test_df.dropna()

    # 对平均值进行排序，找到排名前三和后三的类别
    counts = test_df.sort_values(ascending=False)
    top = counts.head(step)
    bottom = counts.tail(step)

    # 创建颜色列表，前三位为红色，后三位为黄色，其余为蓝色
    colors = ['salmon' if group in top.index
                else 'yellow' if group in bottom.index
                else 'lightblue' for group in counts.index]

    # 绘制柱状图
    plt.figure()
    plt.bar(counts.index, counts.values, color=colors)

    # 在每个柱子上方添加计数的文本标签
    for x, y in zip(counts.index, counts.values):
        plt.text(x, y, f'{y:.3f}', ha='center', va='bottom')

    plt.xlabel('Group')
    plt.ylabel('Count')
    plt.title('各个'+column_group+'对应的平均'+column_name)
    plt.xticks(rotation=45, ha='right')

    fig_name = column_name+'-'+column_group+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)


def plot_scatter_two(df, fig_path, column_group, column_name):
    # Create a scatter plot with circular markers and light blue color
    plt.figure()
    sns.scatterplot(x=column_group, y=column_name, data=df, marker='o', color='salmon', alpha=0.5)

    # # Fit and add the regression line to the plot
    # sns.regplot(x=column_name, y=column_group, data=df, scatter=False, color='lightgreen')

    # 计算相关系数
    correlation = np.corrcoef(df[column_group], df[column_name])[0, 1]

    # Customize the plot
    plt.xlabel(column_group)
    plt.ylabel(column_name)
    plt.title('Scatter Plot of '+column_name+' by '+column_group+f' Correlation: {correlation:.3f}')

    # Show the plot
    fig_name = column_name+'-'+column_group+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)


def plot_scatter(df, fig_path):
    # 选择你想要绘制的自变量和因变量列
    selected_columns = ['吸烟指数', '酒精', '含糖饮料', '不吃早餐', '新鲜蔬菜', '新鲜水果', '体育锻炼',
                        '收缩压', '脉搏', '胆固醇', '血糖', '高密度脂蛋白', '甘油三酯', '尿酸']

    # 从DataFrame中选择这些列
    selected_df = df[selected_columns]

    # 计算互相关系数
    correlation_matrix = selected_df.corr()

    # 创建一个与相关系数矩阵相同大小的零矩阵
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

    # 绘制互相关矩阵的热力图，只显示下三角部分，对角线为1的部分用白色遮挡
    plt.figure()
    sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()
