import pandas as pd

submissions = pd.read_csv('https://stepik.org/media/attachments/course/4852/submissions_data_train.zip')
only_wrong = submissions[submissions['submission_status'] == 'wrong']
print(only_wrong.step_id.value_counts().head(1))
