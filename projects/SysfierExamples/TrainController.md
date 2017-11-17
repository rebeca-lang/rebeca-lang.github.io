---
layout: page
title: Train Controller
permalink: /allprojects/SysfierExamples/TrainController

---

#### Problem Description

The problem is defined as a single railway bridge, which is connected to two ground railways on each side. Each of the railways on the ground is used for trains traveling in one direction, so, a maximum of one trains can arrive at the bridge from each side. But because there is only one railway on the bridge, trains arriving from each direction can not pass simultaneously.

The train controller, is a system to signal the trains to stop, to to pass from the bridge, from each side. The controller gets notified when a train arrives from each side, and when the train which is supposed to pass leaves the bridge.

#### Properties

**Safety:** We want to check the model if there is any possibility that the two trains arriving from each side go on the bridge together, thus causing an accident.

**Starvation:** We want to be sure that each train arriving from any side of the bridge can finally pass, regardless of the traffic on the other side.

#### Model with Two controllers

There are two controllers on two sides of a Bridge. Trains arrive at Left side from n different rails and depart from Right side of the Bridge to n different rails. Trains should pass the bridge one at a time. Each train declares its arrival to the Left Controller and the controller lets the train enter the Bridge if there is no train on the bridge. The train declares its departure to the Right Controller; the Right Controller sends this message to the Left Controller and the Left Controller lets the waiting trains enter the Bridge.

#### Model with N Trains

There are many trains in each side of the bridge. Trains arrive unpredictably and the controller has to manage them in such a way that only one train passes the bridge at a time. Each train declares its arrival to the controller and the controller lets the train enter the bridge if there is no train on the bridge. If the bridge is full the arriving train is put in a queue. The waiting trains will be service according to their position in the queue. Each train should faithfully declare its departure to the controller.

#### Related Files
* The specification of the model [ [zip] ](/assets/projects/Sysfier/case-studies/Train-Controller-Two-Trains.zip)
