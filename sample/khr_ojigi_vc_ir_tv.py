#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import ac_on
import socket
import string
import subprocess
import threading

def jtalk(t):

    fout_utf = open('voice.txt', 'w', encoding='utf-8')
    fout_utf.write(t)
    fout_utf.close()

    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    # htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','test.wav']
    voice=['voice.txt']
    cmd=open_jtalk+mech+htsvoice+speed+outwav+voice
    # c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    # c.stdin.write(t.encode('utf-8'))
    # c.stdin.close()
    # c.wait()
    c = subprocess.call(cmd)


    # aplay = ['aplay','-q','test.wav','-Dhw:1,1'] # HDMI Sound Output
    aplay = ['aplay','-q','test.wav','-Dhw:1,0'] # Analog Sound Output
    # wr = subprocess.Popen(aplay)
    wr = subprocess.call(aplay)

def remocon_on():
    # threading.current_thread().nameはgetName()を呼び出す
    print("task: {} (thread name: {})".format(n, threading.current_thread().name))
    time.sleep(1)
    subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat tv_on-off.dat`", shell=True)
    subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat tv_ouj.dat`", shell=True)
    time.sleep(1)

def remocon_off():
    # threading.current_thread().nameはgetName()を呼び出す
    print("task: {} (thread name: {})".format(n, threading.current_thread().name))
    time.sleep(1)
    subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat tv_on-off.dat`", shell=True)
    time.sleep(1)

def main():
    
    print(0)
        
    host = 'localhost'
    port = 10500 # default
    # port = 25

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    print(1)
    
    # text = 'あの竹垣に竹立て掛けたかったのは、竹立てかけたかったから、竹立てかけた'
    voice_flg = 0
    data = ""
        
    sys.path.append('../Rcb4Lib') #Rcb4Libの検索パスを追加
    
    print(1.0)
    
    from Rcb4BaseLib import Rcb4BaseLib            #Rcb4BaseLib.pyの中のRcb4BaseLibが使えるように設定
    import time                   #timeが使えるように宣言

    rcb4 = Rcb4BaseLib()      #rcb4をインスタンス(定義)
            
    # rcb4.open('/dev/ttyAMA0',115200,1.3)  #(portName,bundrate,timeout(s))
    rcb4.open('/dev/ttyUSB0',115200,1.3)
    
    if rcb4.checkAcknowledge() == True:  #通信が返ってきたとき
        
        print(1.1)
        
        # t1 = threading.Thread(target=remocon_on, args=("t1",))
        # t2 = threading.Thread(target=remocon_off, args=("t2",))

        print(1.2)

        print ('Motion 55 Voice IR TV PG START!!!')
    
        while True:
            
            print(2.0)

            # "/RECOGOUT"を受信するまで、一回分の音声データを全部読み込む。
            # while (string.find(data, "\n.") == -1):
            while (data.find("\n.") == -1): # For Python 3
                # data = data + (sock.recv(1024)).decode("sjis")
                data = data + (sock.recv(1024)).decode("utf-8")
                # data = data + sock.recv(1024)
            
            print(2.1)

            # 音声XMLデータから、<WORD>を抽出して音声テキスト文に連結する。
            strTemp = ""
                        
            for line in data.split('\n'):
                index = line.find('WORD="')

                if index != -1:
                    line = line[index + 6:line.find('"', index + 6)]
                    if line != "[s]":
                        strTemp = strTemp + line
            
            print(2.2)
         
            # if strTemp in ["あつい", "あつい。", "暑い", "暑い。", "つけて", "つけて。", "付けて", "付けて。", "エアコンつけて", "エアコンつけて。", "エアコンをつけて", "エアコンをつけて。"]:
            # if strTemp == ("暑い。"):
            if strTemp in ["てれび", "てれび。", "テレビ", "テレビ。", "TV", "つけて", "つけて。", "付けて", "付けて。", "テレビつけて", "テレビつけて。", "テレビをつけて", "テレビをつけて。", "テレビつけて", "てれびつけて。", "てれびをつけて", "てれびをつけて。", "テレビつける", "テレビつける。", "テレビをつける", "テレビをつける。",]:
            
                print("結果(テレビ入):" + strTemp)

                ac_on.jtalk('テレビをつけます。')
                print("テレビをつけます")
                    
                # if(voice_flg == 0):
                    # jtalk(text) # 発話
                    # time.sleep(0.1) # 間合いの時間
                    # ac_on.jtalk('暑いので、エアコンをつけます。')
                    # jtalk.text("暑いので、エアコンをつけます。")
                    # print("エアコンをつけます")
                    # voice_flg = 1
                
                print ('MotionPlay(55)')
                rcb4.motionPlay(55)

                # t1.start()

                while True:     #モーションの再生が終わるまで繰り返し

                    motionNum = rcb4.getMotionPlayNum()   #現在再生されているモーション番号を取得
                    if motionNum < 0:                     #モーション番号が0より小さい場合はエラー
                        print('motion get error',motionNum)
                        break
                    if motionNum == 0:                    #モーション番号が0のときは再生されていない状態
                        print('stop motion or idle')
                        break
                    
                    print('play motion -> ',motionNum)
                    time.sleep(0.1)
            
                subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat /home/pi/I2C0x52-IR/tv_on-off.dat`", shell=True)
                subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat /home/pi/I2C0x52-IR/tv_ouj.dat`", shell=True)
        
        
            elif strTemp in ["けして", "テレビ消して", "テレビ消して。", "テレビを消して", "テレビを消して。", "テレビ", ]:
                
                print("結果(エアコン切):" + strTemp)
                
                print("テレビを消します")
                ac_on.jtalk('テレビをけします。')
                
                # t2.start()
                subprocess.call("python /home/pi/I2C0x52-IR/IR-remocon02-commandline.py t `cat /home/pi/I2C0x52-IR/tv_on-off.dat`", shell=True)
                
            elif strTemp != "":
                print("結果:" + strTemp)

            data = ""
            
    else:  #通信が返ってきていないときはエラー
        print ('checkAcknowledge error')
      
    rcb4.close()

if __name__ == '__main__':
    main()
