import sys
import os
import subprocess
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QMessageBox)
from PyQt6.QtCore import Qt

class TcnaintGui(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("TCNAINT v1.0 - TUCCI CYBER NATION AI neural tech")
        self.setGeometry(100, 100, 650, 500)
        
        layout = QVBoxLayout()
        
        # Branding Header
        header = QLabel("TCNAINT SYSTEM WORKSPACE\nCreated by TCN | Owned by Tucci Wrld")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-weight: bold; font-size: 16px; color: #2c3e50; margin-bottom: 15px;")
        layout.addWidget(header)
        
        # Project Selector / Creator
        proj_layout = QHBoxLayout()
        proj_layout.addWidget(QLabel("Project Name:"))
        self.proj_input = QLineEdit("Alpha_Network")
        proj_layout.addWidget(self.proj_input)
        self.btn_init = QPushButton("Initialize Project")
        self.btn_init.clicked.connect(self.init_project)
        proj_layout.addWidget(self.btn_init)
        layout.addLayout(proj_layout)
        
        # Incremental Slow-by-Slow Data Feeding Block
        layout.addWidget(QLabel("Feed Complex Data (Slow-by-Slow Staging):"))
        self.data_input = QTextEdit()
        self.data_input.setPlaceholderText("Paste raw structural data, code strings, or documentation profiles here...")
        layout.addWidget(self.data_input)
        
        self.btn_feed = QPushButton("Append Data Payload to Temp Cache")
        self.btn_feed.clicked.connect(self.feed_data)
        layout.addWidget(self.btn_feed)
        
        # Web Scraper Automation Engine
        scrap_layout = QHBoxLayout()
        scrap_layout.addWidget(QLabel("Harvest Content URL:"))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://example.com")
        scrap_layout.addWidget(self.url_input)
        self.btn_scrape = QPushButton("Scrape & Stage")
        self.btn_scrape.clicked.connect(self.scrape_url)
        scrap_layout.addWidget(self.btn_scrape)
        layout.addLayout(scrap_layout)
        
        # Target Model Format Setup
        arch_layout = QHBoxLayout()
        arch_layout.addWidget(QLabel("Target Base Architecture:"))
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Llama 3 (Default)", "Mistral-7B", "Phi-3"])
        arch_layout.addWidget(self.combo_box)
        layout.addLayout(arch_layout)
        
        # Compilation Execution
        self.btn_generate = QPushButton("🚀 RUN GENERATE COMMAND (.GGUF)")
        self.btn_generate.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; padding: 10px;")
        self.btn_generate.clicked.connect(self.generate_gguf)
        layout.addWidget(self.btn_generate)
        
        self.setLayout(layout)
        
    def init_project(self):
        name = self.proj_input.text().strip()
        if name:
            # Invoking our compiled Rust binary CLI backend directly to handle multi-project storage structures
            subprocess.run(["cargo", "run", "--", "new", name])
            QMessageBox.information(self, "TCNAINT Status", f"Workspace environment for '{name}' safely constructed via Rust backend.")
            
    def feed_data(self):
        name = self.proj_input.text().strip()
        data = self.data_input.toPlainText().strip()
        if name and data:
            subprocess.run(["cargo", "run", "--", "feed", name, data])
            self.data_input.clear()
            QMessageBox.information(self, "TCNAINT Status", "Incremental snippet appended to secure project temp cache.")
            
    def scrape_url(self):
        name = self.proj_input.text().strip()
        url = self.url_input.text().strip()
        if name and url:
            res = subprocess.check_output(["python3", "python/ai_engine.py", "scrape", name, url]).decode("utf-8")
            QMessageBox.information(self, "Scraper System Output", res)
            self.url_input.clear()
            
    def generate_gguf(self):
        name = self.proj_input.text().strip()
        if name:
            res = subprocess.check_output(["cargo", "run", "--", "generate", name]).decode("utf-8")
            QMessageBox.information(self, "Compilation Core Engine Report", res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TcnaintGui()
    window.show()
    sys.exit(app.exec())
