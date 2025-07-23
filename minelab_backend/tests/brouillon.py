import pandas as pd

def verify(ID: int, hash: str, taille: int):
    df_BDD = pd.read_csv('/Users/gabrieljeanvermeille/PycharmProjects/MineLab/minelab_backend/tests/simu_bdd.csv')
    ligne_ID = df_BDD[df_BDD["srvID"] == ID]
    hash_ID = str(ligne_ID["hash"].values[0])
    taille_ID = int(ligne_ID["taille"].values[0])
    if hash_ID != hash:
        return False
    if taille_ID != taille:
        return False
    return True

print(verify(1234, "0", 0))