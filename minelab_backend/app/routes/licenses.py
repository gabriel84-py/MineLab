from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/verify")
def verify(ID: int, hash: str, taille: int):
    # Charger le CSV
    df_BDD = pd.read_csv('/Users/gabrieljeanvermeille/PycharmProjects/MineLab/minelab_backend/tests/simu_bdd.csv')

    # Chercher la ligne avec le bon ID
    ligne_ID = df_BDD[df_BDD["srvID"] == ID]

    # Vérifier qu'on a trouvé une ligne
    if ligne_ID.empty:
        return {"status": "error", "message": "ID non trouvé"}

    if str(ligne_ID["first"].iloc[0]) == "True":
        # Récupérer les valeurs attendues
        hash_ID = str(ligne_ID["hash"].iloc[0])
        taille_ID = int(ligne_ID["taille"].iloc[0])

        # Comparaison
        if hash_ID != hash:
            return {"status": "fail", "reason": "hash invalide"}

        if taille_ID != taille:
            return {"status": "fail", "reason": "taille invalide"}

        return {"status": "success", "message": "Vérification réussie"}
    else:
        df_BDD.loc[df_BDD['srvID'] == ID, ['hash', 'taille', 'first']] = [hash, taille, True]
        df_BDD.to_csv('/Users/gabrieljeanvermeille/PycharmProjects/MineLab/minelab_backend/tests/simu_bdd.csv', index=False)
        return {"status": "success", "message": "Vérification réussie, tout ajouté avec succès"}

