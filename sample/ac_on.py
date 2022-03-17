#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    # htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','temp.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','temp.wav','-Dhw:1,0']
    wr = subprocess.Popen(aplay)

def main():
    text = 'エアコンをつけます。'
    jtalk(text)

if __name__ == '__main__':
    main()
