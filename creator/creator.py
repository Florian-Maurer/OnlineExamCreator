import random


def create_exams(number_of_exams, excel_dict):
    exam_list = []

    for i in range(0, number_of_exams):
        turn_df_to_dict(excel_dict['General Information'])
        exam = {'General Information': turn_df_to_dict(excel_dict['General Information'])}
        index = 1
        for full_task in list(excel_dict.values())[1:]:
            exam['Task ' + str(index)] = get_random_task_version(full_task)
            index = index + 1

        exam_list.append(exam)
    return exam_list


def get_random_task_version(task):
    short_task = {'Titel': task.iloc[0][0], 'Points': task.loc[0]['Points'],
                  'Text': random.choice(list(task['Versions']))}

    return short_task


def turn_df_to_dict(df):
    dictio = {}
    for key in df.keys():
        dictio[key] = df.loc[0][key]
    return dictio
