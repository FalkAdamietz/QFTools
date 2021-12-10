# QFTools
Python lib to automate basic QFT calculations like Wick-contractions.
## Features
- [x] Wick contractions for real scalar fields
- [x] Print result of Wick contraction on console
- [x] Save result of Wick contraction in a csv-file
- [x] Generate LaTeX-file of the Wick contractions
- [ ] Wick contractions for complex scalar fields
- [ ] Distingish between vacuum and non-vacuum contractions
## Setup
QFTools is programmed based on phyton3. You can either download the above listed files or you simply clone this repository by
```console
git clone https://github.com/Bra-A-Ket/QFTools.git
```
Furthermore, make sure that all required packages are installed on your machine.
### External / Required Packages
- Itertools is needed to compute all possible combinations of numbers (Wick contractions)
```console
python3 -m pip install itertools
```
- Numpy for standard array-like calculations
```console
python3 -m pip install numpy
```
## Usage / List of Commands
### Basic Usage
QFTools takes simple opt-inputs. To see the version simple execute via console
```console
python3 qftools.py -v
```
The help menu is available via
```console
python3 qftools.py -h
```
### Check current verion
```console
python3 qftools.py -v
```
or
```console
python3 qftools.py -version
```
### Help menu
```console
python3 qftools.py -h
```
or
```console
python3 qftools.py -help
```
#### Wick contractions
```console
python3 qftools -w <type> <mode> <output> <fields>
```
or
```console
python3 qftools --wick <type> <mode> <output> <fields>
```
where the parameters are:\
<ins>type</ins> : rsf (for real scalar field), csf (for complex scalar field)\
<ins>mode</ins> : all (list all possible contractions), vac (only vacuum-like contractions), nvac (only non-vacuum-like contractions)\
<ins>output</ins> : print (print contractions on console), csv (save contractions in csv-file), latex (generate LaTeX-file)\
<ins>fields</ins> : numbered fields, such that the number symolizes the argument of the field, e.g. 1 2 3 3 (note the spacing)
### Examples
#### Print-Mode
If you want to calculate <0|T phi(x_1) phi(x_2) phi(x_3) phi(x_3)|0> for a real scalar field phi including all contractions, simply use
```console
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
This should be read as: <0|T hi(x_1) phi(x_2) phi(x_3) phi(x_3)|0> = 2 x <0|T phi(x_1) phi(x_3)><0|T phi(x_2) phi(x_3)|0> + 1 x <0|T phi(x_1) phi(x_2)|0><0|T phi(x_3) phi(x_3)|0>
#### CSV-Mode
If you want to calculate <0|T phi(x_1) phi(x_2) phi(x_3) phi(x_3)|0> for a real scalar field phi including all contractions, simply use
```console
python3 qftools.py --wick rsf all csv 1 2 3 3
```
This will create a new csv-file, which, in this case, looks like
```bash
4-point function:,"['1', '2', '3', '3']"
multiplier,contractions to two-point propagators
1,"[['1', '2'], ['3', '3']]"
2,"[['1', '3'], ['2', '3']]"
```
Note, that delimiter="," and that the first column is the combinatorial factor.
#### LaTeX-Mode
If you want to calculate <0|T phi(x_1) phi(x_2) phi(x_3) phi(x_3)|0> for a real scalar field phi including all contractions, simply use
```console
python3 qftools.py --wick rsf all latex 1 2 3 3
```
This will create a new tex-file, which, in this case, looks like
```latex
\begin{align}
\langle 0\vert\mathcal{T}\hat{\phi}(x_{1})\hat{\phi}(x_{2})\hat{\phi}(x_{3})\hat{\phi}(x_{3})\vert 0\rangle
&=1\cdot\langle 0\vert\mathcal{T}\hat{\phi}(x_{1})\hat{\phi}(x_{2})\vert 0\rangle\langle 0\vert\mathcal{T}\hat{\phi}(x_{3})\hat{\phi}(x_{3})\vert 0\rangle\\
&=2\cdot\langle 0\vert\mathcal{T}\hat{\phi}(x_{1})\hat{\phi}(x_{3})\vert 0\rangle\langle 0\vert\mathcal{T}\hat{\phi}(x_{2})\hat{\phi}(x_{3})\vert 0\rangle
\end{align}
```
## Update Notes
### Version 1.1.2
New features:
- Export Wick-contractions for real scalar field as a csv-file
- Generate LaTeX-file containing the Wick-contractions for the real scalar field
### Version 1.1.1
Wick contraction for real scalar field now counts repeated contractions and prints the according multiple.
### Version 1.1
Updated README.md. Included output parameter for Wick contractions.
### Version 1.0
Initial upload of the programm. Only the basic file-structure and logic for real scalar field Wick contractions is implemented.
