import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_pie(df, fig_path, column_name):
    # 统计列中各个值的出现次数
    value_counts = df[column_name].value_counts()

    # 创建饼状图
    plt.figure(figsize=(8, 8))
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
    # 使饼状图为圆形
    plt.axis('equal')

    plt.title(column_name)

    plt.show()


def plot_two_less(df, fig_path, column_name):
    this_df = df[column_name]

    if column_name == '盐':
        range_low = 0
        range_high = 440
        step = 5
        threshold = 5
    elif column_name == '酒精':
        range_low = 0
        range_high = 7
        step = 1
        threshold = 15
    elif column_name == '油炸面食':
        range_low = 0
        range_high = 260
        step = 20
        threshold = 100
    elif column_name == '含糖饮料':
        range_low = 0
        range_high = 1850
        step = 25
        threshold = 25
    elif column_name == '不吃早餐':
        range_low = 0
        range_high = 8
        step = 1
        threshold = 1
    elif column_name == '不吃中餐':
        range_low = 0
        range_high = 8
        step = 1
        threshold = 1
    elif column_name == '不吃晚餐':
        range_low = 0
        range_high = 8
        step = 1
        threshold = 1

    # 设置区间范围和标签
    bin_edges = list(range(range_low, range_high+step, step))
    bin_labels = [f"{i}-{i+step}" for i in range(range_low, range_high, step)]

    # 使用cut函数将食用油值分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels, right=False)

    # 统计各个区间的数量
    counts = df['new'].value_counts().sort_index()

    plt.figure()

    # 用于记录绘制过的柱子的索引
    drawn_bars = []
    for i, count in enumerate(counts.values):
        # 跳过统计数值为0的柱子
        if count == 0:
            continue  
        bar = plt.bar(counts.index[i], count)
        drawn_bars.append(bar[0])

        # 低于这区间的标为绿色，高于这区间的标为红色
        if bin_edges[i] < threshold:
            bar[0].set_color('lightgreen')
        else:
            bar[0].set_color('salmon')

        # 在每个柱子上方添加计数的文本标签
        plt.text(counts.index[i], count, f'{count}', ha='center', va='bottom')

    plt.xlabel('Group')
    plt.ylabel('Count')
    plt.title('Distribution of '+column_name)
    plt.xticks(rotation=45, ha='right')

    # 绘制饼状图，并显示计数和比例
    plt.axes([0.4, 0.2, 0.6, 0.6])
    labels = ['Normal', 'High']
    sizes = [this_df[this_df < threshold].count().sum(), this_df[this_df >= threshold].count().sum()]
    colors = ['lightgreen', 'salmon']
    _, _, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    for i, t in enumerate(autotexts):
        t.set_text(f'{sizes[i]} - {t.get_text()}')
    plt.axis('equal')

    fig_name = column_name+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)


def plot_two_more(df, fig_path, column_name):
    this_df = df[column_name]

    if column_name == '新鲜蔬菜':
        range_low = 0
        range_high = 5000
        step = 100
        threshold = 300
    elif column_name == '体育锻炼':
        range_low = 0
        range_high = 1950
        step = 150
        threshold = 150

    # 设置区间范围和标签
    bin_edges = list(range(range_low, range_high+step, step))
    bin_labels = [f"{i}-{i+step}" for i in range(range_low, range_high, step)]

    # 使用cut函数将食用油值分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels, right=False)

    # 统计各个区间的数量
    counts = df['new'].value_counts().sort_index()

    # 绘制柱状图，并设置颜色
    plt.figure()

    # 用于记录绘制过的柱子的索引
    drawn_bars = []
    for i, count in enumerate(counts.values):
        # 跳过统计数值为0的柱子
        if count == 0:
            continue  
        bar = plt.bar(counts.index[i], count)
        drawn_bars.append(bar[0])

        # 低于这区间的标为绿色，高于这区间的标为红色
        if bin_edges[i] >= threshold:
            bar[0].set_color('lightgreen')
        else:
            bar[0].set_color('yellow')

        # 在每个柱子上方添加计数的文本标签
        plt.text(counts.index[i], count, f'{count}', ha='center', va='bottom')

    plt.xlabel('Group')
    plt.ylabel('Count')
    plt.title('Distribution of '+column_name)
    plt.xticks(rotation=45, ha='right')

    # 绘制饼状图，并显示计数和比例
    plt.axes([0.4, 0.2, 0.6, 0.6])
    labels = ['Enough', 'Inadequate']
    sizes = [this_df[this_df >= threshold].count().sum(), this_df[this_df < threshold].count().sum()]
    colors = ['lightgreen', 'yellow']
    _, _, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    for i, t in enumerate(autotexts):
        t.set_text(f'{sizes[i]} - {t.get_text()}')
    plt.axis('equal')

    fig_name = column_name+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)


