import platform
import warnings
import matplotlib as mpl


from preprocess import *
from plot import *
from analyse import *


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    mpl.rcParams['figure.figsize']=(19.2, 10.8)

    if platform.system() == "Windows":
        mpl.rcParams['font.family'] = 'SimHei'
        xlsx_path = r'D:\iCloudDrive\项目\深圳杯\data'
        xlsx_name = '附件2 慢性病及相关因素流调数据.xlsx'
        fig_path = r'D:\iCloudDrive\项目\深圳杯\figure'
    elif platform.system() == "Darwin": 
        mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        # Set the style of the plot
        sns.set(style='ticks', font='Arial Unicode MS')
        xlsx_path = r'/Users/hyx020222/Library/Mobile Documents/com~apple~CloudDocs/project/深圳杯/data'
        xlsx_name = '附件2 慢性病及相关因素流调数据.xlsx'
        fig_path = r'/Users/hyx020222/Library/Mobile Documents/com~apple~CloudDocs/project/深圳杯/figure'

    os.chdir(xlsx_path)
    # 使用pandas的read_excel函数读取文件并转换为DataFrame
    df = pd.read_excel(xlsx_name, header=1, index_col=None)

    df = preprocess(df)
