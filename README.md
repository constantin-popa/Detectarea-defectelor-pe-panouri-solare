# Proiect-PI
# ☀️ Solar Panel Defect Detection: A Computer Vision & Deep Learning Approach

**Panourile solare** sunt menite sa aiba o durata de viata de pana la 30 de ani, insa anumite defecte si probleme de performanta pot aparea cu mult inainte de acest termen. [ 2025 Global Solar Report by Raptor Maps](https://raptormaps.com/resources/global-solar-report-2025), un studiu realizat in 2025, atesta ca lipsa de performanta cauzata de echipamente a crescut cu peste 200% din 2019, estimand o pierdere de peste 10 miliarde de dolari in energie doar in anul 2024.

Inspectia manuala a panourilor solare este inceata, scumpa si predispusa la erori. Pentru un parc solar de 100 MW, verificarea poate dura luni, iar primele panouri verificate se pot degrada pana cand cele din urma ajung sa fie testate. 

Acest proiect exploreaza automatizarea detectarii defectelor pe panourile solare, imbinand tehnici clasice de procesare a imaginilor cu retele neuronale convolutionale (CNN). Obiectivul principal este de a demonstra si cuantifica impactul unui pipeline riguros de preprocesare asupra performantei modelelor de Machine Learning.

Pentru a valida eficienta tehnicilor de *Computer Vision*, proiectul antreneaza si compara doua arhitecturi in paralel:
*   **Baseline:** Un model antrenat exclusiv pe imaginile brute (raw data).
*   **Enhanced:** Un model antrenat pe imagini trecute printr-un pipeline de preprocesare si extragere ROI (filtrare zgomot, ajustare contrast prin CLAHE, detectare margini si corectii de perspectiva).


# **SCHEMA BLOC**
![Schema bloc](/Imagini/schema_bloc_PIP.png)

1. **Achizitia de date**
    - Colectarea setului initial de imagini cu panouri solare.

    - O copie a imaginilor sare peste etapa de preprocesare, pentru a realiza o comparatie de performanta

2. **Preprocesare**
    - Se aplica algoritmi pentru imbunatatirea calitatii vizuale

3. **Extragere Region of Interest**
    - Se elimina datele inutile din fundal, se indreapta imaginea si se distinge conturul panourilor

    - Dupa aceste prelucrari, se realizeaza un cropping precis pe suprafata panourilor

4. **Pregatirea datelor**

    - Se modifica imaginile la o dimensiune standard pentru modelul de Machine Learning
    
    - Rotirile si Flip-urile au rol de a multiplica artificial setul de date pentru a oferi mai multe exemple

5. **Split data**

    - Se impart imaginile in 2 categorii
        - De training, in proportie de 70-80 %
        - De test, in proprotie de 20-30 %

6. **Reteaua Neuronala Convolutionala**

    - Nucleul proiectului
    - Proceseaza datele de training pentru a invata tipare

7. **Postprocesare**

    - Deciziile retelei sunt transformate in rezultate vizuale usor de inteles
    - Se traseaza Bounding Boxes si se aplica masti  care sa identifice defectele 

8. **Extragere concluzii**

    - Se determina metricii de performanta si se analizeaza diferentele intre cele 2 modele, evidentiand necesitatea si eficienta tehnicilor de Prelucrare de Imagini

## Bibliografie

1. Greenlancer - [*Solar Panel Damage & Defects: Signs, Causes & What to Do*](https://www.greenlancer.com/post/common-solar-panel-defects) 
2. Raptor Maps - [ 2025 Global Solar Report by Raptor Maps](https://raptormaps.com/resources/global-solar-report-2025)
3. Datature - [Why Solar Inspection Needs Automation](https://datature.io/blog/solar-panel-defect-detection-with-vision-ai-from-drone-thermography-to-deployed-models)

4. [draw.io](https://www.drawio.com/)

5. [Google Gemini](https://gemini.google.com/app)
