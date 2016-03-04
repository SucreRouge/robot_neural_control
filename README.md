# Robot_neural_control

This code simulates the neural control of an autonomous walking robot. This kind of control is an alternative to conventional control mechanisms since it enables a self organized adjustment of the robot's motions to a changing environment. On each of its six legs, the robot has sensors that are sensitive to contact, acceleration, current, infrared, sound and light. The signals of those sensors can be used to adjust the motions of the robot to its surroundings. The robot is controlled by an artificial neural network which generates suitable movement patterns depending on the incoming sensor signals. The network has intrinsically chaotic dynamics which have to be surpressed in order to generate stable robotic movements instead. This is realized by simultaneously detecting and stabilizing unstable periodic orbits, each of which then leads to one specific activity pattern. That way, the neural network can quickly adapt to new situations.



Reference: S. Steingrube, M. Timme, F. Wörgötter, P. Manoonpong: *Self-organized adaptation of a simple neural circuit enables complex robot behaviour*, Nature Physics 6, 224(2010)
