from setuptools import setup, find_packages

setup(
    name="pacure-ai-labs",
    version="1.0.0",
    author="Pacure AI Team",
    description="WCAI: Web Code Picture AI - Generación de juegos 3D (HTML/JS) desde texto e imágenes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pacureok/pacure-ai-labs",
    packages=find_packages(),
    install_requires=[
        # Versiones controladas para evitar el error que tuviste en Kaggle
        "transformers>=4.41.0,<5.0.0",
        "pydantic>=2.0,<2.10",
        "accelerate",
        "bitsandbytes",
        "torch",
        "sentence-transformers",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.10',
)
