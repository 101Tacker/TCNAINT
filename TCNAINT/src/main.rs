use clap::{Parser, Subcommand};
use std::fs::{create_dir_all, OpenOptions};
use std::io::Write;
use std::path::PathBuf;
use std::process::Command;

#[derive(Parser)]
#[command(name = "TCNAINT")]
#[command(author = "Created by TCN | Owned by Tucci Wrld")]
#[command(version = "1.0")]
#[command(about = "TUCCI CYBER NATION AI neural tech - Llama 3 GGUF Compiler", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Create a new AI project workspace
    New { name: String },
    /// Feed complex data "slow by slow" into a project's temporary file
    Feed { name: String, data: String },
    /// Trigger the Python AI engine to harvest web data or compile into .GGUF
    Generate { name: String },
}

fn get_project_dir(name: &str) -> PathBuf {
    PathBuf::from("workspace").join(name)
}

fn main() {
    let cli = Cli::parse();

    println!("--- TUCCI CYBER NATION AI NEURAL TECH (TCNAINT) ---");
    println!("Creator: TCN | Owner: Tucci Wrld\n");

    match &cli.command {
        Commands::New { name } => {
            let proj_dir = get_project_dir(name);
            create_dir_all(proj_dir.join("tmp")).unwrap();
            create_dir_all(proj_dir.join("builds")).unwrap();
            
            // Create default config
            let config_path = proj_dir.join("config.json");
            std::fs::write(config_path, r#"{"base_model": "Llama-3", "quantization": "Q4_K_M"}"#).unwrap();
            
            println!("🚀 Project '{}' initialized successfully.", name);
        }
        Commands::Feed { name, data } => {
            let tmp_file_path = get_project_dir(name).join("tmp").join("staged_data.txt");
            
            let mut file = OpenOptions::new()
                .create(true)
                .append(true)
                .open(&tmp_file_path)
                .expect("Failed to open temporary staging file");

            writeln!(file, "{}", data).expect("Failed to write data");
            println!("📥 Data staged incrementally to temporary file for project '{}'.", name);
        }
        Commands::Generate { name } => {
            println!("⚙️ Compiling project '{}' into Llama 3 .GGUF format...", name);
            // Calling the Python AI utility to handle Llama-3 parsing & GGUF quantization
            let output = Command::new("python3")
                .arg("python/ai_engine.py")
                .arg("compile")
                .arg(name)
                .output()
                .expect("Failed to execute AI compilation engine");

            println!("{}", String::from_utf8_lossy(&output.stdout));
        }
    }
}
