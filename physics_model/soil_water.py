def compute_soil_water(df, crop="maize", field_capacity=100):

    soil = field_capacity  # starting soil moisture
    soil_list = []

    for _, row in df.iterrows():
        rainfall = row["rainfall"]
        etc = row[f"ETc_{crop}"]

        soil = soil + rainfall - etc

        # Clamp values (important)
        soil = max(0, min(soil, field_capacity))

        soil_list.append(soil)

    df["soil_water"] = soil_list
    return df