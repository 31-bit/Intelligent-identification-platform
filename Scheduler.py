import Collector

def collector_sheduler(camera_id):
    Collector.fetch_image(camera_id)

if __name__ == '__main__':
    collector_sheduler(0)