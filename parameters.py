import torch
import os

DATA_FOLDER = os.path.abspath("C:/Users/fgarboni/PycharmProjects/HW2")

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
VOCABULARY_PATH = 'vocab.pkl'
DATASET_PATH = 'data.pkl'
PREPROCESSED_FILE_PATH = os.path.join('data.h5')

BATCH_SIZE = 2
N_WORKERS = 2


def image_path(image_id=None, train=True):
    t = 'train2014' if train else 'val2014'
    if image_id:
        name = 'COCO_' + t + '_%012d' % image_id + '.jpg'
    else:
        name = ''
    return os.path.join(DATA_FOLDER, t, name)


def questions_path(train=True):
    filename = 'v2_OpenEnded_mscoco_train2014_questions.json' if train else 'v2_OpenEnded_mscoco_train2014_questions.json'
    return os.path.join(DATA_FOLDER, filename)


def answers_path(train=True):
    filename = 'v2_mscoco_train2014_annotations.json' if train else 'v2_mscoco_train2014_annotations.json'
    return os.path.join(DATA_FOLDER, filename)