def plot_three(df, fig_path, column_name):
    this_df = df[column_name]

    if column_name == 'BMI':
        range_low = 13
        range_high = 72
        step = 1
        threshold_low = 18.5
        threshold_high = 24
    elif column_name == '食用油':
        range_low = 0
        range_high = 505
        step = 5
        threshold_low = 25
        threshold_high = 30      
    elif column_name == '新鲜水果':
        range_low = 0
        range_high = 28600
        step = 50
        threshold_low = 200
        threshold_high = 350  
    elif column_name == '鱼禽蛋瘦肉':
        range_low = 0
        range_high = 1000
        step = 40
        threshold_low = 120
        threshold_high = 200  
    elif column_name == '奶制品':
        range_low = 0
        range_high = 17900
        step = 100
        threshold_low = 300
        threshold_high = 500  
    elif column_name == '全谷物':
        range_low = 0
        range_high = 2000
        step = 50
        threshold_low = 50
        threshold_high = 150  
    elif column_name == '大豆制品':
        range_low = 0
        range_high = 840
        step = 5
        threshold_low = 15
        threshold_high = 25

    # 设置区间范围和标签
    bin_edges = list(range(range_low, range_high+step, step))
    bin_labels = [f"{i}-{i+step}" for i in range(range_low, range_high, step)]

    # 使用cut函数将食用油值分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels, right=False)

    # 统计各个区间的数量
    counts = df['new'].value_counts().sort_index()

    plt.figure()

    # 用于记录绘制过的柱子的索引
    drawn_bars = []
    for i, count in enumerate(counts.values):
        # 跳过统计数值为0的柱子
        if count == 0:
            continue  
        bar = plt.bar(counts.index[i], count)
        drawn_bars.append(bar[0])

        # 中间的柱子标为绿色，低于这区间的标为黄色，高于这区间的标为红色
        if range_low <= bin_edges[i] < threshold_low:
            bar[0].set_color('yellow')
        elif threshold_low <= bin_edges[i] < threshold_high:
            bar[0].set_color('lightgreen')
        elif threshold_high <= bin_edges[i] < range_high:
            bar[0].set_color('salmon')

        # 在每个柱子上方添加计数的文本标签
        plt.text(counts.index[i], count, f'{count}', ha='center', va='bottom')

    plt.xlabel('Group')
    plt.ylabel('Count')
    plt.title('Distribution of '+column_name)
    plt.xticks(rotation=45, ha='right')

    # 绘制饼状图，并显示计数和比例
    plt.axes([0.4, 0.2, 0.6, 0.6])
    labels = ['Low', 'Normal', 'High']

    count1 = df[(this_df >= range_low) & (this_df < threshold_low)][column_name].count()
    count2 = df[(this_df >= threshold_low) & (this_df < threshold_high)][column_name].count()
    count3 = df[(this_df >=threshold_high) & (this_df < range_high)][column_name].count()

    sizes = [count1, count2, count3]
    colors = ['yellow', 'lightgreen', 'salmon']
    _, _, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    for i, t in enumerate(autotexts):
        t.set_text(f'{sizes[i]} - {t.get_text()}')
    plt.axis('equal')

    fig_name = column_name+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)


def plot_four(df, fig_path, column_name):
    this_df = df[column_name]

    if column_name == '吸烟指数':
        range_low = -2000
        range_high = 3800
        step = 200
        threshold_low = 0
        threshold_medium = 400
        threshold_high = 800

    # 设置区间范围和标签
    bin_edges = list(range(range_low, range_high+step, step))
    bin_labels = [f"{i}-{i+step}" for i in range(range_low, range_high, step)]

    # 使用cut函数将食用油值分组到不同的区间，并统计每个区间的数量
    df['new'] = pd.cut(this_df, bins=bin_edges, labels=bin_labels)

    # 统计各个区间的数量
    counts = df['new'].value_counts().sort_index()

    plt.figure()

    # 用于记录绘制过的柱子的索引
    drawn_bars = []
    for i, count in enumerate(counts.values):
        # 跳过统计数值为0的柱子
        if count == 0:
            continue  
        bar = plt.bar(counts.index[i], count)
        drawn_bars.append(bar[0])

        # 中间的柱子标为绿色，低于这区间的标为黄色，高于这区间的标为红色
        if range_low <= bin_edges[i] < threshold_low:
            bar[0].set_color('lightgreen')
        elif threshold_low <= bin_edges[i] < threshold_medium:
            bar[0].set_color('yellow')
        elif threshold_medium <= bin_edges[i] < threshold_high:
            bar[0].set_color('orange')
        elif threshold_high <= bin_edges[i] < range_high:
            bar[0].set_color('salmon')

        # 在每个柱子上方添加计数的文本标签
        plt.text(counts.index[i], count, f'{count}', ha='center', va='bottom')

    plt.xlabel('Group')
    plt.ylabel('Count')
    plt.title(column_name+'分布')
    plt.xticks(rotation=45, ha='right')

    # 绘制饼状图，并显示计数和比例
    plt.axes([0.4, 0.2, 0.6, 0.6])
    labels = ['无', '轻度', '中度', '重度']

    count1 = df[(this_df > range_low) & (this_df <= threshold_low)][column_name].count()
    count2 = df[(this_df > threshold_low) & (this_df <= threshold_medium)][column_name].count()
    count3 = df[(this_df > threshold_medium) & (this_df <= threshold_high)][column_name].count()
    count4 = df[(this_df > threshold_high) & (this_df <= range_high)][column_name].count()

    sizes = [count1, count2, count3, count4]
    colors = ['lightgreen', 'yellow', 'orange', 'salmon']
    _, _, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    for i, t in enumerate(autotexts):
        t.set_text(f'{sizes[i]} - {t.get_text()}')
    plt.axis('equal')

    fig_name = column_name+'.png'
    os.chdir(fig_path)
    plt.savefig(fig_name)
