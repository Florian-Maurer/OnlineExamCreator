import random


def create_exams(number_of_exams, excel_dict):
    exam_list = []

    for i in range(0, number_of_exams):
        exam = {'General Information': excel_dict['General Information']}
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
