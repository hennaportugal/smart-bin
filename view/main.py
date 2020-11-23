from proximity_sensor import ProximitySensor

def main():
    plasticBottle_sensor = ProximitySensor(14, 15)
    alumniumCan_sensor = ProximitySensor(23, 24)
    paperCup_sensor = ProximitySensor(25, 8)
    unclassified_sensor = ProximitySensor(7, 1)

    plasticBottle_sensor.read_distance()
    alumniumCan_sensor.display_distance()
    paperCup_sensor.on_bin_full()
    unclassified_sensor.run()

if __name__ == '__main__':
    main()

