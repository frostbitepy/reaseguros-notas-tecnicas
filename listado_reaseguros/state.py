import reflex as rx
import pandas as pd
from typing import List
import os
import tempfile



class State(rx.State):

    uploaded_file: list[str]
    df_html: str

    @rx.var
    def uploaded_file(self) -> List[str]:
        """The uploaded file(s)."""
        return []


    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.uploaded_file.append(file.filename)

    async def convert_to_df(self, files: list[rx.UploadFile]) -> pd.DataFrame:
        """Convert a file to a pandas DataFrame.

        Args:
            file: The uploaded file.

        Returns:
            A pandas DataFrame.
        """
        for file in files:
            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file_name = temp_file.name

            # Save the uploaded file to the temporary file
            upload_data = await file.read()
            with open(temp_file_name, "wb") as file_object:
                file_object.write(upload_data)

            # Read the temporary file into a DataFrame
            df = pd.read_csv(temp_file_name)

            # Delete the temporary file
            os.remove(temp_file_name)

            # Convert the DataFrame to HTML and save it
            self.df_html = df.to_html()

        return self.df_html

