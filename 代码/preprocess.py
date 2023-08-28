import numpy as np


def preprocess_eat(df, column_name, start_index, new_name, ratio=1.0):
    df[column_name] = np.where(df[column_name] == 1, df[column_name], 0)
    index_list = [start_index + i for i in range(4)]
    for each in index_list:
        df.iloc[:, each].fillna(0, inplace=True)
    df[new_name] = df[column_name]*(df.iloc[:, start_index]+\
                                    df.iloc[:, start_index+1]/7.0+\
                                    df.iloc[:, start_index+2]/30.42)*df.iloc[:, start_index+3]*50*ratio

    return df


def preprocess_drink(df, column_name, start_index, new_name, ratio=1.0):
    df[column_name] = np.where(df[column_name] == 1, df[column_name], 0)
    index_list = [start_index + i for i in range(4)]
    for each in index_list:
        df.iloc[:, each].fillna(0, inplace=True)
    df[new_name] = df[column_name]*(df.iloc[:, start_index]+\
                                    df.iloc[:, start_index+1]/7.0+\
                                    df.iloc[:, start_index+2]/30.42)*df.iloc[:, start_index+3]*ratio

    return df


def preprocess_cigar(df):
    df['是否吸烟'] = np.where(df['是否吸烟'] == 1, df['是否吸烟'], 0)
    df['开始吸烟年龄'].fillna(0, inplace=True)
    df['开始吸烟年龄'] = df['开始吸烟年龄'].replace({99: 19})
    df['烟龄'] = df['年龄']-df['开始吸烟年龄']
    df['平均每周吸烟天数'].fillna(0, inplace=True)
    df['一天吸烟支数'].fillna(0, inplace=True)
    df['吸烟指数'] = df['是否吸烟']*df['平均每周吸烟天数']*df['一天吸烟支数']/7*df['烟龄']

    return df


def preprocess_wine(df):
    wine_if = ['是否饮酒', '是否饮用高度白酒', '是否饮用低度白酒', '是否饮用啤酒', '是否饮用黄酒、糯米酒', '是否饮用葡萄酒']
    for each in wine_if:
        df[each].fillna(0, inplace=True)
        df[each] = np.where(df[each] == 1, df[each], 0)
    wine_index = [17, 18, 20, 21, 23, 24, 26, 27, 29, 30]
    for each in wine_index:
        df.iloc[:, each].fillna(0, inplace=True)
        df.iloc[:, each] = np.where(df.iloc[:, each] == 1, df.iloc[:, each], 0)
    # 应该给出市面上白酒，啤酒，低度白酒，黄酒，葡萄酒的平均酒精占比，从而确定比例系数
    df['酒精'] = df['是否饮酒'] * (df['是否饮用高度白酒'] * 0.45 * df.iloc[:, 17] * df.iloc[:, 18] +
                                 df['是否饮用低度白酒'] * 0.25 * df.iloc[:, 20] * df.iloc[:, 21] +
                                 df['是否饮用啤酒'] * 0.05 * df.iloc[:, 23] * df.iloc[:, 24] +
                                 df['是否饮用黄酒、糯米酒'] * 0.15 * df.iloc[:, 26] * df.iloc[:, 27] +
                                 df['是否饮用葡萄酒'] * 0.1 * df.iloc[:, 29] * df.iloc[:, 30]) / 7.0 * 50

    return df


def preprocess_BP(df):
    SBP = df['收缩压']
    DBP = df['舒张压']

    # Use numpy.logical_and() and numpy.logical_or() for element-wise logical operations
    df['血压水平'] = np.select(
        [
            np.logical_and(SBP >= 140, DBP < 90),
            np.logical_or(SBP >= 180, DBP >= 110),
            np.logical_or(np.logical_and(160 <= SBP, SBP < 180), np.logical_and(100 <= DBP, DBP < 110)),
            np.logical_or(np.logical_and(140 <= SBP, SBP < 160), np.logical_and(90 <= DBP, DBP < 100)),
            np.logical_or(SBP >= 140, DBP >= 90),
            np.logical_or(np.logical_and(120 <= SBP, SBP < 140), np.logical_and(80 <= DBP, DBP < 90)),
            np.logical_and(SBP < 120, DBP < 80)
        ],
        [
            '单纯收缩期高血压',
            '3级高血压（重度）',
            '2级高血压（中度）',
            '1级高血压（轻度）',
            '高血压',
            '正常高值',
            '正常血压'
        ],
        default='未知血压'
    )

    return df


def preprocess_BG(df):
    FBG = df['血糖']

    df['糖代谢状态'] = np.select(
        [
            FBG >= 7.0,
            np.logical_and(FBG >= 6.1, FBG < 7.0),
            FBG < 6.1
        ],
        [
            '糖尿病（DM）',
            '空腹血糖受损（IFG）',
            '正常血糖（NGR）'
        ],
        default='未知血糖'
    )

    return df


def preprocess_BL(df):
    TC = df['胆固醇']
    TG = df['甘油三酯']
    HDLC = df['高密度脂蛋白']
    LDLC = df['低密度脂蛋白']

    df['血脂水平'] = np.select(
        [
            np.logical_and(TC > 5.72, TG <= 1.70),
            np.logical_and(TC <= 5.72, TG > 1.70),
            np.logical_and(TC > 5.72, TG > 1.70),
            HDLC < 0.90,
            np.logical_and(TC <= 5.72, TG <= 1.70, HDLC >= 0.90),
        ],
        [
            '高胆固醇血症',
            '高甘油三酯血症',
            '混合型高脂血症',
            '低高密度脂蛋白血症',
            '正常血脂'
        ],
        default='未知血脂'
    )

    return df


