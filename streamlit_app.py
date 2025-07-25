
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Tytuł dashboardu
st.title("📈 Wykrywacz Spekulacji Detalicznej")

# Wprowadzenie danych wejściowych
st.sidebar.header("Parametry rynkowe")
vol_zscore = st.sidebar.slider("Z-score wolumenu", -3.0, 3.0, 0.0)
buzz_score = st.sidebar.slider("Buzz społecznościowy", -3.0, 3.0, 0.0)
gamma_exposure = st.sidebar.slider("Ekspozycja gamma", -3.0, 3.0, 0.0)
retail_buy_ratio = st.sidebar.slider("Stosunek zakupów detalicznych", 0.4, 1.5, 1.0)
momentum_3d = st.sidebar.slider("Momentum 3-dniowe", -3.0, 3.0, 0.0)
price_return = st.sidebar.slider("Zwrot z ceny (dzienny)", -3.0, 3.0, 0.0)

# Załaduj model
@st.cache_resource
def load_model():
    return joblib.load("model_pipeline.pkl")

model = load_model()

# Przetwarzanie danych wejściowych
X_input = pd.DataFrame([{
    "vol_zscore": vol_zscore,
    "buzz_score": buzz_score,
    "gamma_exposure": gamma_exposure,
    "retail_buy_ratio": retail_buy_ratio,
    "momentum_3d": momentum_3d,
    "price_return": price_return
}])

# Predykcja
prediction = model.predict(X_input)[0]
proba = model.predict_proba(X_input)[0][1]

# Wyświetlanie wyników
st.subheader("📊 Wynik predykcji")
if prediction == 1:
    st.error(f"⚠️ Detekcja spekulacyjna: Prawdopodobieństwo = {proba:.2%}")
else:
    st.success(f"✅ Brak sygnałów spekulacji: Prawdopodobieństwo = {proba:.2%}")

# Wyświetl dane wejściowe
st.write("Dane wejściowe:")
st.dataframe(X_input)
