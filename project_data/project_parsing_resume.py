from .project_dict import project_dict
import sys
import pickle
from numba import jit, cuda
@jit
def project_parsing_data(prediction, X_t):
    pickle_in = open(sys.path[0]+"/project_data/project_model/project_idx2tag.pickle","rb")
    project_idx2tag = pickle.load(pickle_in)
    pickle_in.close()
    print(project_idx2tag)
    word_tag = ""
    for i in range(prediction.shape[0]):
        for s, pred in zip(X_t[i], prediction[i]):
            if s != "__PAD__" and project_idx2tag[pred] != 'OTH':
                sentence = s
                tag = project_idx2tag[pred]
                if tag == 'B-ACHIVE':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-ACHIVE':
                  if word_tag == 'B-ACHIVE':
                    project_dict['B-ACHIVE'][-1].append(sentence)
                  else:
                    project_dict['B-ACHIVE'].append([sentence])

                if tag == 'B-AOI':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-AOI':
                  if word_tag == 'B-AOI':
                    project_dict['B-AOI'][-1].append(sentence)
                  else:
                    project_dict['B-AOI'].append([sentence])

                if tag == 'B-CAR-OBJ':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-CAR-OBJ':
                  if word_tag == 'B-CAR-OBJ':
                    project_dict['B-CAR-OBJ'][-1].append(sentence)
                  else:
                    project_dict['B-CAR-OBJ'].append([sentence])

                if tag == 'B-CERTIFICATE':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-CERTIFICATE':
                  if word_tag == 'B-CERTIFICATE':
                    project_dict['B-CERTIFICATE'][-1].append(sentence)
                  else:
                    project_dict['B-CERTIFICATE'].append([sentence])

                if tag == 'B-COLLEGE':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-COLLEGE':
                  if word_tag == 'B-COLLEGE':
                    project_dict['B-COLLEGE'][-1].append(sentence)
                  else:
                    project_dict['B-COLLEGE'].append([sentence])

                if tag == 'B-DEGREE':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-DEGREE':
                  if word_tag == 'B-DEGREE':
                    project_dict['B-DEGREE'][-1].append(sentence)
                  else:
                    project_dict['B-DEGREE'].append([sentence])

                if tag == 'B-EDUCATION':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-EDUCATION':
                  if word_tag == 'B-EDUCATION':
                    project_dict['B-EDUCATION'][-1].append(sentence)
                  else:
                    project_dict['B-EDUCATION'].append([sentence])

                if tag == 'B-EXP':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-EXP':
                  if word_tag == 'B-EXP':
                    project_dict['B-EXP'][-1].append(sentence)
                  else:
                    project_dict['B-EXP'].append([sentence])

                if tag == 'B-GRADUATION-END-YEAR':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-GRADUATION-END-YEAR':
                  if word_tag == 'B-GRADUATION-END-YEAR':
                    project_dict['B-GRADUATION-END-YEAR'][-1].append(sentence)
                  else:
                    project_dict['B-GRADUATION-END-YEAR'].append([sentence])

                if tag == 'B-H-SCHOOL':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-H-SCHOOL':
                  if word_tag == 'B-H-SCHOOL':
                    project_dict['B-H-SCHOOL'][-1].append(sentence)
                  else:
                    project_dict['B-H-SCHOOL'].append([sentence])

                if tag == 'B-H-SCHOOL-GRADUATION-END-YEAR':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-H-SCHOOL-GRADUATION-END-YEAR':
                  if word_tag == 'B-H-SCHOOL-GRADUATION-END-YEAR':
                    project_dict['B-H-SCHOOL-GRADUATION-END-YEAR'][-1].append(sentence)
                  else:
                    project_dict['B-H-SCHOOL-GRADUATION-END-YEAR'].append([sentence])

                if tag == 'B-HSS-SCHOOL':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-HSS-SCHOOL':
                  if word_tag == 'B-HSS-SCHOOL':
                    project_dict['B-HSS-SCHOOL'][-1].append(sentence)
                  else:
                    project_dict['B-HSS-SCHOOL'].append([sentence])

                if tag == 'B-HSS-SCHOOL-GRADUATION-END-YEAR':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-HSS-SCHOOL-GRADUATION-END-YEAR':
                  if word_tag == 'B-HSS-SCHOOL-GRADUATION-END-YEAR':
                    project_dict['B-HSS-SCHOOL-GRADUATION-END-YEAR'][-1].append(sentence)
                  else:
                    project_dict['B-HSS-SCHOOL-GRADUATION-END-YEAR'].append([sentence])

                if tag == 'B-OTHER-SKILL':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-OTHER-SKILL':
                  if word_tag == 'B-OTHER-SKILL':
                    project_dict['B-OTHER-SKILL'][-1].append(sentence)
                  else:
                    project_dict['B-OTHER-SKILL'].append([sentence])

                if tag == 'B-PROJECT-EXP':
                    word_tag = tag
                    project_dict[tag].append([sentence])
                elif tag == 'I-PROJECT-EXP':
                  if word_tag == 'B-PROJECT-EXP':
                    project_dict['B-PROJECT-EXP'][-1].append(sentence)
                  else:
                    project_dict['B-PROJECT-EXP'].append([sentence])
    return project_dict
