---
layout: page
title: Distributed Controllers
permalink: /allprojects/DistributedControllers

---

#### Description
A potential problem that may arise in the domain of distributed control systems is the existence of more than one primary controller in redundancy plans that may lead to inconsistency. An algorithm called NRP FD is proposed to solve this issue by prioritizing consistency over availability. 
In this project, we modeled and formally verified NRP FD using Timed Rebeca and its model checker Afra. 
For model checking, we consider the regular system behaviour, and scenarios where we have failures of Distributed Control Nodes (DCN) and switches. We examine all the possible failure combinations of DCNs and switches at the start of handling an event and also at specific points in time and perform model checking to provide a comprehensive analysis.

We have discovered an issue in where we may have two primary controllers at the same time. We then provide a solution to mitigate the identified issue, thereby enhancing the robustness and reliability of such systems. 

It's worth noting that this project is undertaken in collaboration with ABB Industrial Automation, Process Control Platform, in Västerås, Sweden.

#### Case Studies
*[ NRP FD ](https://itrust.sutd.edu.sg/testbeds/secure-water-treatment-swat/) Code: 
<a class="link link_download" href="https://github.com/fereidoun-moradi/SWaT-Rebeca-Model">download</a>

*[ Leasing NRP FD ] Code: 
<a class="link link_download" href="https://github.com/fereidoun-moradi/SWaT-Rebeca-Model">download</a>


#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* Bahman Pourvatan
* Bjarne Johansson
* Zahra Moezkarimi
* Alessandro Papadopoulos

