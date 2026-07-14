TCNAINT/
├── Cargo.toml
├── src/
│   └── main.rs          # Rust Backend & CLI Interface
└── python/
    ├── gui.py           # Python PyQt6 GUI Interface
    └── ai_engine.py     # Python Internet Scraping & Llama 3/GGUF Tools


💡 How to Run and Test Your EnvironmentInitialize a Project via CLI:bashcargo run -- new TucciProject
Use code with caution.Feed Data "Slow-by-Slow" via CLI:bashcargo run -- feed TucciProject "First layer of complex structural datasets..."
cargo run -- feed TucciProject "Second layer of complex engineering configurations..."
Use code with caution.Launch the Visual Desktop GUI:bashpython3 python/gui.py