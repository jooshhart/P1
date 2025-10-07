import numpy as np
import pandas as pd
import zipfile
import os
import requests
import tempfile

def download_if_url(path_or_url):
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        response = requests.get(path_or_url)
        response.raise_for_status()
        # Save to a temporary file
        suffix = os.path.splitext(path_or_url)[-1]
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmp.write(response.content)
        tmp.close()
        return tmp.name
    return path_or_url

def to_numpy(data_path):
    """
    Loads data from a CSV, XLSX, or ZIP file and returns a numpy array and column names.
    If it's a ZIP file, it will look for a CSV or XLSX inside.
    Accepts a local file path or a URL.
    """
    local_path = download_if_url(data_path)
    # First, check if it's a zip file
    if local_path.endswith('.zip'):
        with zipfile.ZipFile(local_path) as z:
            # Prefer CSV, then XLSX
            csv_names = [name for name in z.namelist() if name.endswith('.csv')]
            xlsx_names = [name for name in z.namelist() if name.endswith('.xlsx')]
            if csv_names:
                with z.open(csv_names[0]) as f:
                    df = pd.read_csv(f)
                    return df.to_numpy(), df.columns.tolist()
            elif xlsx_names:
                with z.open(xlsx_names[0]) as f:
                    df = pd.read_excel(f)
                    return df.to_numpy(), df.columns.tolist()
            else:
                raise ValueError("No CSV or XLSX file found in the ZIP.")
    elif local_path.endswith('.csv'):
        df = pd.read_csv(local_path)
        return df.to_numpy(), df.columns.tolist()
    elif local_path.endswith('.xlsx'):
        df = pd.read_excel(local_path)
        return df.to_numpy(), df.columns.tolist()
    else:
        raise ValueError("Unsupported file type.")