import pandas as pd

def load_raw_data(path='data/raw/Talent_Academy_Case_DT_2025.xlsx', sheet_name=0):
    """
    Excel dosyasından ham veriyi yükler ve DataFrame olarak döndürür.
    """
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df

if __name__ == "__main__":
    df = load_raw_data()
    print(df.head(3))
