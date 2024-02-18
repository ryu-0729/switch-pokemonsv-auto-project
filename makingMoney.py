import datetime
import time
from random import randint

from nxbt import PRO_CONTROLLER, Buttons, Nxbt, Sticks


def random_colour():

    return [
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    ]


def start_game(controller_index):
    for _ in range(2):
        nx.press_buttons(controller_index, [Buttons.B], down=1.0)
        time.sleep(2)

    for _ in range(4):
        nx.tilt_stick(controller_index, Sticks.LEFT_STICK, -100, 0, 0.25, 0.25)

    nx.tilt_stick(controller_index, Sticks.LEFT_STICK, 0, 100, 0.25, 0.25)
    for _ in range(2):
        nx.press_buttons(controller_index, [Buttons.A], down=1.0)


if __name__ == "__main__":

    # Init NXBT
    nx = Nxbt()

    # Get a list of all available Bluetooth adapters
    adapters = nx.get_available_adapters()
    # Prepare a list to store the indexes of the
    # created controllers.
    controller_index = []
    # Loop over all Bluetooth adapters and create
    # Switch Pro Controllers
    for i in range(0, len(adapters)):
        index = nx.create_controller(
            PRO_CONTROLLER,
            adapter_path=adapters[i],
            colour_body=random_colour(),
            colour_buttons=random_colour(),
        )
        controller_index.append(index)

    # Select the last controller for input
    controller_index = controller_index[-1]
    print("connecting")

    # Wait for the switch to connect to the controller
    nx.wait_for_connection(controller_index)

    # NOTE: ゲームの起動
    start_game(controller_index)
    time.sleep(25)

    now = datetime.datetime.now()
    # NOTE: 任意の時間を設定
    after_hour = datetime.timedelta(hours=0, minutes=30)

    print(datetime.datetime.now())
    print(now + after_hour)

    # NOTE: 指定した時間までAボタン連打
    while datetime.datetime.now() < now + after_hour:
        print(datetime.datetime.now())
        nx.press_buttons(controller_index, [Buttons.R], 1.0)
        nx.press_buttons(controller_index, [Buttons.A], 1.0)

    print("Exiting...")
