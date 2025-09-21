from setuptools import setup, find_packages

setup(
    name="aitco-web",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'flask==2.3.3',
        'pandas==2.0.3',
        'networkx==3.1',
        'google-generativeai==0.3.2',
        'python-dotenv==1.0.0',
        'numpy==1.24.3',
        'plotly==5.18.0',
        'gunicorn==21.2.0',
    ],
    python_requires='>=3.10.0',
)
