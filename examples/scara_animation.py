""" example script to animate scara robot """
import numpy as np
from maniviz.maniplot import ManipulatorVisualizer

# plot example
m = ManipulatorVisualizer(
    manipulator_type="scara",
    fig_xlim=[],
    fig_ylim=[],
    num_of_links=5,
    len_of_links=[1.0, 2.0, 3.0, 4.0, 5.0],
    base_pos=[-1.0, 3.0],
    initial_state_type="joint_angles",
    initial_joint_angles=[0.3, 0.6, 0.9, 0.6, 0.3],
)
m.echo_info()

# animate figures
for i in range(100):
    _buf = m.get_joint_angles()
    _buf[0] = np.sin(i/10)
    m.set_joint_angles(_buf)
    m.updatefig(duration=0.1)
