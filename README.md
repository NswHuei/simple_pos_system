# Simple POS System for a Family Supermarket

## 🎯 Project Overview

This project is a custom-built, lightweight Point of Sale (POS) system designed specifically for the daily operations of my family's small supermarket. The goal is to create a simple, intuitive, and efficient tool to manage inventory and sales.

✨ ## Core Features (MVP v0.1 - Completed)

The current Minimum Viable Product (MVP) provides the foundational **Inventory Management Engine** for the system. It is a fully functional application that allows for:

-   **Product Database Management:** Direct interaction with the SQLite database to **Add**, **Search**, and **Delete** product information, forming the core logic of the inventory system.

*(A screenshot of the database interaction or basic UI can be added here)*

---

🚀 ## Future Roadmap

With the core database engine in place, the next steps focus on building the user-facing features and adding intelligent automation.

### Phase 1: Core POS Functionality (Up Next)
-   [ ] **Barcode Integration:** Implement barcode scanning (using a library like `pyzbar`) to instantly add or look up products.
-   [ ] **Sales Recording Module:** Develop the interface and logic to process and record sales transactions.
-   [ ] **GUI Enhancement:** Evolve the current Tkinter interface to be more user-friendly for daily operations.

### Phase 2: AI-Powered Automation (Planned)
-   **Objective:** Eliminate manual data entry for new stock by automatically scanning supplier invoices using an LLM to perform OCR and data extraction.
-   **Proposed Workflow:** The LLM will process scanned invoices and format the extracted data into a structured CSV or JSON file for batch import.

### Phase 3: Modularization & Refactoring (Ongoing)
-   **Objective:** Refactor the current MVP codebase into a more modular architecture to simulate a professional development workflow, making the system easier to maintain, test, and scale.