def preprocess_UA(df):
    UA = df['尿酸']
    gender = df['性别']

    df['尿酸水平'] = np.select(
        [
            np.logical_or(np.logical_and(UA > 420, gender == '男'), np.logical_and(UA > 360, gender == '女')),
            np.logical_or(np.logical_and(UA <= 420, gender == '男'), np.logical_and(UA <= 360, gender == '女'))
        ],
        [
            '高尿酸血症',
            '正常尿酸'
        ],
        default='未知尿酸'
    )

    return df


def preprocess(df):
    df['BMI'] = df['体重']/((df['身高']/100)**2)
    # 根据BMI阈值筛选出要删除的行
    rows_to_drop = df[df['BMI'] > 72].index
    # 使用drop()方法删除这些行
    df.drop(rows_to_drop, inplace=True)
    # 重置行索引
    df.reset_index(drop=True, inplace=True)

    health_list = ['收缩压', '舒张压', '脉搏', '胆固醇', '血糖', '高密度脂蛋白', '低密度脂蛋白', '甘油三酯', '尿酸']
    for each_health in health_list:
        df[each_health].fillna(0, inplace=True)
        df.drop(df[df[each_health] == 0].index, inplace=True)

    df['年龄'] = 2023-df['出生年']

    gender_dict = {1: '男', 2: '女'}
    df['性别'] = df['性别'].replace(gender_dict)

    df.iloc[:, 4] = df.iloc[:, 4].fillna('汉族', inplace=True)

    marriage_dict = {1: '未婚', 2: '已婚', 3: '再婚', 4: '离婚', 5: '丧偶'}
    df['婚姻状况'] = df['婚姻状况'].replace(marriage_dict)

    educate_dict = {1: '文盲', 2: '小学', 3: '初中', 4: '高中/中专', 5: '大本/大专', 6: '研究生及以上'}
    df['文化程度'] = df['文化程度'].replace(educate_dict)

    career_dict = {1: '工人', 2: '农民', 3: '军人', 4: '行政干部', 5: '科技人员',
                   6: '医务人员', 7: '教师', 8: '金融财务', 9: '商业服务人员', 10: '家庭妇女',
                   11: '离、退休人员', 12: '待业', 13: '学生'}
    df['职业'] = df['职业'].replace(career_dict)

    df = preprocess_cigar(df)

    df = preprocess_wine(df)

    df['不吃早餐'].fillna(0, inplace=True)

    df['不吃中餐'].fillna(0, inplace=True)

    df['不吃晚餐'].fillna(0, inplace=True)

    df = preprocess_eat(df, '是否吃大米', 53, '大米')
    df = preprocess_eat(df, '是否吃小麦面粉', 58, '小麦面粉')
    df = preprocess_eat(df, '是否吃杂粮', 63, '杂粮')
    df['全谷物'] = df['大米']+df['小麦面粉']+df['杂粮']

    df = preprocess_eat(df, '是否吃油炸面食', 73, '油炸面食')

    df = preprocess_eat(df, '是否吃水产类', 98, '水产类')
    df = preprocess_eat(df, '是否吃禽肉', 88, '禽肉')
    #蛋类单位是个，需要考虑平均每个鸡蛋多少克，就是50
    df = preprocess_eat(df, '是否吃蛋类', 118, '蛋类')
    df['鱼禽蛋瘦肉'] = df['水产类']+df['禽肉']+df['蛋类']

    #一勺奶粉4-5克？
    df = preprocess_eat(df, '是否吃鲜奶', 103, '鲜奶')
    df = preprocess_eat(df, '是否吃奶粉', 108, '奶粉')
    df = preprocess_eat(df, '是否吃酸奶', 113, '酸奶')
    df['奶制品'] = df['鲜奶']+df['奶粉']+df['酸奶']

    df = preprocess_eat(df, '是否吃豆腐', 123, '豆腐', 0.22)
    df = preprocess_eat(df, '是否吃豆腐丝等', 128, '豆腐丝', 0.67)
    df = preprocess_eat(df, '是否吃豆浆', 133, '豆浆', 0.06)
    df = preprocess_eat(df, '是否吃干豆', 138, '干豆')
    df['大豆制品'] = df['豆腐'] + df['豆腐丝'] + df['豆浆'] + df['干豆']

    df = preprocess_eat(df, '是否吃新鲜蔬菜', 143, '新鲜蔬菜')

    df = preprocess_eat(df, '是否吃水果', 173, '新鲜水果')

    df = preprocess_drink(df, '是否吃果汁饮料', 178, '果汁饮料', 53)
    df = preprocess_drink(df, '是否吃其他饮料', 183, '其他饮料', 43.5)
    df['含糖饮料'] = df['果汁饮料']+df['其他饮料']

    #30.42是365/12，500是斤换算克，2.62来自网站平均每户人的数据
    df['食用油'] = (df['植物油']+df['动物油'])/2.62/30.42*500

    df['盐'] = df['盐']/2.62/30.42*50

    exercise_dict = {1: 0, 2: 1.5, 3: 4, 4: 6.5}
    df['是否参加体育锻炼'] = df['是否参加体育锻炼'].replace(exercise_dict)
    df['平均每天体育锻炼时间'].fillna(0, inplace=True)
    df['体育锻炼'] = df['是否参加体育锻炼']*df['平均每天体育锻炼时间']

    df = preprocess_BP(df)

    df = preprocess_BG(df)

    df = preprocess_BL(df)

    df = preprocess_UA(df)

    return df