from pydub import AudioSegment
import os
from os import walk
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# direct_wav = 'scream'
# direct_wav_1 = 'vote'
#
# direct_picture = 'scream'
# direct_picture_1 = 'vote'

def cut_audio(direct, time):
    if not os.path.exists(direct):
        os.makedirs(direct)
    count = 1
    for i in range(1,time,1):
        t1 = i * 1000
        t2 = (i+1) * 1000
        newAudio = AudioSegment.from_wav(direct + ".wav")
        newAudio = newAudio[t1:t2]
        newAudio.export(direct + '/'+str(count)+'.wav', format="wav")
        print(count)
        count += 1

def wav_to_picture(direct_wav, direct_picture):
    if not os.path.exists(direct_picture + "Plots"):
        os.makedirs(direct_picture + "Plots")
    wavs = []
    for (_,_,filenames) in walk(direct_wav):
        wavs.extend(filenames)
        break
    for wav in wavs:
        input_data = read(direct_wav + "/" + wav)
        audio = input_data[1]
        plt.plot(audio)
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.savefig(direct_picture + "Plots/" + wav.split('.')[0] + '.png')
        plt.close('all')

# cut_audio(direct_wav)
# cut_audio(direct_wav_1)
#
# wav_to_picture(direct_wav, direct_picture)
# wav_to_picture(direct_wav_1, direct_picture_1)




