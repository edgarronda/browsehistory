import sqlite3
import os
import platform
import datetime
import pandas as pd

def get_chrome_history():
    # Get default google chrome history path.
    if platform.system() == 'Windows':
        db_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default\History')
    elif platform.system() == 'Darwin':  # macOS
        db_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')
    else:  # Linux
        db_path = os.path.expanduser('~/.config/google-chrome/Default/History')

    if not os.path.exists(db_path):
        print("No se encontró la base de datos del historial de Chrome.")
        return []

    try:
        # Connect to the Google Chrome DB.
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get the browser history.
        cursor.execute('''
            SELECT urls.url, urls.title, visits.visit_time
            FROM urls, visits
            WHERE urls.id = visits.url
            ORDER BY visits.visit_time DESC
        ''')

        # Convert the datetime to human readable.
        history_data = []
        for row in cursor.fetchall():
            url = row[0]
            title = row[1]
            visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[2])
            history_data.append((url, title, visit_time))

        conn.close()

        return history_data

    except sqlite3.OperationalError as e:
        print(f"Error al acceder a la base de datos: {e}")
        return []

def export_to_excel(history, output_file):

    df = pd.DataFrame(history, columns=['URL', 'Título', 'Fecha de Visita'])

    # Save the  history in the Excel file.
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    history = get_chrome_history()
    if history:
        output_file = 'chrome_history.xlsx'
        export_to_excel(history, output_file)
        print(f"Historial exportado a {output_file}")
    else:
        print("No se encontró historial para exportar.")
