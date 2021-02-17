This project is based on the OpenCV perspective transformation. The goal is to find the real-world distance between objects (e.g., workers, equipment) or locating objects in specific zones using pixel coordinates and camera calibration parameters. Capture.png file shows an example of the proposed method. The average error measured for this project is around 1.5 m.
To get the world coordinates run
```
Main.py
```
wehere, (100, 200) are the pixel coordinates of the equioment
```
equipment_world_coordinate = eq.transfer_2d_to_3d(100, 200)
```
The image bellow shows perspective locating of equipments on the construction site.

![alt text](https://github.com/mohammadakz/Perspective_transfromation/blob/master/Capture.PNG)
