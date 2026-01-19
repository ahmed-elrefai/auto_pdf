import os
import urllib.request
import sys

# URL for the GTK3 installer (standard one recommended for WeasyPrint on Windows)
GTK_INSTALLER_URL = "https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe"
INSTALLER_FILENAME = "gtk3-runtime-installer.exe"

def download_file(url, filename):
    print(f"Downloading GTK3 installer from {url}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Download complete: {filename}")
        print("Please run this installer to set up the required dependencies for PDF generation.")
    except Exception as e:
        print(f"Failed to download installer: {e}")

if __name__ == "__main__":
    download_file(GTK_INSTALLER_URL, INSTALLER_FILENAME)
