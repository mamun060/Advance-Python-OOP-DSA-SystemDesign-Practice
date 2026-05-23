import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

print("১. ডেটা লোড এবং ক্লিন করা হচ্ছে...")
# আপনার লোকাল ফোল্ডারে 'Scores (1).csv' ফাইলটি রেখে এই কোড রান করুন
df = pd.read_csv("Scores.csv", sep=';')

# কমা সরিয়ে ডট করা এবং ফ্লোট-এ রূপান্তর
df['score'] = df['score'].astype(str).str.replace(',', '.')
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# লং ফরম্যাট থেকে ওয়াইড ফরম্যাটে রূপান্তর (অ্যানালাইসিসের সুবিধার জন্য)
df_wide = df.pivot(index=['student_id', 'gender', 'parental.level.of.education'], 
                   columns='subject', 
                   values='score').reset_index()

print("--- ডেটা ক্লিনিং ও রিসেপ সফল হয়েছে! ---")

print("\n২. ডেসক্রিপティブ গ্রাফ (Boxplot) জেনারেট করা হচ্ছে...")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# জেন্ডার ভিত্তিক বক্সপ্লট
sns.boxplot(data=df, x='subject', y='score', hue='gender', ax=axes[0], palette='Set2')
axes[0].set_title('Distribution of Scores by Gender', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Subject', fontsize=12)
axes[0].set_ylabel('Scores (0-100)', fontsize=12)

# বাবা-மায়ের শিক্ষা ভিত্তিক বক্সপ্লট
edu_order = ['high school', "associate's degree", "bachelor's degree", "master's degree"]
sns.boxplot(data=df, x='parental.level.of.education', y='score', hue='subject', 
            order=edu_order, ax=axes[1], palette='Pastel1')
axes[1].set_title('Distribution of Scores by Parental Education', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Parental Level of Education', fontsize=12)
axes[1].set_ylabel('Scores (0-100)', fontsize=12)
axes[1].axes.set_xticklabels(edu_order, rotation=15)

plt.tight_layout()
plt.savefig('student_scores_boxplot.png', dpi=300)
print("--- গ্রাফটি 'student_scores_boxplot.png' নামে সেভ হয়েছে! ---")

print("\n৩. জেন্ডার ভিত্তিক হাইপোথিসিস টেস্ট (Two-Sample t-test) রান করা হচ্ছে...")
male_math = df_wide[df_wide['gender'] == 'male']['math']
female_math = df_wide[df_wide['gender'] == 'female']['math']
t_stat_m, p_val_m = stats.ttest_ind(male_math, female_math, equal_var=False)
print(f">> Math Score -> t-statistic: {t_stat_m:.4f}, p-value: {p_val_m:.4e}")

male_lang = df_wide[df_wide['gender'] == 'male']['language']
female_lang = df_wide[df_wide['gender'] == 'female']['language']
t_stat_l, p_val_l = stats.ttest_ind(male_lang, female_lang, equal_var=False)
print(f">> Language Score -> t-statistic: {t_stat_l:.4f}, p-value: {p_val_l:.4e}")

print("\n৪. বাবা-মায়ের শিক্ষা ভিত্তিক হাইপোথিসিস Test (ANOVA) রান করা হচ্ছে...")
model_math = ols('math ~ Q("parental.level.of.education")', data=df_wide).fit()
anova_math = sm.stats.anova_lm(model_math, typ=2)
print("\n--- Math Score ANOVA Table ---")
print(anova_math)

model_lang = ols('language ~ Q("parental.level.of.education")', data=df_wide).fit()
anova_lang = sm.stats.anova_lm(model_lang, typ=2)
print("\n--- Language Score ANOVA Table ---")
print(anova_lang)