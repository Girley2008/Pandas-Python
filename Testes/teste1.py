import seaborn as sns
import pandas as pd
df = sns.load_dataset("titanic")
tabela = pd.DataFrame(df)
print(tabela.info())