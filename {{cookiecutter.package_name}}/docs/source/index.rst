{% for number in range("%s: %s"|format(cookiecutter.project_name, cookiecutter.short_description)|count) %}*{% endfor %}

{{cookiecutter.project_name}}: {{cookiecutter.short_description}}
{% for number in range("%s: %s"|format(cookiecutter.project_name, cookiecutter.short_description)|count) %}*{% endfor %}



{{cookiecutter.long_description}}

Main Features
-------------

* |:zap:| User-friendly
* |:rocket:| Easy to scale
* |:bird:| Light package, minimal dependencies
* |:tools:| Actively maintained by Mindee


.. toctree::
   :maxdepth: 2
   :caption: Getting started
   :hidden:

   getting_started/installing


.. toctree::
   :maxdepth: 2
   :caption: Package Reference
   :hidden:

   modules/module


.. toctree::
   :maxdepth: 2
   :caption: Contributing
   :hidden:

   contributing/contributing
