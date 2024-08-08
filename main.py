import streamlit as st
from views.page_inity import view_main_page
from services.database import connect_to_database

def main():
    conn = connect_to_database()
    if conn is None:
        return

    view_main_page(conn)

if __name__ == "__main__":
    main()
