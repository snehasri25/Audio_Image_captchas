# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import pandas as pd
import librosa
import argparse
import os


def save_spectrogram(audio_fname, image_fname):
    y, sr = librosa.load(audio_fname)
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ])
    S = librosa.feature.melspectrogram(y, sr=sr)
    log_S = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(log_S)
    #fig1=plt.figure(figsize=(1.28, .64), dpi=100)
    #fig1 = plt.gcf()
    plt.savefig(image_fname,bbox_inches=None,pad_inches=0)
    plt.close()
    

def audio_to_spectrogram(audio_dir_path, image_dir_path=None):
    file_list = os.listdir(audio_dir_path)
    print(audio_dir_path)
    for paths in file_list:
        #print(paths)
        audio_filename = paths
        aud_fname = audio_dir_path +'\\'+ paths
        image_fname = audio_filename.split('.')[0] + '.png'
        if image_dir_path:
            image_fname = image_dir_path + '\\' + image_fname
        #print(image_fname)
        #plot_spectrogram(image_fname)
        try:
            save_spectrogram(aud_fname, image_fname)
        except ValueError as verr:
            print('Failed to process %s %s' % (image_fname, verr))
        # wait between every batch for xyz seconds

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mp3dir', help='mp3 directory', type=str)
    parser.add_argument('--imagedir', help='image directory', type=str)
    args = parser.parse_args()

    if args.mp3dir is None:
        print("Please specify mp3 directory")
        exit(1)

    if args.imagedir is None:
        print("Please specify image directory")
        exit(1)
        
    audio_to_spectrogram(args.mp3dir,args.imagedir)

if __name__ == '__main__':
    main()