import string
import webbrowser

def generate_and_batch_open(url):
    if not url:
        print("Please enter a valid URL.")
        return

    base_url = url[:-1]
    all_urls = []
    for digit in string.digits:
        all_urls.append(base_url + digit)
    for letter in string.ascii_lowercase:
        all_urls.append(base_url + letter)

    print(f"\nSuccessfully generated {len(all_urls)} URLs.")
    print("We will open them in batches of 5 to avoid crashing your browser.")
    
    batch_size = 6
    for i in range(0, len(all_urls), batch_size):
        batch = all_urls[i:i+batch_size]
        print(f"\n--- Ready to open links {i+1} to {min(i+batch_size, len(all_urls))} ---")
        confirm = input("Press 'Enter' to open these 6 tabs (or type 'q' and Enter to stop): ")
        if confirm.lower() == 'q':
            print("Process stopped.")
            break
        for link in batch:
            webbrowser.open_new_tab(link)
            
        print("Tabs opened! Check your browser, close the error ones, then come back.")
user_url = input("Enter the Study URL here: ")
generate_and_batch_open(user_url)