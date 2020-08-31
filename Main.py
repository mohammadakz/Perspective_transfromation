# Mohammad Akbarzadeh
# August 2020
# This is an example for perspective transformation project


# import class
from Perspective_transformation import Perspective_transformation

if __name__ == '__main__':
    # equipment pixel location
    eq = Perspective_transformation()
    equipment_world_coordinate = eq.transfer_2d_to_3d(100, 200)

    # worker pixel location
    wo = Perspective_transformation()
    worker_world_coordinate = wo.transfer_2d_to_3d(200, 150)

    # calculate the distance in meters
    d = Perspective_transformation()
    distance = d.get_real_distance(worker_world_coordinate, equipment_world_coordinate)
    print(distance, "m")
