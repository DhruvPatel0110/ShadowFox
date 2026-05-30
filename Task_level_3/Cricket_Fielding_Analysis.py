import pandas as pd

# Read dataset
df = pd.read_csv("fielding_data.csv")

# Performance Matrix
performance_matrix = []

# Unique players
players = df["Player Name"].unique()

for player in players:

    player_data = df[df["Player Name"] == player]

    CP = 0
    GT = 0
    C = 0
    DC = 0
    ST = 0
    RO = 0
    MRO = 0
    DH = 0
    RS = 0

    for _, row in player_data.iterrows():

        pick = str(row["Pick"]).strip().upper()
        throw = str(row["Throw"]).strip().upper()

        # Pick column
        if pick == "Y":
            CP += 1

        elif pick == "C":
            C += 1

        elif pick == "DC":
            DC += 1

        # Throw column
        if throw == "Y":
            GT += 1

        elif throw == "S":
            ST += 1

        elif throw == "RO":
            RO += 1

        elif throw == "MR":
            MRO += 1

        elif throw == "DH":
            DH += 1

        # Runs
        if pd.notna(row["Runs"]):
            RS += row["Runs"]

    # Performance Score Formula
    PS = (
        (CP * 1)
        + (GT * 1)
        + (C * 3)
        - (DC * 4)
        + (ST * 3)
        + (RO * 3)
        - (MRO * 3)
        + (DH * 2)
        + RS
    )

    performance_matrix.append([
        player,
        CP,
        GT,
        C,
        DC,
        ST,
        RO,
        MRO,
        DH,
        RS,
        PS
    ])

# Create DataFrame
output_df = pd.DataFrame(
    performance_matrix,
    columns=[
        "Player Name",
        "CP",
        "GT",
        "C",
        "DC",
        "ST",
        "RO",
        "MRO",
        "DH",
        "RS",
        "Performance Score"
    ]
)

# Save Performance Matrix
output_df.to_csv("performance_matrix.csv", index=False)

print(output_df)

print("\nPerformance Matrix created successfully!")