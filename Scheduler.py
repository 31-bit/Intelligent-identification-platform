# # Importing the CronTab class from the module
# from crontab import CronTab
#
# cron = CronTab('*/5 * * * * *')
# # 字符串中python解释器地址和允许内容地址依次
# job = cron.new(command='/bin/python /CronTask/CollectorControl.py')
# # job.setall('*/0.2 * * * *')
#
# # 验证cron表达式是否有效
# if job.is_valid():
#     # 将任务添加到cron表中
#     cron.write()
#
# # 检查是否有任务需要执行
# cron.run_pending()
# from crontab import CronTab
#
# if __name__ == '__main__':
#     # 创建 CronTab 对象
#     cron = CronTab(user= True)
#
#     # 添加任务到 CronTab 对象
#     job = cron.new(command='python /Collector.py')
#     job.setall('*/5 * * * *')
#
#     # 保存任务到 CronTab 对象
#     cron.write()


import schedule
import time


class Scheduler:
    def __init__(self, collector):
        self.collector = collector

    def run(self):
        schedule.every(5).seconds.do(self.collector.run)
        while True:
            schedule.run_pending()
            time.sleep(1)
        self.collector.release()