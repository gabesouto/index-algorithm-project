# Document Indexing Project

This project involves the implementation of a document indexing system similar to what Google uses. The program consists of two main modules: a file management module and a search module. The main objective is to allow users to attach TXT format text files and perform efficient searches on these files.

## Features

### File Management Module

The file management module allows the user to:

1. Attach text files (TXT format): Users can add TXT format documents to the system for later indexing and searching.

2. Store information about the files: The program should store metadata about the files, such as name, creation date, size, and other relevant information.

3. Index terms in the documents: The program should extract significant terms from the documents and store them in a suitable data structure for efficient searches.

### Search Module

The search module allows the user to:

1. Perform searches for terms: Users can input search terms and receive a list of documents that contain those terms.

2. Present relevant results: The program should be capable of sorting search results based on relevance, taking factors like term frequency in documents into account.

3. View detailed information: Users can access detailed information about each document, including name, creation date, and sections of text containing the search terms.

## Technical Requirements

To implement this project, skills in the following areas are required:

- Stack Manipulation: For managing the insertion and removal of documents from the attachment list.

- Deque Manipulation: For performing efficient search operations and presenting results in order.

- Node and Linked Lists Manipulation: For storing and managing indexed terms in documents.

- Doubly Linked Lists Manipulation: For storing and managing document metadata.

## Important Notes

- This project does not include the analysis of meanings or the search for synonyms in documents. The search is based solely on the exact occurrence of terms provided by the user.

- Efficiency in indexing and searching is crucial for the user experience, so optimize your algorithm and data structures to handle large volumes of documents and queries.

## Running the System

To run this system on your local environment, follow the steps below:

1. Clone this repository to your machine:

   ```sh
   git clone git@github.com:gabesouto/index-algorithm-project.git

2. Navigate to the project directory:
    ```sh
   cd index-algorithm-project
    
3. Create a Python virtual environment to isolate project dependencies:
     ```sh
     python3 -m venv .venv

4. Activate the virtual environment:
     ```sh
     source .venv/bin/activate

5. Now that the virtual environment is active, install project dependencies from the dev-requirements.txt file:
    ```sh
    python3 -m pip install -r dev-requirements.txt

### 🐍
   


