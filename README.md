# Employee-Company Data Upload API

This Django-based application provides an API to upload employee data from an Excel file, which contains employee information and the associated company name. The data is then inserted into two tables in the database: `Employee` and `Company`. A one-to-many relationship is established where one company can have multiple employees.

## Features

- Upload an Excel file containing employee data.
- Automatically read and insert data into two related tables: `Employee` and `Company`.
- Establish a one-to-many relationship between `Company` and `Employee`.
- API built with Django and Django REST Framework (DRF).
- File validation to ensure only Excel files (.xlsx, .xls) are uploaded.

## Requirements

Before running the application, make sure to install the required dependencies listed in `requirements.txt`:

- **Django**: The web framework used for building the application.
- **Django REST Framework (DRF)**: For building API views and serializers.
- **pandas**: For reading and processing Excel files.
- **openpyxl**: Required by pandas to handle `.xlsx` files.

### Setup Instructions

1. **Clone the repository** (or copy the project files):

   ```bash
   git clone "https://github.com/toromayuri98/BrainerHub_Solution-Assisment.git"

