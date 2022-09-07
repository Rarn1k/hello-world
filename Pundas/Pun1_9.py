import pandas as pd
df = pd.read_csv("https://stepik.org/media/attachments/course/4852/submissions_data_train.zip")
print(df[df.submission_status == 'correct'].groupby("user_id", as_index=False).agg({'submission_status': 'count'})
      .sort_values('submission_status', ascending=False).head())
