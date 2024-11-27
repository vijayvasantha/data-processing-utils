import pandas as pd # type: ignore

def remove_null_rows(dataframe):
    "Removes rows with any null (NaN) values"
    return dataframe.dropna()


def remove_null_columns(dataframe):
    "Removes columns with any null (NaN) values."
    return dataframe.dropna(axis=1)


def fill_null_values(dataframe, value):
    "Fills null (NaN) values with a specified value."
    return dataframe.fillna(value)


def analyze_nulls(dataframe):
    "Provides a summary of null (NaN) values in the dataset."
    total_nulls = dataframe.isnull().sum()
    percentage_nulls = (total_nulls / len(dataframe)) * 100
    return {
        "null_counts": total_nulls,
        "percentage_nulls": percentage_nulls
    }


if __name__ == "__main__":
    # Example 
    data = {
        "Name": ["Alice", "Bob", None, "David"],
        "Age": [24, None, 35, 29],
        "City": ["New York", None, "Los Angeles", None]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    print("\nRemove Rows with Nulls:")
    print(remove_null_rows(df))

    print("\nRemove Columns with Nulls:")
    print(remove_null_columns(df))

    print("\nFill Nulls with a Default Value:")
    print(fill_null_values(df, "Unknown"))

    print("\nNull Analysis:")
    print(analyze_nulls(df))
