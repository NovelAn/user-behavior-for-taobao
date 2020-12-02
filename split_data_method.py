import os
from datetime import datetime
class splitData(object):
    def __init__(self,original_file_path=None, spliteddata_savedpath=None):
        '''
        :param original_file_path:
        :param spliteddata_savedpath:
        '''
        self.original_file_path = original_file_path
        self.spliteddata_savedpath = spliteddata_savedpath

    def mkdir(self):
        '''
        Create a directory to save the splited data

        OUTPUTS:
        path - (os.path) directory path that save the splited data
        '''
        path = self.spliteddata_savedpath
        path = path.strip()
        path = path.rstrip('\\')

        if not os.path.exists(path):
            os.makedirs(path)
            print(path + '--- 创建成功')
            return path
        else:
            print(path + '--- 目录已存在')
            return path
    def Main(self):
        '''
        This function is useful for splitting a large data_set into several small data_sets
        INPUTS:
        source_dir - (os.path) the path that data comes from
        target_dir - (os.path) the path that splited data need to save

        '''

        target_dir = self.mkdir()
        # count_num
        flag = 0
        # file_name
        name = 1
        # data_save
        data_list = []
        start_time = datetime.now()
        print('开始时间:{}'.format(start_time.strftime('%Y-%m-%d %H:%M:%S')))

        with open(self.original_file_path) as f_source:
            for line in f_source:
                flag += 1
                data_list.append(line)
                if flag == 5000000:
                    with open(os.path.join(target_dir,'UB_split_'+str(name))+'.csv','w+') as f_target:
                        for data in data_list:
                            f_target.write(data)
                    name += 1
                    flag = 0
                    data_list = []
                else:
                    continue

        # 处理最后一批行数少于500w行的数据

        with open(os.path.join(target_dir,'UB_split_'+str(name))+'.csv','w+') as f_target:
            for data in data_list:
                f_target.write(data)

        end_time = datetime.now()
        run_time = (end_time - start_time).seconds
        print('结束时间：{}'.format(end_time.strftime('%Y-%m-%d %H:%M:%S')))
        print('程序运行的时间是：{}秒'.format(run_time))
#
# if __name__ == '__main__':
#     Splitdata = splitData('')