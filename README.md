# GUI design software for the __qPHA__ method
## About the software
The software is built for the **qPHA** method [1].

## How to Use
0. Directly run qPHA.exe or run ./Python/qPHA.py with Python 3.
1. Save experimental data to a .csv file. Use the same format as 'Import_data-sample.csv'. For the point needing prediction, please fill the PHA (%) with 'NaN'. (**Note**: Use 'Save as' function of Excel to save the input .csv file, even after editing a .csv file)
2. Import data from .csv files by [Files -> Import data].
3. Select the function for following fitting and prediction.
4. Run parameter estimation. All the data except for 'NaN' PHA (%) will be used for parameter estimation.
5. Run prediction. The predicted PHA (%) will be listed in the window. Use [File -> Save data] to export the prediction results to .csv files. If step 4 was skipped, the default parameters will be applied to the prediction function.
6. Use [Files -> Clear all] to clear all the data in the qPHA software.

## References
[1]. 