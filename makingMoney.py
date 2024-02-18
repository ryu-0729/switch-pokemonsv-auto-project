import datetime

from CustomCommon import CustomCommon


def main():
    custom = CustomCommon()

    custom.setup_controller()
    print("接続中...")

    custom.nx.wait_for_connection(custom.controller_index)
    print("接続完了！")

    print("ゲームを開始します！")
    custom.game_start()

    now = datetime.datetime.now()
    # NOTE: 任意の時間を設定
    after_hour = datetime.timedelta(hours=00, minutes=10)

    print("お金稼ぎスタート！")
    while True:
        cap_img = custom.get_capture()
        if custom.check_report(cap_img):
            print("レポートを書きます")
            # NOTE: レポート実行
            custom.report()
            print("レポートを書きました")
            # NOTE: 設定時間を経過しているかつレポートが終わったタイミングで処理終了
            if not datetime.datetime.now() < now + after_hour:
                break

        if custom.check_re_entry(cap_img):
            print("休憩いたします。。。")
            custom.restart()
            print("業務を再開いたします。")
        custom.streak_button()

    print("本日の業務を終了します。。")
    print("お疲れ様でした。。。")


if __name__ == "__main__":
    main()
