from random import randint
import datetime
import nxbt

from CustomCommon import CustomCommon


def random_colour():

    return [
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    ]

def main():
    # Init NXBT
    nx = nxbt.Nxbt()

    # Get a list of all available Bluetooth adapters
    adapters = nx.get_available_adapters()
    # Prepare a list to store the indexes of the
    # created controllers.
    controller_index = []
    # Loop over all Bluetooth adapters and create
    # Switch Pro Controllers
    for i in range(0, len(adapters)):
        index = nx.create_controller(
            nxbt.PRO_CONTROLLER,
            adapter_path=adapters[i],
            colour_body=random_colour(),
            colour_buttons=random_colour())
        controller_index.append(index)

    # Select the last controller for input
    controller_index = controller_index[-1]
    print('接続中...')

    # Wait for the switch to connect to the controller
    nx.wait_for_connection(controller_index)
    print('接続完了！')

    custom = CustomCommon(nx, controller_index)

    print('ゲームを開始します！')
    # NOTE: ゲームの起動
    custom.game_start()

    now = datetime.datetime.now()
    # NOTE: 任意の時間を設定
    after_hour = datetime.timedelta(hours=00, minutes=10)

    print('お金稼ぎスタート！')
    while True:
        cap_img = custom.get_capture()
        if custom.check_report(cap_img):
            print('レポートを書きます')
            # NOTE: レポート実行
            custom.report()
            print('レポートを書きました')
            # NOTE: 設定時間を経過しているかつレポートが終わったタイミングで処理終了
            if not datetime.datetime.now() < now + after_hour:
                break

        if custom.check_re_entry(cap_img):
            print('休憩いたします。。。')
            custom.restart()
            print('業務を再開いたします。')
        custom.streak_button()

    print('本日の業務を終了します。。')
    print('お疲れ様でした。。。')


if __name__ == "__main__":
    main()
