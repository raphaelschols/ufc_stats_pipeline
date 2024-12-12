import streamlit as st

def dropdown_menus(
    company_label: str,
    company_options: list,
    year_label: str,
    year_options: list,
    default_company=None,
    default_year=None,
):
    """
    Creates dropdown menus in the Streamlit sidebar for selecting company and year.

    Parameters:
    - company_label: A string label for the company dropdown.
    - company_options: A list of options for the company dropdown.
    - year_label: A string label for the year dropdown.
    - year_options: A list of options for the year dropdown.
    - default_company: Default selected value for the company dropdown (optional).
    - default_year: Default selected value for the year dropdown (optional).

    Returns:
    - A tuple (selected_company, selected_year) containing the selected values.
    """

    # Ensure options are lists
    company_options = list(company_options)
    year_options = list(year_options)

    # Select company
    selected_company = st.sidebar.selectbox(
        company_label,
        company_options
    )

    # Select year
    selected_year = st.sidebar.selectbox(
        year_label,
        year_options)

    return selected_company, selected_year

def insert_image(image_path: str, caption: str):
    """
    Inserts an image into the Streamlit app.

    Parameters:
    - image_path: The path to the image file.
    - caption: A caption for the image.
    """
    st.image(image_path, caption=caption)

