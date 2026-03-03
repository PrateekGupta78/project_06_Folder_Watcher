import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from cleaner import clean_data
from config import WATCH_FOLDER, OUTPUT_FOLDER

class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        print("New file detected:", file_path)

        cleaned_df = clean_data(file_path)

        filename = os.path.basename(file_path)
        output_path = os.path.join(OUTPUT_FOLDER, "cleaned_" + filename)

        cleaned_df.to_csv(output_path, index=False)
        print("Cleaned file saved!")

if __name__ == "__main__":
    observer = Observer()
    handler = MyHandler()
    observer.schedule(handler, WATCH_FOLDER, recursive=False)

    observer.start()
    print("Watching folder...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()