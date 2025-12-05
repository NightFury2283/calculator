from setuptools import setup

setup(
    name="calculator",
    version="1.0.0",
    description="Calculator",
    long_description="Very complicated app for mathematics.",
    py_modules=["calc_gui"],
    entry_points={
        "console_scripts": [
            "calculator = calc_gui:main",
        ],
    },
)