# E-payment
**Automatisation des tests fonctionnels d'une application WEB (E-payment)**

## Les prérequis&Etapes:
**Il vous faut un IDE ou un terminal pour commencer et lancer le programme**
1- Creer un dossier ,placez vous dans le dossier
2- Telecharger python ,veuillez Consulter le lien suivant **"https://www.python.org/downloads/"**
3- Telecharger selenium compatible avec python avec la commande **"pip install selenium"** sur votre terminal,veuillez Consulter le lien suivant **"https://pypi.org/project/selenium/"**
4- Telecharger le driver de google chrome et le placer dans le dossier  => "chromedriver" avec une version compatible à celle de votre navigateur chrome,veuillez Consulter le lien suivant "https://chromedriver.chromium.org/"
5- Telecharger **"pytest"** le framework de python ,qui est responsable de l'organisation des tests et la generation du rapport des tests lancés, avec la commande "pip install pytest" sur votre terminal
## Lancer les tests:
**-Pour lancer le script(ttes les fonctions de tests) =>"pytest nom_fichier.py"  ,exemple:"pytest tst_decon.py"**  
## Generer des rapports:
**-Pour generer un rapport faut installer et ecrire sur le terminal  :**
**-"pip install pytest-html"** => **pour un rapport HTML**  ,  RUN : **"pytest test_decon.py --html=rapport_epayment.html"**
**-"pip install pytest-reportlog"**  => **pour un rapport txt**   ,  RUN : **"pytest test_decon.py --report-log=rapport_epayment.txt"** 
**-"pip install WeasyPrint"**  => **pour convertir un rapport txt en PDF**  ,  RUN : **"weasyprint rapport_epayment.txt rapport_epayment.pdf"**
