from recording import recording
from os import walk
from preproches import cut_audio, wav_to_picture
from model import predicting_model, train_and_check_model


def train():
    name_audio_scream = 'val_scream'
    dir_train_scream = 'val\\scream'
    time = 20

    recording(name_audio_scream, time)
    cut_audio(name_audio_scream, time)
    wav_to_picture(name_audio_scream, dir_train_scream)

    name_audio_vote = 'val_vote'
    dir_train_vote = 'val\\vote'
    time = 20

    recording(name_audio_vote, time)
    cut_audio(name_audio_vote, time)
    wav_to_picture(name_audio_vote, dir_train_vote)


def use_code():
    name_audio_predict = 'predict'
    dir_train_predict = 'predict'
    time = 10

    recording(name_audio_predict, time)
    cut_audio(name_audio_predict, time)
    wav_to_picture(name_audio_predict, dir_train_predict)

    wavs = []
    for (_, _, filenames) in walk(dir_train_predict + "Plots"):
        wavs.extend(filenames)
        break

    result = []
    for el in wavs:
        result.append(predicting_model('predictPlots\\' + el))

    result = [i for i in range(len(result)) if result[i] == 0]

    print(f'Вы кричали на {result} секундах')

use_code()