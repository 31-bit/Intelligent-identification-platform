from Collector import Collector
from Scheduler import Scheduler

if __name__ == '__main__':
    collector = Collector(camera_id=0)
    scheduler = Scheduler(collector)
    scheduler.run()