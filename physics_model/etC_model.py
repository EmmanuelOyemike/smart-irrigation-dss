from crop_coefficient import get_kc

def compute_etc(df):

    etc_values = []

    for i, row in df.iterrows():

        kc = get_kc(i)

        etc = row["ET0"] * kc

        etc_values.append(etc)

    df["ETc_maize"] = etc_values

    return df