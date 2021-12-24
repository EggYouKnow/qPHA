# A GUI design software for the __qPHA__ method

`qPHA.exe` is a GUI design software for the **qPHA** method - a rapid quantification method of polyhydroxyalkanoates (PHA) accumulated in living cells based on green fluorescence proteins labeled phasi.

# Contents

- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [How to use](#How-to-Use)
- [License](#license)
- [Reference](#Reference)

# System Requirements
## Hardware requirements
`qPHA.exe` requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
This package is supported for *Windows*. The package has been tested on the following systems:
+ Windows: Windows 10 Pro (2004)

### Python Dependencies
There is no python dependency when use `qPHA.exe` directly.

Otherwise, it depends on the following Python packages:
```
numpy
scipy
PyQt5
```

# Installation Guide:
Two ways to use qPHA:
1. Unzip the `qPHA.zip` and run `qPHA.exe` in '/qPHA' folder.

2. run ./Python/qPHA.py with Python 3.

It takes few seconds to run the `qPHA.exe`.

# How to Use
1. Save experimental data to a .csv file. Use the same format as the **Demo** file 'Import_data-sample.csv'. For the points need prediction, please fill the PHA (%) with 'NaN'. (**Note**: Use 'Save as' function of Excel to save the input .csv file, even after editing a .csv file)
2. Import data from .csv files by [Files -> Import data].
3. Select the function for following fitting and prediction.
4. Run parameter estimation. All the data except for 'NaN' PHA (%) will be used for parameter estimation. (Around few seconds when data size is similar as the demo)
5. Run prediction. The predicted PHA (%) will be listed in the window. Use [File -> Save data] to export the prediction results to .csv files. If step 4 was skipped, the default parameters will be applied to the prediction function. (Around few seconds when data size is similar as the demo)
6. Use [Files -> Clear all] to clear all the data in the qPHA software.

# License

This project is covered under the **Apache 2.0 License**.

# Reference
