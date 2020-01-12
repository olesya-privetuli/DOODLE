from constans import all_speeds, cloud_koords


class Cloud:
    def __init__(self):
        self.width, self.height = 500, 600

    def change_h(self):
        for i in range(len(cloud_koords)):
            if cloud_koords[i][1] <= self.height:
                new_y = cloud_koords[i][1] + all_speeds[cloud_koords.index(cloud_koords[i])]
                cloud_koords[i] = cloud_koords[i][0], new_y
            else:
                cloud_koords[i] = cloud_koords[i][0], -30
