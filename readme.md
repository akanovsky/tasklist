1 Aplikace Tasklist
 - aplikace slouží k evidenci úkolů v samostatně vytvořených seznamech pro jednotlivé uživatele

2 Instalace
- před spuštěním je třeba stáhnout extra moduly, které program pro běh využívá
 
`pip install django`

` pip install django-crispy-forms`

Dále je potřeba zpropagovat modely do databázového schématu příkazem

`python manage.py migrate`

- Spuštění aplikace následně 

`python manage.py runserver`

3 Použití aplikace
  
- Zalogování existujícího uživatele - Log in
- Zaregistrování nového uživatele - Sign in
- Odhlášení z aplikace - Log out

Po zalogování uživatele
- vytvoření nového seznamu úkolů - New list
- přehled vytvořených seznamů úkolů - List

Práce v seznamu úkolů
- přidat nový úkol - Add task
- uložit stav úkolů - Save
- splnění/nesplnění úkolu lze zaznamenat zaškrtnutím u daného úkolu a následným uložením stavu
  

