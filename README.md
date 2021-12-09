# QFTools
Python lib to automate basic QFT calculations like Wick-contractions.
## Features
- [x] Wick contractions for real scalar fields
- [ ] Wick contractions for complex scalar fields
- [ ] Distingish between vacuum and non-vacuum contractions
## Setup
QFTools is programmed based on phyton3. You can either download the above listed files or you simply clone this repository by
```bash
git clone https://github.com/Bra-A-Ket/QFTools.git
```
Furthermore, make sure that all required packages are installed on your machine.
### External / Required Packages
- Itertools is needed to compute all possible combinations of numbers (Wick contractions)
```bash
python3 -m pip install itertools
```
## Usage / List of Commands
### Basic Usage
QFTools takes simple opt-inputs. To see the version simple execute via console
```bash
python3 qftools.py -v
```
The help menu is available via
```bash
python3 qftools.py -h
```
### Check current verion
```bash
python3 qftools.py -v
```
or
```bash
python3 qftools.py -version
```
### Help menu
```bash
python3 qftools.py -h
```
or
```bash
python3 qftools.py -help
```
#### Wick contractions
```bash
python3 qftools -w <type> <mode> <output> <fields>
```
or
```bash
python3 qftools --wick <type> <mode> <output> <fields>
```
where the parameters are:\
<ins>type</ins> : rsf (for real scalar field), csf (for complex scalar field)\
<ins>mode</ins> : all (list all possible contractions), vac (only vacuum-like contractions), nvac (only non-vacuum-like contractions)\
<ins>output</ins> : print (print contractions on console), save (save contractions in csv-file)
<ins>fields</ins> : numbered fields, such that the number symolizes the argument of the field, e.g. 1 2 3 3 (note the spacing)
### Examples
If you want to calculate <0|Tphi(x_1)phi(x_2)phi(x_3)phi(x_3)|0> for a real scalar field phi including all contractions, simply use
```bash
python3 qftools.py --wick rsf all print 1 2 3 3
```
The result is printed on the console due to the parameter 'print'. Note that |0> is the free vacuum.\
Output:
```bash
<0|T['1', '2', '3', '3']|0> =

2 x [['1', '3'], ['2', '3']] +
1 x [['1', '2'], ['3', '3']]
process finished in 0.07 ms
```
This should be read as: <0|T['1', '2', '3', '3']|0> = 2 x <0|Tphi(x_1)phi(x_3)><0|Tphi(x_2)phi(x_3)|0> + 1 x <0|Tphi(x_1)phi(x_2)|0><0|Tphi(x_3)phi(x_3)|0>
## Update Notes
### Version 1.1.1
Wick contraction for real scalar field now counts repeated contractions and prints the according multiple.
### Version 1.1
Updated README.md. Included output parameter for Wick contractions.
### Version 1.0
Initial upload of the programm. Only the basic file-structure and logic for real scalar field Wick contractions is implemented.
