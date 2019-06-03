import pandas as pd
signups = pd.read_excel("signups.xlsx", sheet_name = "Sheet1")

print("\nMESA Machine Signups: ")
print(signups.loc[signups.Machine == 1].Name.to_string(index = False))

print("\nGlider Signups:")
print(signups.loc[signups.Glider == 1].Name.to_string(index=False))

print("\nTank Signups:")
print(signups.loc[signups.Tank == 1].Name.to_string(index=False))

print("\nBridge Signups:")
print(signups.loc[signups.Bridge == 1].Name.to_string(index=False))

print("\nArm Signups:")
print(signups.loc[signups.Arm == 1].Name.to_string(index=False))
