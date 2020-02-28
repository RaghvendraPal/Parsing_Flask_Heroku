from __future__ import absolute_import
from .ner_dict import ner_dict
import json
import sys
from numba import jit, cuda
@jit
def ner_parsing_data(prediction, X_t):
    pickle_in = open(sys.path[0]+'/ner_data/ner_model/ner_idx2tag.json')
    ner_idx2tag = json.load(pickle_in)
    pickle_in.close()
    word_tag = ""

    for i in range(prediction.shape[0]):
      for w, pred in zip(X_t[i], prediction[i]):
        if w != "__PAD__" and ner_idx2tag[str(pred)] != 'OTH':
            word = w
            tag = ner_idx2tag[str(pred)]
            if tag == 'B-GITHUB':
              word_tag = tag
              ner_dict[tag].append(word)
            if tag == 'B-INSTAGRAM':
              word_tag = tag
              ner_dict[tag].append(word)
            if tag == 'B-TWITTER':
              word_tag = tag
              ner_dict[tag].append(word)
            if tag == 'B-LINKEDIN':
              word_tag = tag
              ner_dict[tag].append(word)

            if tag == 'B-DESIGNATION':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-DESIGNATION':
              if word_tag == 'B-DESIGNATION':
                ner_dict['B-DESIGNATION'][-1] = ner_dict['B-DESIGNATION'][-1]+' '+word
              else:
                ner_dict['B-DESIGNATION'].append(word)

            if tag == 'B-PERSON':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-PERSON':
              if word_tag == 'B-PERSON':
                ner_dict['B-PERSON'][-1] = ner_dict['B-PERSON'][-1]+' '+word
              else:
                ner_dict['B-PERSON'].append(word)
            if tag == 'B-COMPANY-DURATION':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-COMPANY-DURATION':
              if word_tag == 'B-COMPANY-DURATION':
                ner_dict['B-COMPANY-DURATION'][-1] = ner_dict['B-COMPANY-DURATION'][-1]+' '+word
              else:
                ner_dict['B-COMPANY-DURATION'].append(word)

            if tag == 'B-COMPANY':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-COMPANY':
              if word_tag == 'B-COMPANY':
                ner_dict['B-COMPANY'][-1] = ner_dict['B-COMPANY'][-1]+' '+word
              else:
                ner_dict['B-COMPANY'].append(word)
            if tag == 'B-SKILLS':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-SKILLS':
              if word_tag == 'B-SKILLS':
                ner_dict['B-SKILLS'][-1] = ner_dict['B-SKILLS'][-1]+' '+word
              else:
                ner_dict['B-SKILLS'].append(word)
            if w.lower()!='email':
              if tag == 'B-EMAIL':
                word_tag = tag
                ner_dict[tag].append(word)

            if tag == 'B-CURR-DESIGNATION':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-CURR-DESIGNATION':
              if word_tag == 'B-CURR-DESIGNATION':
                ner_dict['B-CURR-DESIGNATION'][-1] = ner_dict['B-CURR-DESIGNATION'][-1]+' '+word
              else:
                ner_dict['B-CURR-DESIGNATION'].append(word)
            if tag == 'B-CURR-LOCATION':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-CURR-LOCATION':
              if word_tag == 'B-CURR-LOCATION':
                ner_dict['B-CURR-LOCATION'][-1] = ner_dict['B-CURR-LOCATION'][-1]+' '+word
              else:
                ner_dict['B-CURR-LOCATION'].append(word)

            if tag == 'B-COMPANY-LOCATION':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-COMPANY-LOCATION':
              if word_tag == 'B-COMPANY-LOCATION':
                ner_dict['B-COMPANY-LOCATION'][-1] = ner_dict['B-COMPANY-LOCATION'][-1]+' '+word
              else:
                ner_dict['B-COMPANY-LOCATION'].append(word)

            if tag == 'B-CURR-COMPANY':
              word_tag = tag
              ner_dict[tag].append(word)
            elif tag == 'I-CURR-COMPANY':
              if word_tag == 'B-CURR-COMPANY':
                ner_dict['B-CURR-COMPANY'][-1] = ner_dict['B-CURR-COMPANY'][-1]+' '+word
              else:
                ner_dict['B-CURR-COMPANY'].append(word)
    return ner_dict
