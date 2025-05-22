# xAPIEngine

Paprastas žaidimų variklis sukurtas su `pygame`, integruotas su [xAPI (Experience API)](https://xapi.com/) žaidėjų veikloms sekti. Sukurtas mokymosi veikloms registruoti naudojant LRS (Learning Record Store), pavyzdžiui, [Veracity LRS](https://veracity.fpg.unc.edu/).

## 🔧 Funkcionalumas

- Pagrindinis 2D žaidimų variklis su Python ir pygame
- Žaidėjo veiksmų sekimas (judėjimas, sąveika, objektų kūrimas)
- xAPI palaikymas (veiksmų registravimas į LRS)
- Automatinis xAPI pranešimų siuntimas

### Projekto struktūra

```plaintext
xAPIEngine/
├── main.py              # Pagrindinis paleidimo failas
├── engine.py            # Žaidimo variklio klasė (Engine) su xAPI integracija
├── game_objects.py      # Reikiamų žiadimo objektų klasių aprašymas
  ```

## Paleigimas

1. Nusiklonuokite repozitoriją:

```bash
git clone https://github.com/Ne-Ga-TIV/BD2025.git
cd BD2025/xAPIEngine
```

2. Įdiekite reikalingas bibliotekas
```python
pip install pygame requests
```

3. Paleiskite žaidimą
```python
python main.py

```

