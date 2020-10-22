---
layout: page
title: AdaptiveFlow
permalink: /allprojects/AdaptiveFlow

---

#### Problem Description
AdaptiveFlow is a framework that allows to model and analyze track-based flow management systems based on a Eulerian model. In this framework, users provide three input files: environment.xml, topology.xml, and configuration.xml and the Python script will process their content and generates the corresponding Timed Rebeca model for model checking and analysis purposes.

The command for running the Python script is: python ModelGenerator.py envFile topFile confFile outFile. In which envFile is the file that contains information about the configuration of the environment to analyze, topFile specifies the position of Point of Interest, confFile contains information about the machines to simulate, outFile is the file that the script will generate containing the model specification. The so generated model can be run with Timed Rebeca Model Checker for further analysis.

<img align="right" width="50%" src="{{ "/assets/projects/AdaptiveFlow/environment.png" | absolute_url }}" alt="AdaptiveFlow Environment" />

Python model generator can be found [here](/assets/projects/AdaptiveFlow/ModelGenerator-v20.py). Examples of the input files of the system in the figure are: [environment.xml](/assets/projects/AdaptiveFlow/example/environment.xml), [topology.xml](/assets/projects/AdaptiveFlow/example/topology.xml), and [configuration.xml](/assets/projects/AdaptiveFlow/example/configuration.xml). An example of a model that violates correctness properties and has a deadlock can be downloaded from [here](/assets/projects/AdaptiveFlow/input-deadlock.zip).

More details about this project is provided in this presentation: <a class="link link_presentation" href="/assets/projects/AdaptiveFlow/Adaptiveflow.pptx">pptx</a>

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Giorgio Forcina
* Ali Jafari
* Ehsan Khamespanah
* Stephan Baumgart

{% comment %}
#### Related Publications
- Giorgio Forcina, Ali Jafari, Ehsan Khamespanah, Stephan Baumgart, Marjan Sirjani: AdaptiveFlow: An Actor-based Eulerian Framework for Track-based Flow Management, Submitted to SAC 2019.
FOCLASA, 2017  [ [pdf] ](/assets/papers/2017/LightweightPreprocessingForAgent-BasedSimulationOfSmartMobilityInitiatives.pdf) [ [report] ](/assets/projects/Tangramob/reports/tech-report.pdf) [ [model] ](/assets/projects/tangramob/case-studies/model-smi1.rebeca)
{% endcomment %}


