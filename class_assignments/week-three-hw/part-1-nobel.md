Number of Nobel Prize winners by category 

1. Chemistry: 181
   Command: cut -d "," -f 3 nobel.csv | grep -w chemistry | wc -l
2. Economics: 81
   Command: cut -d "," -f 3 nobel.csv | grep -w economics | wc -l
3. Literature: 114
   Command: cut -d "," -f 3 nobel.csv | grep -w literature | wc -l
4. Medicine: 216
   Command: cut -d "," -f 3 nobel.csv | grep -w medicine | wc -l
5. Peace: 133
   Command: cut -d "," -f 3 nobel.csv | grep -w peace | wc -l
6. Physics: 210
   Command: cut -d "," -f 3 nobel.csv | grep -w physics | wc -l

Winners of Multiple Nobel Prizes: 
Command: cut -d "," -f 4-6  nobel.csv | sort | uniq -c | sort -n
 2 217,"Linus Carl","Pauling"
 2 222,"Frederick","Sanger"
 2 515,"Office of the United Nations High Commissioner for Refugees (UNHCR)",NA
 2 66,"John","Bardeen"
 2 6,"Marie","Curie
 3 482,"Comité international de la Croix Rouge (International Committee of the Red Cross)",NA
 

Most common surnames (appears more than once): 
Command: cut -d "," -f 6 nobel.csv | sort | uniq -c | sort -n
 2 "Anderson"
 2 "Bardeen"
 2 "Bloch"
 2 "Bohr"
 2 "Bragg"
 2 "Brown"
 2 "Buck"
 2 "Chamberlain"
 2 "Curie
 2 "Frank"
 2 "Friedman"
 2 "Hall"
 2 "Henderson"
 2 "Hess"
 2 "Hodgkin"
 2 "Hoffmann"
 2 "Jensen"
 2 "Kendall"
 2 "Kornberg"
 2 "Krebs"
 2 "Marshall"
 2 "Mistral"
 2 "Moser"
 2 "Mott"
 2 "Murad"
 2 "Myrdal"
 2 "Pauling"
 2 "Porter"
 2 "Richards"
 2 "Richardson"
 2 "Sanger"
 2 "Siegbahn"
 2 "Simon"
 2 "Thomson"
 2 "Tinbergen"
 2 "Wiesel"
 2 "Williams"
 3 "Lee"
 3 "Lewis"
 3 "Müller"
 4 "Fischer"
 4 "Wilson"
 5 "Smith"
 31 NA

Years that Awarded most nobel prizes: 2001 (15 prizes) 
Years that Awarded least nobel prizes:1916 (1 Prize) 
Command: cut -d "," -f 2 nobel.csv | sort | uniq -c | sort -n

