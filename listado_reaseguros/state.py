import reflex as rx
import pandas as pd
from typing import List
import os
import asyncio
import glob


class State(rx.State):
    # A base var for the list of colors to cycle through.
    colors: list[str] = [
        "black",
        "red",
        "green",
        "blue",
        "purple",
    ]

    # A base var for the index of the current color.
    index: int = 0

    def next_color(self):
        """An event handler to go to the next color."""
        # Event handlers can modify the base vars.
        # Here we reference the base vars `colors` and `index`.
        self.index = (self.index + 1) % len(self.colors)

    @rx.var
    def color(self) -> str:
        """A computed var that returns the current color."""
        # Computed vars update automatically when the state changes.
        return self.colors[self.index]
    
class UploadState(rx.State):
    file_paths: list[str] = []


    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
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
            self.img.append(file.filename)


class FileState(rx.State):
    """The app state."""

    # Whether we are currently uploading files.
    is_uploading: bool

    # DataFrames for the Excel files
    emision_df: pd.DataFrame = pd.DataFrame()
    anulacion_df: pd.DataFrame = pd.DataFrame()
    recupero_df: pd.DataFrame = pd.DataFrame()

    @rx.var
    def file_str(self) -> str:
        """Get the string representation of the uploaded .xlsx files."""
        return "\n".join(file for file in os.listdir(rx.get_asset_path()) if file.endswith('.xlsx'))

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the file upload."""
        self.is_uploading = True

        # Iterate through the uploaded files.
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

        # Stop the upload.
        return FileState.stop_upload
    
    async def convert_to_dataframe(self, filename: str, filepath: str):
        """Convert an uploaded file to a DataFrame."""
        # Read the Excel file and convert it to a DataFrame
        if 'emision' in filename.lower():
            self.emision_df = pd.read_excel(filepath)
        elif 'anulacion' in filename.lower():
            self.anulacion_df = pd.read_excel(filepath)
        elif 'recupero' in filename.lower():
            self.recupero_df = pd.read_excel(filepath)

    async def stop_upload(self):
        """Stop the file upload."""
        await asyncio.sleep(1)
        self.is_uploading = False

    async def clear_xlsx_files(self):
        """Clear all .xlsx files from the uploaded files directory."""
        xlsx_files = glob.glob(os.path.join(rx.get_asset_path(), "*.xlsx"))
        for file in xlsx_files:
            os.remove(file)

    @rx.var
    async def get_dataframe(self, df_type: str) -> pd.DataFrame:
        """Return the appropriate DataFrame based on the parameter passed."""
        if df_type.lower() == 'emision':
            return self.emision_df
        elif df_type.lower() == 'anulacion':
            return self.anulacion_df
        elif df_type.lower() == 'recupero':
            return self.recupero_df
        else:
            raise ValueError("Invalid DataFrame type. Expected 'emision', 'anulacion', or 'recupero'.")