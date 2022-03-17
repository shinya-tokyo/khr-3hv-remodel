# KHR-3HV-remodel add Intelligence
 日本語は下へスクロールして下さい。/ For Nihongo (Japanese), scroll down.
 
 Remodel Program of KHR-3HV (Humanoid Robot of Kondo Kagaku).
 
 This is the program source code of adding intelligence to KHR-3HV and make KHR-3HV recognize your voice, speek and remote controll the home electronics devices.
 
 After physically assemblled the KHR-3HV and tuned with the Original Software (HTH4; HeartToHeart 4),
 
 You need to connect Raspberry Pi (RPi) and KHR-3HV using "DUAL USB ADAPTER HS" and "RCB4 Python Library".
 
 See the command in the Kondo website and set it.
 
 You need to install "julius" and "Open JTalk" to your RPi.
 
 Put these 3 files on your RPi Desktop. "/Desktop"
 (RPi 4 8GB fits, since of the high processing speed)
 
 1. robot_parent.sh
 2. robot_voice_recognition.sh
 3. robot_kinetics.sh

 Installing RCB on RPi Desktop there will be a directory like "RCB".
 
 In "RCB" directory put "sample" directory, 
 and put the "./khr-3hv-remodel/sample" files into it.
 
 <<< Usage >>>

 In "/Desktop/robot_kinetics.sh" 's 6 or 7th row,
 there are next sentences. 
 
 Choose one and comment out the other.
 
   python3 khr_ojigi_vc_ir.py
   python3 khr_ojigi_vc_ir_tv.py
 
 1. Run "robot_parent.sh" using the "Terminal".
  
 2. The Voice recognition will start.

 3.1. If you choose "python3 khr_ojigi_vc_ir.py", the airconditioner remote control mode will appears.
      (Say "Atsui" <Hot in Japanese> and the "Keshite" <Turn off in Japanese>)
 
 3.2. If you choose "python3 khr_ojigi_vc_ir_tv.py", the TV remote control mode appears.
      (Say "Tsukete" <Turn on in Japanese> or "Keshite" <Turn off in Japanese>)
 
 For detail see this: 
 https://www.shinya-t.tokyo/robot/khr-3hv/intelligence/
 
 *** I've remodelded the source code of Kondo Kagaku ggot permission and uploaded here ***
 
 # KHR-3HV の改造 (知能化)

 近藤科学さん の人間型ロボットであるKHR-3HVの修正版プログラムです。
 
 KHR-3HVを物理的に組み立てて、HTH4 (HeartToHeart 4) を動かした後で、
 ラズベリーパイ(RPi)とKHR-3HVを「デュアルUSBアダプターHS」と「RCB 4 Pythonライブラリー」で接続する必要があります。
 
 近藤科学さん のホームページを見て設定して下さい。
 
 「julius」と「Open JTalk」をRPiにインストールする必要があります。
 
 
 次の3つのファイルをRPiの「デスクトップ」に置いて下さい。 ("/Desktop")
 
 (処理が早くなるので、RPi 4の8GBがよいと思います)
 
 1. robot_parent.sh
 2. robot_voice_recognition.sh
 3. robot_kinetics.sh

 RPiのデスクトップをRCBにインストールすると「RCB」ディレクトリーが出来ます。
 
 「RCB」ディレクトリーに「sample」ディレクトリーを置いて、 
 "./khr-3hv-remodel/sample"のファイルを足して下さい。
 
 <<< 使い方 >>>

 「/Desktop/robot_kinetics.sh」の6行目か7行目に、次の文があります。
 
 1つ選んで、他をコメントアウトして下さい。
   python3 khr_ojigi_vc_ir.py
   python3 khr_ojigi_vc_ir_tv.py
 
 1. 「端末」を使って、「robot_parent.sh」を動かします。
  
 2. 音声認識が始まります。
 
 3.1. 「python3 khr_ojigi_vc_ir.py」 を選んだ場合、エアコンの李顧問制御モードとなります。
      (「暑い」や「消して」と言ってください。)
 
 3.2. 「python3 khr_ojigi_vc_ir_tv.py"」をエラン場合TVリモコン制御モードとなります。
      (「つけて」や「消して」と言ってください。)
 
詳しくは、こちらをご参照ください。
https://www.shinya-t.tokyo/robot/khr-3hv/intelligence/
 
※※※ 近藤科学さん から許可をいただいて、ソースコードを使い改造したプログラムを載せました。 ※※※
