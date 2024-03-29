# switch-pokemonsv-auto-project
ポケモンSVの自動化プロジェクト

## プログラムの内容
ポケモンSVの学校最強大会を無限に周回するプログラム  
こちらのプログラムは画像処理を行うため、キャプチャーボード等が必要になります。  
→画像処理等を行わないプログラムは[こちら](https://github.com/ryu-0729/switch-pokemonsv-auto-project/tree/old_making_money)を参照ください

- 機能
  - 学校最強大会終了後のレポート機能
  - 学校最強大会中のリタイア時のリエントリー機能

## 使用技術/システム構成
- Raspberry Pi 3 Model B
- Raspberry Pi OS
- [nxbt](https://github.com/Brikwerk/nxbt)
- Python3.9
- OpenCV
- Bluetoothアダプタ
- キャプチャーボード

## インストール

#### Step1
まずラズパイのセットアップ
詳しくは下記のサイトが参考になります。  
[ラズパイのインストール](https://www.indoorcorgielec.com/resources/raspberry-pi/raspberry-pi-os%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/)  
[ラズパイの初期設定](https://www.indoorcorgielec.com/resources/raspberry-pi/raspberry-pi-setup/)

#### Step2
次は下記コマンドを実行

```
$ sudo apt update
$ sudo apt upgrade
```

#### Step3
プロジェクトのcloneとnxbtのインストール

```
$ git clone https://github.com/ryu-0729/switch-pokemonsv-auto-project.git
$ sudo pip3 install nxbt
```

#### Step4
OpenCVのインストール  
※ おそらく下記でインストールできたと思いますが、適宜インストール方法は調べていただければと思います。

```
$ sudo apt install libopencv-dev opencv-data
$ sudo python3 -m pip install opencv-python
```

#### Step5
Bluetoothアダプタの設定と内部Bluetoothの無効化  
ここの設定を行わないとswitchに接続がうまくいかないので必須（ラズパイ4ではどうなのかはわかりません。。）  
内部Bluetoothの無効化については下記サイトを参考
[内部Bluetoothの無効化](https://pcvogel.sarakura.net/2019/08/17/31966)  
そして再起動

#### Step6
キャプチャーボードとラズパイを接続  
下記構成図になります。

![スクリーンショット 2023-01-22 23 12 23](https://user-images.githubusercontent.com/65229017/227762609-fd788350-23f9-40ff-8968-81f17de22a43.png)


## makingMoney.pyの実行の前に
makingMoney.pyは金稼ぎの自動化ファイルなので、switch側である程度準備をしておく必要があります。

- 準備すること
  - 学校最強大会を重労働していただくポケモン1体の準備（周回できるポケモン）
  - 学校最強大会のエントリー前でレポート
  - switch本体のスリープ設定

## makingMoney.pyの実行
あとは楽しいお金稼ぎの時間  
switch側ではホーム画面のコントローラーから「持ち方/順番を変える」を開いておく  
ターミナルから`sudo python makingMoney.py`を実行（デフォルトでは30分後に自動操作が終了するので適宜変更）  
64行目あたりの`after_hour = datetime.timedelta(hours=0, minutes=30)`の引数を何時間後に終わって欲しいかに合わせて設定すればオッケー

## その他
プログラムの内容等についてはブログにまとめますので少々お待ちをー

