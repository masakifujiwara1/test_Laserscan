#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

TARGET_ANGLE = 180 # deg

class calc_ray_node():
    def __init__(self):
        rospy.init_node("calc_ray_distance", anonymous=True)
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback)
        self.scan_distance = 0
        self.scan_min = 0
        self.scan_max = 0
        self.scan_increment = 0
        self.scan_ranges = []
        self.scan_increment_deg = 0
    
    def callback(self, data):
        self.scan_ranges = list(data.ranges)
        self.scan_min = data.angle_min
        self.scan_max = data.angle_max
        self.scan_increment = data.angle_increment
        self.scan_increment_deg = int((self.scan_increment * 180) / 3.14)

    def loop(self):
        # print(self.scan_min, self.scan_max)
        try:
            print(self.scan_ranges[int(TARGET_ANGLE/self.scan_increment_deg)]) 
        except:
            pass

if __name__ == "__main__":
    rg = calc_ray_node()
    DURATION = 0.2
    r = rospy.Rate(1 / DURATION)
    while not rospy.is_shutdown():
        rg.loop()
        r.sleep()