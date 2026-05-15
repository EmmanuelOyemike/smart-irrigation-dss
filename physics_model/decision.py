def irrigation_decision(df):

    decisions = []

    for _, row in df.iterrows():

        soil_water = row["soil_water"]

        needed = 100 - soil_water

        if soil_water < 40:

            action = f"Irrigate {needed:.1f} mm"

        else:

            action = "Wait"

        decisions.append(action)

    df["decision"] = decisions

    return df