# Module to read spectrum data from ASCII files with two columns (wavelength/frequency/wavenumber and flux).

import pandas as pd
class ReadAscii:
    """
    Class to read spectrum data from ASCII files with two columns (wavelength/frequency/wavenumber and flux).

    Attributes:
        file_path (str): Path to the ASCII file.
        data (pd.DataFrame): Data loaded from the file.
    """

    def __init__(self, file_path: str, colnames:list=['wave', 'flux']):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Load data from an ASCII file with two columns.
        The first column is assumed to be wavelength/frequency/wavenumber,
       
        """
        try:
            self.data = pd.read_csv(self.file_path, delim_whitespace=True, header=None, names=colnames)
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def get_data(self):
        """Return the loaded data."""
        return self.data