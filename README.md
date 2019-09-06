# TOX_HL
 It is a simple method for the determination of half-lives of drugs based on survival outcomes alone.
 
TOXHL involves 3 experiments: an acute toxicity experiment, a cumulative toxicity experiment, and a multi-dose experimentat different dosing intervals. Data obtained from these 3 experiment has been demonstrated to be sufficient to calculate the peritoneal half-life of the antimicrobial peptide, Ω76.

survival_file #File which contains data on Survival vs conc

crit_died #Number of mice which died during time-spaced experiment

crit_total  #Total number of mice which were used during time-spaced experiment

conc_point  #Fraction of mice which died during time-spaced experiment

time_period  #Time period of dosage

conc_dosage  #Concentration of dosage

N_points #Number of dosages administered before witnessing first death

Usage: python dosage.py <file_name> <number_died> <total_number> <time_period> <dosage_conc> <dosage_points>

Please input the following for an example run -

Survival file is given as acute_toxicity.csv
Number of mice which died during multi-dose experiment = 2
Total number of mice which were used during multi-dose experiment = 6
Time period of dosage = 3
Concentration of dosage = 64
Number of dosages administered before witnessing first death = 5

Copyright (c) <2019> <Preetham Venkatesh>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
