---
layout: page
title: RoboRebeca
permalink: /allprojects/RoboRebeca

---
#### Project 1: Automatic translation of Rebeca models to ROS, Advantages and Challenges
#### Problem Description 
ROS2 is an increasingly popular middleware framework for developing robotic applications. A ROS2 application basically is composed of nodes that run concurrently and can be deployed distributedly. ROS2 nodes communicate with each other through asynchronous interfaces; they reside in memory and wait to respond events that circulate around the system during the interactions between the robot(s) and the environment. Rebeca is an actor-based language for modelling asynchronous, concurrent applications. Timed Rebeca added timing features to Rebeca to deal with timing requirements of real-time systems. The similarities in the concurrency and message-based asynchronous interactions of reactive nodes justify the relevance of using Timed Rebeca to assist the development and verification of ROS2 applications. Model-based development and model checking allow quicker prototyping and earlier detection of system errors without the requirement of developing the entire real system. However, there are challenges in bridging the gaps between continuous behaviours in a real robotic system and discrete behaviours in a model, between complex computations in a robotic system and the inequivalent programming facilities in a modelling language. There have been previous attempts in mapping Rebeca to ROS, however they could not be put into practice due to over-simplifications or improper modelling approaches. This thesis addresses the problem from a more systematic perspective and has been successful in modelling a realistic multiple autonomous mobile robots system, creating corresponding ROS2 demonstration code, showing the synchronization between the model and the program to prove the values of the model in driving development and automatic verification of correctness properties (freedom of deadlocks, collisions, and congestions). Stability of model checking results confirms design problems that are not always detected by simulation. The modelling principles, modelling and implementing techniques that are invented and summarized in this work can be reused for many other cases.

#### Case Studies 
* Master Thesis: MODEL-BASED DEVELOPMENT & VERIFICATION OF ROS2 ROBOTIC APPLICATIONS USING TIMED REBECA [ [pdf] ](https://www.diva-portal.org/smash/get/diva2:1767802/FULLTEXT01.pdf). 
* Presentation: [ [pdf] ](/assets/projects/RoboRebeca/Hiep-ModellingROS2inTimedRebeca.pdf)
  


#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Hong Hiep Trinh



#### Project 2: An automatic code generation tool for converting Rebeca models to ROS
#### Problem Description 
RoboRebeca is a framework to develop safe/correct codes for robotic applications. We suggest some modeling patterns to model robotic control systems using TRebeca language and propose an automatic code generation tool for converting Rebeca models to ROS.
The models can be model checked/ analyzed/verified against desired properties in Afra, and then can be automatically transformed into correct ROS codes right there in Afra 3.0.
Our toolset fully covers this chain for creating safe ROS codes for the robotic application. 
More details about this project is provided in this presentation: <a class="link link_presentation" href="/assets/projects/RoboRebeca/RoboRebeca.pptx">pptx</a>

This work is continued in "[Software for Safe Mobile Robots with ROS 2 and Rebeca](/assets/theses/SOFTWARE-FOR-SAFE-MOBILE-ROBOTS-WITH-ROS2-AND-REBECA.pdf)" master thesis. This work focuses on a scenario in which mobile robots move from a starting position to the target position. Models of various ROS 2 components utilised in mobile robots are developed and both single- and multi- robot scenarios are verified.

#### Case Studies 
* The demo of Volvo Autonomous machines: [ [movie] ](/assets/projects/RoboRebeca/automaticConversionChain.mp4) (by Bahar Salmani). 
* Traffic Light Model: [ [zip] ](https://github.com/rebeca-lang/rebeca-lang.binaries/raw/master/Traffic%20Light%20Case.zip) (by Bahar Salmani). 
* Train Controller Model: [ [zip] ](https://github.com/rebeca-lang/rebeca-lang.binaries/raw/master/Train%20Contoller.zip) (by Bahar Salmani). 
* Kobuki Robot Controller Model: [ [zip] ](https://github.com/rebeca-lang/rebeca-lang.binaries/raw/master/Kobuki%20Case.zip) (by Bahar Salmani). 
* HXVolvo Model: [ [zip] ](https://github.com/rebeca-lang/rebeca-lang.binaries/raw/master/HXVolvo%20Case.zip) (by Bahar Salmani). 
* Rebeca Models, Developed as a part of "Software for Safe Mobile Robots with ROS 2 and Rebeca" Master Thesis: [ [zip] ](/assets/projects/RoboRebeca/MobileRobots.zip) (Kostiantyn Sharovarskyi). 

#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Bahar Salmani
* Giorgio Forcina
* Ehsan Khamespanah
<!--  {% comment %}
#### Related Publications
- Giorgio Forcina, Ali Jafari, Ehsan Khamespanah, Stephan Baumgart, Marjan Sirjani: AdaptiveFlow: An Actor-based Eulerian Framework for Track-based Flow Management, Submitted to SAC 2019.
FOCLASA, 2017  [ [pdf] ](/assets/papers/2017/LightweightPreprocessingForAgent-BasedSimulationOfSmartMobilityInitiatives.pdf) [ [report] ](/assets/projects/Tangramob/reports/tech-report.pdf) [ [model] ](/assets/projects/tangramob/case-studies/model-smi1.rebeca)
{% endcomment %} -->
