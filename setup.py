from setuptools import find_packages,setup

setup(

    name='mcqgenerator',
    version='0.0.1',
    author='dipayan majumder',
    author_email='majumderd007@gmail.com',
    
    install_requires=['google-generativeai','langchain','streamlit','python-dotenv','PyPDF2','pandas','langchain_community'],
    packages=find_packages(),


)