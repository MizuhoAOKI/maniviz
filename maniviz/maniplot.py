""" class to plot manipulator """
from typing import Union, List
from maniviz.utils.logger import initialize_logging
import rich
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.table import Table
import numpy as np

logger = initialize_logging(__name__)

# TODO
# - Add joint_angles_vel input

class ScaraManipulator:
    """ class to define manipulator model """
    def __init__(
        self,
        num_of_links: int = 2,
        len_of_links: List[float] = [1.0, 1.0],
        base_pos: List[float] = [1.0, 1.0],
        initial_state_type: str = "joint_angles", # "joint_angles, joint_positions"
        initial_joint_angles: List[float] = [0.3, 0.6],
        initial_joint_positions_xy: List[Union[float, float]] = [[0.5, 0.5], [1.5, 1.5]],
        ) -> None:

        # save arguments
        self.num_of_links = num_of_links # == (num of joints)
        if self.num_of_links < 1:
            logger.error("Invalid value of num_of_links is specified.")
            raise AttributeError
        self.len_of_links = len_of_links
        self.base_pos = base_pos

        # declare state variables
        self.joint_positions_xy = initial_joint_positions_xy
        self.joint_angles = initial_joint_angles

        # calculate manipulator attitude
        if initial_state_type == "joint_angles":
            self.update_attitude_with_joint_angles()
        elif initial_state_type == "joint_positions_xy":
            self.update_attitude_with_joint_positions()
        else:
            logger.error(f"Invalid initial_state_type '{initial_state_type}' is specified. ")
            raise AttributeError

        # announcement
        logger.debug("Finish building a SCARA manipulator")

    def echo_info(self):
        """ display manipulator's info """
        # Title panel
        rich.print(
            Panel(Text("Info of the SCARA Manipulator", justify="left"), expand=False)
        )

        # Print table of joints
        _console = Console()
        _table = Table(show_header=True, header_style="bold")
        _table.add_column("Joint Number", justify="center")
        _table.add_column("Link Length (m)", justify="center")
        _table.add_column("Angle (rad) ", justify="center")
        _table.add_column("Position [X(m),Y(m)]", justify="center")
        for i in range(self.num_of_links):
            _format_pos_str = []
            for pos in self.joint_positions_xy[i]:
                _format_pos_str.append(f"{pos:.3f}")
            _table.add_row(str(i), f"{self.len_of_links[i]:.1f}", f"{self.joint_angles[i]:.3f}", f"{_format_pos_str}")
        _console.print(_table)

    def get_joint_angles(self) -> List[float]:
        """ return list of joint angles """
        return self.joint_angles

    def get_joint_positions(self) -> List[float]:
        """ return list of joint positions """
        return self.joint_positions_xy

    def set_joint_angles(self, joint_angles:List[float]) -> None:
        """ set joint angles """
        self.joint_angles = joint_angles
        self.update_attitude_with_joint_angles()

    def set_joint_positions(self, joint_positions_xy:List[Union[float, float]]):
        """ set joint positions """
        self.joint_positions_xy = joint_positions_xy
        self.update_attitude_with_joint_positions()

    def update_attitude_with_joint_angles(self) -> None:
        """ use forward kinematics and update joint positions with latest joint angles """
        # clear joint positions
        self.joint_positions_xy = [self.base_pos]

        _len = self.len_of_links
        _angle_cumsum = np.cumsum(self.joint_angles)

        for i in range(self.num_of_links):
            _pos = self.joint_positions_xy[-1]
            _new_pos = [0.0, 0.0]
            _new_pos[0] = _pos[0] + _len[i] * np.cos(_angle_cumsum[i]) # x pos
            _new_pos[1] = _pos[1] + _len[i] * np.sin(_angle_cumsum[i]) # y pos
            self.joint_positions_xy.append(_new_pos)

    def update_attitude_with_joint_positions(self) -> None:
        """ use forward kinematics and update joint angles with latest joint positions """
        pass

class ManipulatorVisualizer:
    """ manipulator visualizer """
    def __init__(
        self,
        manipulator_type: str="scara",
        **kwargs
        # num_of_links: int = 2,
        # len_of_links: List[float] = [1.0, 1.0],
        # base_pos: List[float] = [0.0, 0.0],
        # initial_state_type: str = "joint_angles", # "joint_angles, joint_positions"
        # initial_joint_angles: List[float] = [0.3, 0.6],
        # initial_joint_positions_xy: List[Union[float, float]] = [[0.5, 0.5], [1.5, 1.5]],
        ) -> None:

        # call constructor of the specified type of a manipulator
        if manipulator_type == "scara": # corresponding to 2d visualization
            # instantiate a scara manipulator
            # self.mani_obj = ScaraManipulator(
            #     num_of_links=num_of_links,
            #     len_of_links=len_of_links,
            #     base_pos=base_pos,
            #     initial_state_type=initial_state_type,
            #     initial_joint_angles=initial_joint_angles,
            #     initial_joint_positions_xy=initial_joint_positions_xy
            # )
            self.mani_obj = ScaraManipulator(**kwargs)

        elif manipulator_type == "vertical_multi_jointed": # corresponding to 3d visualization
            raise NotImplementedError
        else:
            logger.error(f"Invalid manipulator type '{manipulator_type}' is specified. ")
            raise AttributeError

    def echo_info(self) -> None:
        """ notice this manipulator's description """
        self.mani_obj.echo_info()

    # ここのgetter, setterは**kwargsで引数渡すだけ.
    def get_joint_angles(self) -> List[float]:
        """ return list of joint angles """
        return self.mani_obj.get_joint_angles()

    def get_joint_potisions(self) -> List[float]:
        """ return list of joint positions """
        return self.mani_obj.get_joint_positions()

    def set_joint_angles(self, arg) -> None:
        """ set joint angles """
        self.mani_obj.set_joint_angles(arg)

    def set_joint_positions(self, *args) -> None:
        """ set joint angle positions """
        self.mani_obj.set_joint_angles(args)

    def showfig(self) -> None:
        """ show figure """
        pass

    def savefig(self) -> None:
        """ save figure """
        pass

    def updatefig(self) -> None:
        """ update figure """
        pass

if __name__=="__main__":
    # plot example
    m = ManipulatorVisualizer(
        num_of_links= 2,
        len_of_links=[1.0, 1.0],
        base_pos = [0.0, 0.0],
        initial_state_type = "joint_angles", # "joint_angles" or "joint_positions"
        initial_joint_angles = [0.3, 0.6],
        initial_joint_positions_xy = [[0.5, 0.5], [1.5, 1.5]],
    )
    m.set_joint_angles([2.0, 3.0])
    m.echo_info()