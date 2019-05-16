import pandas as pd
import numpy as np
class Student:
    # 做预处理数据
    def __init__(self):
        self.SEART_NUMBER = 400#座位数量

    def pre_process(self):
        '''
        预处理Excel表格
        :return:stu_no_list 学生的序号列表
                class_dic_for_each 学号为键，课表为值的字典，课表是一个dataframe
                seat_dic_for_each 座位号为键，学号为值得的字典
        '''
        df1 = pd.read_excel('class.xls',usecols=[0],names=None)
        stu_no_list = df1.values.tolist()
        stu_no = ['旅行社151105']#存储所有学号
        for i in stu_no_list:
            stu_no.append(i[0])

        df2 = pd.DataFrame(pd.read_excel('class.xls'))
        class_dic_for_each = {}
        days = ['Mon','Tues','Wed','Thur','Fri']
        class_time = [1,2,3,4,5]
        for i in stu_no:
            for_each_index = df2.loc[i]
            for_each_index_matrix = np.array(for_each_index).reshape(5,5).T
            for_each_index_df = pd.DataFrame(for_each_index_matrix,
                                             index=class_time,columns=days)
            class_dic_for_each.update({i:for_each_index_df})

        seat_list = []
        for i in range(self.SEART_NUMBER):
            seat_list.append(i+1)

        seat_dic_for_each = {}
        random_seat_list = np.random.choice(seat_list, len(stu_no_list))
        for i in range(len(random_seat_list)):
            seat_dic_for_each.update({random_seat_list[i]:stu_no_list[i]})

        return stu_no_list,class_dic_for_each,seat_list,seat_dic_for_each



