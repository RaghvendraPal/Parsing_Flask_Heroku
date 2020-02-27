
def update_dict(data_dict):
    if len(data_dict['B-CURR-COMPANY']) > 0:
        data_dict['B-CURR-COMPANY'] = data_dict['B-CURR-COMPANY'][0]
    if len(data_dict['B-CURR-DESIGNATION']) > 0:
        data_dict['B-CURR-DESIGNATION'] = data_dict['B-CURR-DESIGNATION'][0]
    if len(data_dict['B-CURR-LOCATION']) > 0:
        data_dict['B-CURR-LOCATION'] = data_dict['B-CURR-LOCATION'][0]
    if len(data_dict['B-EMAIL']) > 0:
        data_dict['B-EMAIL'] = data_dict['B-EMAIL'][0]
    if len(data_dict['B-PERSON']) > 0:
        data_dict['B-PERSON'] = data_dict['B-PERSON'][0]
    if len(data_dict['B-LINKEDIN']) > 0:
        data_dict['B-LINKEDIN'] = data_dict['B-LINKEDIN'][0]
    if len(data_dict['B-INSTAGRAM']) > 0:
        data_dict['B-INSTAGRAM'] = data_dict['B-INSTAGRAM'][0]
    if len(data_dict['B-GITHUB']) > 0:
        data_dict['B-GITHUB'] = data_dict['B-GITHUB'][0]
    if len(data_dict['B-SKILLS']) > 0:
        data_dict['B-SKILLS'] = data_dict['B-SKILLS'][0:10]
    return data_dict
