# qPHA - Rapid quantitation of microbial intracellular polyhydroxyalkanoates (PHA)
## How to Use
1. Save experimental data to a .csv file. Use the same format as showed in 'Import_data-sample.csv'. For the point needing prediction, please fill the PHA (%) with 'NaN'. (Note: Use 'Save as' of Excel to save the input .csv file, even after editing a .csv file)
2. Import data from .csv files by [Files -> Import data].
3. Select the function for following fitting and prediction.
4. Run parameter estimation. All the data except for the point with 'NaN' PHA (%) will be used for parameter estimation.
5. Run prediction. The predicted PHA (%) will be listed in the window. Use [File -> Save data] to export the prediction results to .csv files. If step 4 was skipped, the default parameters will be applied to the prediction.
6. Use [Files -> Clear all] to clear all the data in the qPHA.