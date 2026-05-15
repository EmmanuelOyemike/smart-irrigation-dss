import numpy as np

def compute_et0(df):

    gamma = 0.665e-3 * 101.3

    et0_list = []

    for _, row in df.iterrows():
        T = row["temp"]
        RH = row["humidity"]
        u2 = row["wind"]
        Rs = row["radiation"]

        # Saturation vapor pressure
        es = 0.6108 * np.exp((17.27 * T) / (T + 237.3))

        # Actual vapor pressure
        ea = es * (RH / 100)

        # Slope of vapor pressure curve
        delta = (4098 * es) / ((T + 237.3) ** 2)

        # Net radiation (simplified)
        Rn = 0.77 * Rs

        G = 0  # daily assumption

        et0 = (
            (0.408 * delta * (Rn - G)) +
            (gamma * (900 / (T + 273)) * u2 * (es - ea))
        ) / (delta + gamma * (1 + 0.34 * u2))

        et0_list.append(et0)

    df["ET0"] = et0_list
    return df