""" main process of maniviz"""
from maniviz.maniplot import ManipulatorVisualizer

def main() -> None:
    """ main process """
    # plot example for debug
    m = ManipulatorVisualizer(
        manipulator_type="scara",
        fig_xlim=[],
        fig_ylim=[],
        num_of_links= 5,
        len_of_links=[1.0, 2.0, 3.0, 4.0, 5.0],
        base_pos = [-1.0, 3.0],
        initial_state_type = "joint_angles", # "joint_angles" or "joint_positions"
        initial_joint_angles = [0.3, 0.6, 0.9, 0.6, 0.3],
    )
    m.echo_info()
    m.showfig()
