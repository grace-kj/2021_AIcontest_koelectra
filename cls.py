import argparse
import json
import logging
import os
import glob

import numpy as np
import torch

from transformers import ElectraModel, ElectraTokenizer

cos = torch.nn.CosineSimilarity()
tokenizer = ElectraTokenizer.from_pretrained('monologg/koelectra-base-v3-discriminator')
model = ElectraModel.from_pretrained('monologg/koelectra-base-v3-discriminator')

text1 = "나는 지금 학교에 간다."
text2 = "나는 지금 학원에 간다."

inputs_1 = tokenizer(text1, return_tensors='pt')
inputs_2 = tokenizer(text2, return_tensors='pt')

cls1 = model(**inputs_1)[0][:, 0]
cls2 = model(**inputs_2)[0][:, 0]

cosine_similarity = cos(cls1, cls2).item()

print(cosine_similarity)