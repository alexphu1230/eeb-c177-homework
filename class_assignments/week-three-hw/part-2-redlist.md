Number of Occurences of Species Codes:

Command: cut -d "," -f 10 European_Red_List.csv | sort | uniq -c | sort -n
 4 EW
      4 NE
      8 CR (PE)
      8 RE
     29 EX
    411 NA
    456 CR
    687 EN
    885 VU
    964 NT
   2409 DD
   5805 LC

Number of Occruences of Species Codes of only Birds:

Command: grep Birds European_Red_List.csv | cut -d "," -f 10 | sort | uniq -c | sort -n

 2 EX
      4 RE
     10 CR
     18 EN
     32 NT
     39 VU
    428 LC

Birds that are Extinct/Near Extinct:
 
Command: grep -w AVES  European_Red_List.csv | cut -d "," -f 10 | sort | uniq -c | grep -w RE |  sort -n
4 RE 

Command: grep -w AVES  European_Red_List.csv | cut -d "," -f 10 | sort | uniq -c | grep -w CR |  sort -n
10 CR 

Command: grep -w AVES  European_Red_List.csv | cut -d "," -f 10 | sort | uniq -c | grep -w EX |  sort -n
2 EX
