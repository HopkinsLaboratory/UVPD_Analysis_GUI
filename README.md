# UVPD Analysis GUI

## Introduction
This repository contains a Graphical User Interface (GUI) designed for the analysis of variable wavelength Ultraviolet Photodissociation (UVPD) data. It's specifically tailored for data obtained on the modified QTRAP 5500 hybrid triple-quad in the Hopkins Lab.

## Prerequisites
Before using the UVPD Analysis GUI, ensure that the following software and packages are installed on your local machine:

### Required Software
- **GitHub Desktop**: Download from [GitHub Desktop](https://desktop.github.com/). A GitHub account is not required for installation.
- **Git**: Download from [Git SCM](https://git-scm.com/). Please install in the default location and add it to PATH if necessary. A GitHub account is not required for installation.
- **Python 3.12+**: Download and install from [Python Downloads](https://www.python.org/downloads/).
-**Proteowizard's msconvert package**: Download and install the latest version from [Proteowizard Downloads](https://proteowizard.sourceforge.io/download.html). Install in the default directory.

### Required Python Packages
The GUI depends on several Python packages. Install them using the following command in your command prompt:

```console
pip install numpy lxml pandas PyQt6 pyteomics gitpython
```

### PATH Configuration

After installation, add the following directories to your system's PATH. These contain the necessary executables `msconvert.exe` and `fileinfotoxml.exe`:

```text
C:\Program Files (x86)\ProteoWizard\ProteoWizard 3.0.11392
C:\Program Files (x86)\ProteoWizard\ProteoWizard 3.0.11392\FileInfoToXml
```
*Note: The version number in the paths might vary slightly.*

### Setup and Usage

After completing the installation and configuration steps, you can proceed with setting up and using the UVPD Analysis GUI.

## Getting Started

To launch the GUI, run `UVPD_GUI.py` located in the `GUI` directory in your preferred Python environment. Ensure that the following packages are installed: `GitHub Desktop`, `Git`, and `msconvert`.

Also ensure that the following python packages are installed: `numpy`, `lxml`, `pandas`, `PyQt6`, `pyteomics`, and `gitpython`. 

If any of these packages are missing, you will be prompted to install them upon launching the GUI.

## GUI Initialization

Once initialized, the interface can be populated with information in the following fields:

- **Directory:** The directory containing the .wiff files. Each scan saved to the .wiff file follows the naming convention 'Laser_On_XXXnm', where XXX is the wavelength of the laser light used for UVPD.

- **Base Peak Range:** The upper and lower m/z values encompassing the parent ion peak. Enter two comma-separated numbers (e.g., 202.5, 204).

- **Fragment Ion Ranges:** The upper and lower m/z values encompassing each fragment ion formed via UVPD. Enter pairs of values enclosed by brackets and separated by commas (e.g., (50.5, 51.5),(102.5, 103.5),(125.5, 127.9).

- **Extract mzML files from .wiff checkbox:** If checked, .mzML files will be created for all scans in the specified directory. If unchecked, the code will look for .mzML files in the mzML directory (automatically created if checked).

- **Normalize to Laser Power checkbox:** If checked, normalizes photofragmentation efficiency to laser power (recommended). If unchecked, photofragmentation efficiency will not be normalized. Specify the powerdata.csv file in the corresponding dialog box.

- **Print Raw Data checkbox:** If selected, the full mass spectrum for each scan in the .wiff file will be printed to a .csv.

## Example Usage

Same data is provided to demonsate the GUI's utility:

1. Use the data in the `ExampleData_beforeAnalysis` directory.
2. Populate the GUI with the following information to mimic the outputs found in the `ExampleData_afterAnalysis` directory:

   - **Base Peak Range:** 239.0,242.0
   - **Fragment Ion Ranges:** (54.5,57.0),(114.5,116.0),(129.5,131.0),(139.5,140.5),(141.5,142.8),(153.5,154.5),(156.5,158.0),(167.5,169.0),(170.5,172.0),(180.5,181.8),(182.6,184.0),(184.5,186.0),(198.5,200.0),(208.0,210.0)
   - **Power Data Filename:** powerscan_400_600nm_120us.csv

Please report any bugs in the issues section.
