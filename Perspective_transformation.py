# MA
import math
import numpy as np


class Perspective_transformation:
    def __init__(self):
        self.rotation_inverse = np.array([[-0.115659, 0.988251979, 0.099899485], [0.79096401, 0.030796248, 0.61108731],
                                          [0.600831655, 0.149694944, -0.785234]], dtype=np.float32)

        self.cam_inverse = np.array([[0.002757224, 0, -1.763244611], [0, 0.002757224, -0.991221951], [0, 0, 1]],
                                    dtype=np.float32)

        self.scale = 904.6029

        self.transition_vector = np.array([[866.94915], [341.171439], [1061.64967]], dtype=np.float32)

    def transfer_2d_to_3d(self, u, v):
        pixel_coordinates = np.array([[u], [v], [1]], dtype=np.float32)
        cam_times_pixel = np.matmul(self.cam_inverse, pixel_coordinates)
        cam_times_pixel_t = np.subtract(cam_times_pixel, self.transition_vector)
        scale_in = self.scale * cam_times_pixel_t
        self.point = np.matmul(self.rotation_inverse, scale_in)
        x_coordinate = (self.point[0], self.point[1])[0][0]
        y_coordinate = (self.point[0], self.point[1])[1][0]
        return x_coordinate, y_coordinate

    def get_real_distance(self, worker_loc, equipment_loc):
        real_distance = math.sqrt(((worker_loc[0] - equipment_loc[0]) ** 2) + ((worker_loc[1] - equipment_loc[1]) ** 2))
        return float("%.2f" % real_distance) / 100
