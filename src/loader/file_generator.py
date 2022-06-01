import src.logger as logger
import pandas as pd


def write_csv_from_dict(row: dict, file_name: str) -> bool:
    try:

        def _create_valid_df(row: dict):
            if "mention_driver" in row and row["mention_driver"] != "":
                df = pd.DataFrame(row)
            else:
                df = pd.DataFrame(row, index=[0])
            return df

        df = _create_valid_df(row)
        df.to_csv(file_name, mode="a", index=False, header=False)
        return True
    except Exception as err:
        print(
            "Failed to append row to CSV output",
            {"error": err, "file": file_name, "data": row},
        )
        return False
