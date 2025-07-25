# Wykrywacz Spekulacji Detalicznej (Streamlit App)

Aplikacja stworzona do detekcji zachowań spekulacyjnych na rynku akcji, bazująca na wskaźnikach takich jak buzz społecznościowy, wolumen, momentum i ekspozycja gamma.

## Uruchomienie lokalne

1. Zainstaluj zależności:
```
pip install -r requirements.txt
```

2. Uruchom aplikację Streamlit:
```
streamlit run streamlit_app.py
```

## Hosting

Możesz wystawić aplikację w chmurze:
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Hugging Face Spaces](https://huggingface.co/spaces)

Pliki potrzebne do wdrożenia:
- streamlit_app.py
- model_pipeline.pkl
- requirements.txt