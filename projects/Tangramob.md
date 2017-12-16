---
layout: page
title: Tangramob
permalink: /allprojects/Tangramob

---

#### Problem Description
Understanding the impacts of a mobility initiative prior to deployment is a complex task for both urban planners and transport companies.
To support this task, [Tangramob](https://www.tangramob.com/) offers an Agent-Based (AB) simulation framework for assessing the evolution of urban traffic after the introduction of new mobility services. This allows urban planners and transport companies to evaluate the efficacy of their initiatives with respect to the current urban system. However, Tangramob simulations are computationally expensive due to their iterative nature. Thus, we simplified the Tangramob model into a Timed Rebeca (TRebeca) model and we designed ToolTRain, i.e. a tool-chain that:

1. generates instances of the TRebeca model starting from the same input files of Tangramob;
1. runs the resulting model in order to obtain its statespace;
1. infers a list of output measures from the statespace obtained from the previous step.
      
ToolTRain thus allows users to get an idea of how mobility initiatives affect the performance of an urban system in a short time, without running simulations. In particular, the experimenter can use ToolTRain to understand which initiatives are more in line with his expectations, so as to simulate them later with Tangramob to get more details.


##### The architecture of ToolTRain

<img align="right" width="100%" src="{{ "/assets/projects/Tangramob/Tangramob-pipeline.png" | absolute_url }}" alt="Tangramob Pipeline" />

The conceptual organization and architecture of ToolTRain can be reused in other AB contexts, thereby exploiting the power and the expressiveness of actor-based formal languages like Rebeca in order to reproduce the behavior of a certain phenomenon with an acceptable fidelity and few implementation efforts.

#### Case Studies

- An abstract version (pseudo-code) of the Tangramob TRebeca model: [ [Rebeca model] ](/assets/projects/Tangramob/case-studies/TRebeca-pseudocode.rebeca)
- The source code of an example of Tangramob TRebeca model: [ [Rebeca model] ](/assets/projects/Tangramob/case-studies/TRebeca-example.rebeca)
- The runnable model: [ [Rebeca model] ](/assets/projects/tangramob/case-studies/model-smi1.rebeca)


#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Carlo Castagnari
* Jacopo de Berardinis
* Giorgio Forcina
* Ali Jafari
* Ehsan Khamespanah

#### Related Publications
- Carlo Castagnari, Jacopo de Berardinis, Giorgio Forcina, Ali Jafari, Marjan Sirjani: Lightweight Preprocessing for Agent-Based Simulation of Smart Mobility Initiatives, FOCLASA, 2017  [ [pdf] ](/assets/papers/2017/LightweightPreprocessingForAgent-BasedSimulationOfSmartMobilityInitiatives.pdf) [ [report] ](/assets/projects/Tangramob/reports/tech-report.pdf) [ [model] ](/assets/projects/tangramob/case-studies/model-smi1.rebeca)


