from constans import all_speeds, cloud_coords


class Cloud:
    def __init__(self):
        self.width, self.height = 500, 600

    def change_h(self):
        for i in range(len(cloud_coords)):
            if cloud_coords[i][1] <= self.height:
                new_y = cloud_coords[i][1] + all_speeds[cloud_coords.index(cloud_coords[i])]
                cloud_coords[i] = cloud_coords[i][0], new_y
            else:
                cloud_coords[i] = cloud_coords[i][0], -30
