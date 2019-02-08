import xlrd
import matplotlib.pyplot as plt
import imageio

# cols展示前几列数据，xlim_num为刻度值，duration为动图间隔0.2-0.5最好
def data_gif(cols, xlim_num, duration):
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 显示中文
    plt.rcParams['axes.unicode_minus'] = False # 显示负号
    frames = []
    xlsx = xlrd.open_workbook('example.xlsx')
    sheet = xlsx.sheet_by_index(0)
    name_list = []
    for j in range(1, int(cols)):
        name_list.append(sheet.cell_value(0, j))
    
    for i in range(1, sheet.nrows):
        row_data_list = []
        for j in range(1, int(cols)):
            title = sheet.cell_value(i, 0)
            row_data = sheet.cell_value(i, j)
            row_data_list.append(float(row_data))
        plt.xlim((0, int(xlim_num)))
        plt.barh(name_list, row_data_list, color='blue')
        plt.savefig('img/{}.png'.format(title))
        plt.close('all')

        im = imageio.imread('img/{}.png'.format(title))
        frames.append(im)
    imageio.mimsave('data_rank.gif', frames, 'GIF', duration=round(duration, 2))


data_gif(7, 7500, 0.5)    