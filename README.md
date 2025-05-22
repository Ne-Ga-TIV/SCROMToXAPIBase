# SCORM to xAPI (Base Version)

Šis projektas pateikia SCORM 1.2 kurso konvertavimo į xAPI veikimo pavyzdį. Vietoj SCORM LMS integracijos naudotojo veiksmai fiksuojami naudojant xAPI pareiškimus ir siunčiami į Learning Record Store (LRS).

## Kas tai?

Tai bazinė xAPI integracija, kuri atkuria SCORM kurso testavimo scenarijų naršyklėje:

- Fiksuojami `answered` tipo xAPI teiginiai
- Veikia be LMS
- Tinka kaip mokomasis pavyzdys arba xAPI įvadui

## Failų struktūra

- `assessmenttemplate.html` – pagrindinis testavimo šablonas su integruotu `tincan.js`
- `questions.js` – klausimų rinkinys (JavaScript masyvas)

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

1. Atsisiųskite arba nuklonuokite repozitoriją:

   ```bash
   https://github.com/Ne-Ga-TIV/BD2025.git
   cd ВD2025/xAPIBase

2. Paleisketi Playing.html per savo internet naršykle
