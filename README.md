# xAPI Extended (Second Stage)

Šiame projekte pateikiama išplėstinė xAPI integracijos versija, kurioje fiksuojami ne tik naudotojo atsakymai, bet ir papildoma informacija apie mokymosi eigą: skaidrių peržiūra, užuominos (hint) naudojimas, konteksto veikla, trukmė ir platformos informacija.

## Kas tai?

Tai antrojo etapo xAPI integracija, kuri išplečia bazinį SCORM atitikmenį pridėdama šiuos funkcionalumus:

- Skaidrių peržiūros sekimas (`experienced`)
- Atsakymų laiko trukmė (`duration`)
- Pagalbos naudojimo registracija (`used`)
- Naudotojo platformos (OS/naršyklė) fiksavimas
- Konteksto veiklos nurodymas (`parent`)

## Failų struktūra

- `assessmenttemplate.html` – testavimo failas su klausimais ir hint’ais
- `questions.js` – klausimų aprašai su galimais atsakymais ir `hint` lauku
- `xapi-slide.js` – skaidrių peržiūros fiksavimo modulis su `experienced` ir `duration`

## Kofiguracija

  ```JS
  const tincan = new TinCan({
    recordStores: [
      {
        endpoint: "https://xapi-quiz.lrs.io/xapi/",
        username: "JŪSŲ_LRS_RAKTAS",
        password: "JŪSŲ_SLAPTAŽODIS",
        allowFail: false
      }
    ]  
  });
  ```

## Paleidimas

1. Nuklonuokite šią repozitoriją ir persijunkite į šaką:

   ```bash
   git clone https://github.com/Ne-Ga-TIV/BD2025.git
   cd BD2025/xAPIExtended

2. Paleisketi Playing.html per savo internet naršykle
