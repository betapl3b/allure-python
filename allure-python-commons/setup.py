from setuptools import setup

PACKAGE = "allure-python-commons"

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
]

install_requires = [
    "attrs>=16.0.0",
    "pluggy>=0.4.0",
]


def main():
    setup(
        name=PACKAGE,
        use_scm_version={"root": "..", "relative_to": __file__},
        setup_requires=['setuptools_scm'],
        description="Common module for integrate allure with python-based frameworks",
        url="https://allurereport.org/",
        project_urls={
            "Source": "https://github.com/allure-framework/allure-python",
        },
        author="QAMetaSoftware, Stanislav Seliverstov",
        author_email="sseliverstov@qameta.io",
        license="Apache-2.0",
        classifiers=classifiers,
        keywords="allure reporting report-engine",
        packages=["allure_commons"],
        package_dir={"allure_commons": 'src'},
        install_requires=install_requires,
        py_modules=['allure', 'allure_commons'],
        python_requires='>=3.6'
    )


if __name__ == '__main__':
    main()
