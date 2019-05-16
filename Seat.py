import Student
import Env
import re
class Seat:
    def __init__(self):
        self.stu_no_list, self.class_dic_for_each, self.seat_list, self.seat_dic_for_each = Student().pre_process()
        self.search_seat_dic = {}


    def SearchDatenum(self,nowdate):
        weekdic = {'1': "Mon", '2': "Tues", '3': "Wed", '4': "Thur", '5': "Fri"}
        monlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        years = 0
        date = 0
        for j in range(2018, nowdate[0]):
            years += 365
        for i in range(nowdate[1] - 1):
            date += monlist[i]
        days = date + nowdate[2]
        total = days + years
        weeknum = total // 7 - 34
        week = total % 7
        if week != 0:
            week = str(week)
            week = weekdic[week]
        else:
            week = weekdic['7']
        datelist = [weeknum,week]
        return datelist


    def SearchWeeknum(self,class_info):#返回一个所有周数的list
        newss4 = []
        thenum1 = []
        weeklist = []
        for i in range(len(class_info)):
            if '周' in class_info[i]:
                newss4.append(class_info[i])
        for j in range(len(newss4)):
            thenum1.append(re.findall('\d+', newss4[j]))

        for k in range(len(thenum1)):
            if len(thenum1[k]) == 3:
                num1 = num2 = int(thenum1[k][0])
                weeklist.append(num1)
            elif len(thenum1[k]) == 4:
                num1 = int(thenum1[k][0])
                num2 = int(thenum1[k][1])
                if '单周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 != 0:
                            weeklist.append(m)
                elif '双周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 == 0:
                            weeklist.append(m)
                else:
                    for m in range(num1, num2 + 1):
                        weeklist.append(m)
            elif len(thenum1[k]) == 5:
                num1 = int(thenum1[k][0])
                num2 = int(thenum1[k][1])
                num3 = int(thenum1[k][2])
                if '单周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 != 0:
                            weeklist.append(m)
                    weeklist.append(num3)
                elif '双周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 == 0:
                            weeklist.append(m)
                    weeklist.append(num3)
                else:
                    for m in range(num1, num2 + 1):
                        weeklist.append(m)
                    weeklist.append(num3)
            elif len(thenum1[k]) == 6:
                num1 = int(thenum1[k][0])
                num2 = int(thenum1[k][1])
                num3 = int(thenum1[k][2])
                num4 = int(thenum1[k][3])
                if '单周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 != 0:
                            weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        if n % 2 != 0:
                            weeklist.append(n)
                if '双周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 == 0:
                            weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        if n % 2 == 0:
                            weeklist.append(n)
                else:
                    for m in range(num1, num2 + 1):
                        weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        weeklist.append(n)
            elif len(thenum1[k]) == 8:
                num1 = int(thenum1[k][0])
                num2 = int(thenum1[k][1])
                num3 = int(thenum1[k][2])
                num4 = int(thenum1[k][3])
                num5 = int(thenum1[k][4])
                num6 = int(thenum1[k][5])
                if '单周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 != 0:
                            weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        if n % 2 != 0:
                            weeklist.append(n)
                    for x in range(num5, num6 + 1):
                        if x % 2 != 0:
                            weeklist.append(x)
                if '双周' in newss4[k]:
                    for m in range(num1, num2 + 1):
                        if m % 2 == 0:
                            weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        if n % 2 == 0:
                            weeklist.append(n)
                    for x in range(num5, num6 + 1):
                        if x % 2 == 0:
                            weeklist.append(x)
                else:
                    for m in range(num1, num2 + 1):
                        weeklist.append(m)
                    for n in range(num3, num4 + 1):
                        weeklist.append(n)
                    for x in range(num5, num6 + 1):
                        weeklist.append(x)
        return weeklist



    def search(self,time,classnum,seatnum_list):
        '''
        根据时间和教室查询情况
        :param time: 选择时间
        :param class:第几节课
        :param seat_numlist: 选择教室
        :return:一个座位的字典  座位：人
        '''
        week_list = Seat.SearchDatenum(time)
        result_dict = {}
        vip_list = {}
        for i in seatnum_list:
            if i in self.seat_dic_for_each:
                vip_list.update({i:self.seat_dic_for_each[i]})
            else:
                vip_list.update({i:0})

        for i in seatnum_list:
            if vip_list[i]!=0:
                vip_df = self.seat_dic_for_each[vip_list[i][0]].fillna(0)
                df_class_time = vip_df[week_list[1]][classnum]
                if df_class_time!=0:
                    df_class_time = vip_df[week_list[1]][classnum].split('\n')
                    week_list = Seat.SearchWeeknum(df_class_time)
                    if week_list[0] in week_list:
                        result_dict.update({i:'空闲'})
                    else:
                        result_dict.update({i:'占用'})
                else:
                    result_dict.update({i:'占用'})
            else:
                result_dict.update({i:'未分配'})
        time = 0
        for i in seatnum_list:
            if result_dict[i] == '空闲':
                for j in range(classnum, 6):
                    df_class_time_next = vip_df['Wed'][j]
                    if df_class_time_next != 0:
                        time += 45
                    else:
                        break
                result_dict.update({i: '空闲时间:' + str(time)})
        return result_dict


    def show_search(self,dic):
        '''
        给出时间（状态）、座位和人的接口
        :param dic:search传进来的
        :return:两个字典
        '''
        pass



