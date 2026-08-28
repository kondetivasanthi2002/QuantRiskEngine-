from setuptools import setup, find_packages

setup(
    name="quantriskengine",
    version="1.0.0",
    description="Enterprise Financial Risk Analytics & Algorithmic Trading Platform",
    author="Antigravity Financial Technologies",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.4.0",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "scipy>=1.11.1",
        "fastapi>=0.98.0",
        "uvicorn>=0.22.0"
    ],
    python_requires=">=3.8",
)
