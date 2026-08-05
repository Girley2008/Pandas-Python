import seaborn as sns
import pandas as pd
df = sns.load_dataset("titanic")
tabela = pd.DataFrame(df)
print(tabela.info())
df = df.drop('deck', axis=1)
df_sem_null = df.fillna(df.mean(numeric_only=True))
df_sem_null = df_sem_null.dropna()  # Drop any remaining rows with NaN values
print(df_sem_null.info())