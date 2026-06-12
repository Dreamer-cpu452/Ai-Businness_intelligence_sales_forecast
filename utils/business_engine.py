def business_score(df):

    score = 100

    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    score -= missing_values * 2
    score -= duplicate_rows * 3

    if score < 0:
        score = 0

    return score