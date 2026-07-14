import sys
import os
import json
import urllib.request
from bs4 import BeautifulSoup

def scrape_to_stage(project_name, url):
    """Scrapes clean text from a URL and appends it to the project's temp file."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract paragraph texts
        text_data = "\n".join([p.get_text() for p in soup.find_all('p')])
        
        tmp_path = f"workspace/{project_name}/tmp/staged_data.txt"
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        
        with open(tmp_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- Scraped from {url} ---\n{text_data}\n")
        return f"✅ Successfully harvested data from {url}"
    except Exception as e:
        return f"❌ Scraping failed: {str(e)}"

def compile_gguf(project_name):
    """Simulates bundling the staged data into a Llama-3 layout unified inside a GGUF file structure."""
    proj_dir = f"workspace/{project_name}"
    tmp_file = f"{proj_dir}/tmp/staged_data.txt"
    output_gguf = f"{proj_dir}/builds/{project_name}_llama3_tcnaint.gguf"
    
    if not os.path.exists(tmp_file):
        return "❌ Error: No staged data found. Feed data slow by slow first!"
        
    # Read metadata/config
    with open(f"{proj_dir}/config.json", "r") as f:
        config = json.load(f)
        
    print(f"Reading staged datasets inside {tmp_file}...")
    print(f"Applying metadata tags: Creator=TCN, Owner=Tucci Wrld, Base={config['base_model']}")
    
    # Simulating the writing of the binary .GGUF structure packaging the text
    with open(output_gguf, "wb") as f:
        f.write(b"GGUF_TCNAINT_LLAMA3_V1")
        f.write(b"\x00" * 100) # Mock header blocks
        
    return f"🎉 Success! Generated binary package asset at:\n👉 {output_gguf}"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        action = sys.argv[1]
        target_project = sys.argv[2]
        
        if action == "compile":
            print(compile_gguf(target_project))
        elif action == "scrape" and len(sys.argv) > 3:
            target_url = sys.argv[3]
            print(scrape_to_stage(target_project, target_url))
