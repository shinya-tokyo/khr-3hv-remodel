# KHR-3HV-remodel
 Remodel Program of KHR-3HV (Humanoid Robot of Kondo Kagaku).
 
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
 
 In "RCB" directory put "sample" directory.
 
 put the "./khr-3hv-remodel/sample" files into it.
 
 - Usage -

 In "/Desktop/robot_kinetics.sh" 's 6 or 7th row,
 there are next sentences. 
 
 Choose one and comment out the other.
 
   python3 khr_ojigi_vc_ir.py
   python3 khr_ojigi_vc_ir_tv.py
 
 1. Run "robot_parent.sh" using the "Terminal".
  
 3. The Voice recognition will start.

 4.1. If you choose "python3 khr_ojigi_vc_ir.py", the airconditioner remote control mode will appears.
      (Say "Atsui" <Hot in Japanese> and the "Keshite" <Turn off in Japanese>)
 
 4.2. If you choose "python3 khr_ojigi_vc_ir_tv.py", the TV remote control mode appears.
      (Say "Tsukete" <Turn on in Japanese> or "Keshite" <Turn off in Japanese>)
